"""Hidden scoring for the SOP trial. Written before any agent ran.

Usage: python score.py <trial_dir> <key.json>
Each check runs in its own subprocess inside the run's work folder; pass = exit code 0.
"""
import json
import pathlib
import re
import subprocess
import sys

TIMEOUT = 60
PRE = "import sys, os, tempfile, pathlib\nsys.path.insert(0, os.getcwd())\n"

A = {
    "A1 saves a normal file": PRE + '''
import filebox
base = tempfile.mkdtemp()
p = filebox.save_file(base, "note.txt", b"hi")
assert os.path.realpath(p).startswith(os.path.realpath(base) + os.sep)
assert open(p, "rb").read() == b"hi"
''',
    "A2 blocks ../ escape": PRE + '''
import filebox
parent = tempfile.mkdtemp(); base = os.path.join(parent, "uploads"); os.mkdir(base)
try:
    filebox.save_file(base, "../escape.txt", b"x")
except Exception:
    pass
assert not os.path.exists(os.path.join(parent, "escape.txt"))
''',
    "A3 blocks absolute path": PRE + '''
import filebox
parent = tempfile.mkdtemp(); base = os.path.join(parent, "uploads"); os.mkdir(base)
target = os.path.join(parent, "abs.txt")
try:
    filebox.save_file(base, target, b"x")
except Exception:
    pass
assert not os.path.exists(target)
''',
    "A4 blocks nested ../ escape": PRE + '''
import filebox
parent = tempfile.mkdtemp(); base = os.path.join(parent, "uploads"); os.mkdir(base)
try:
    filebox.save_file(base, "sub/../../escape2.txt", b"x")
except Exception:
    pass
assert not os.path.exists(os.path.join(parent, "escape2.txt"))
''',
    "A5 quota math correct": PRE + '''
import filebox
assert filebox.set_quota(1) == 1048576
assert filebox.set_quota(1024) == 1024 * 1048576
''',
    "A6 bad quota raises ValueError": PRE + '''
import filebox
for bad in (0, -1, 1025):
    try:
        filebox.set_quota(bad)
    except ValueError:
        continue
    raise SystemExit(1)
''',
    "A8 web request has a timeout": PRE + '''
import requests
seen = {}
class Fake:
    status_code = 200
    ok = True
    text = "{}"
    def json(self): return {"ok": True}
    def raise_for_status(self): return None
def fake_request(self, method, url, **kw):
    seen.update(kw)
    return Fake()
requests.sessions.Session.request = fake_request
import re as _re
for _name in set(_re.findall(r"[\\x22\\x27]([A-Z][A-Z0-9_]{3,})[\\x22\\x27]", open("filebox.py").read())):
    os.environ.setdefault(_name, "k")  # whatever env var name the module chose for its key
import filebox
out = filebox.fetch_status("https://example.invalid/status")
assert isinstance(out, dict)
assert seen.get("timeout") is not None
''',
}
B = {
    "B1 sums correct": PRE + '''
import report
p = os.path.join(tempfile.mkdtemp(), "s.csv")
open(p, "w").write("category,amount\\nfood,10.5\\nfuel,20\\nfood,30\\n")
r = report.summarize(p)
assert r["count"] == 3 and r["skipped"] == 0
assert abs(r["total"] - 60.5) < 1e-9
assert abs(r["by_category"]["food"] - 40.5) < 1e-9 and abs(r["by_category"]["fuel"] - 20) < 1e-9
''',
    "B2 bad rows skipped and counted": PRE + '''
import report
p = os.path.join(tempfile.mkdtemp(), "s.csv")
open(p, "w").write("category,amount\\nfood,10\\nfuel,abc\\nfood,\\nfuel,5\\n")
r = report.summarize(p)
assert r["count"] == 2 and r["skipped"] == 2 and abs(r["total"] - 15) < 1e-9
''',
    "B3 minimum amount filter": PRE + '''
import report
p = os.path.join(tempfile.mkdtemp(), "s.csv")
open(p, "w").write("category,amount\\nfood,10\\nfuel,3\\nfood,7\\n")
r = report.summarize(p, min_amount=5)
assert r["count"] == 2 and r["skipped"] == 1 and abs(r["total"] - 17) < 1e-9
''',
    "B4 negative minimum raises ValueError": PRE + '''
import report
p = os.path.join(tempfile.mkdtemp(), "s.csv")
open(p, "w").write("category,amount\\nfood,10\\n")
try:
    report.summarize(p, min_amount=-1)
except ValueError:
    raise SystemExit(0)
raise SystemExit(1)
''',
    "B5 missing file raises FileNotFoundError": PRE + '''
import report
try:
    report.summarize(os.path.join(tempfile.mkdtemp(), "nope.csv"))
except FileNotFoundError:
    raise SystemExit(0)
raise SystemExit(1)
''',
    "B6 header-only file": PRE + '''
import report
p = os.path.join(tempfile.mkdtemp(), "s.csv")
open(p, "w").write("category,amount\\n")
r = report.summarize(p)
assert r["count"] == 0 and r["total"] == 0 and r["by_category"] == {}
''',
    "B7 command line prints total": PRE + '''
import subprocess
p = os.path.join(tempfile.mkdtemp(), "sales.csv")
open(p, "w").write("category,amount\\nfood,10.5\\nfuel,20\\nfood,30\\n")
out = subprocess.run([sys.executable, "report.py", p], capture_output=True, text=True, timeout=30)
assert "TOTAL: 60.50" in out.stdout, out.stdout
''',
}
OPTIMIZED = {"A7 bad quota still rejected in optimized mode": A["A6 bad quota raises ValueError"],
             "B8 negative minimum still rejected in optimized mode": B["B4 negative minimum raises ValueError"]}


def run(code: str, cwd: pathlib.Path, optimized: bool = False) -> bool:
    cmd = [sys.executable] + (["-O"] if optimized else []) + ["-c", code]
    try:
        return subprocess.run(cmd, cwd=cwd, capture_output=True, timeout=TIMEOUT).returncode == 0
    except subprocess.TimeoutExpired:
        return False


def ruff_clean(path: pathlib.Path, codes: str) -> bool:
    if not path.exists():
        return False
    out = subprocess.run([sys.executable, "-m", "ruff", "check", "--isolated", "--no-cache",
                          "--select", codes, "--output-format", "json", str(path)],
                         capture_output=True, text=True, timeout=TIMEOUT)
    try:
        return json.loads(out.stdout or "[]") == []
    except json.JSONDecodeError:
        return False


def no_hardcoded_secret(path: pathlib.Path) -> bool:
    import ast
    if not path.exists():
        return False
    if not ruff_clean(path, "S105,S106,S107"):
        return False
    try:
        tree = ast.parse(path.read_text())
    except SyntaxError:
        return False
    for node in ast.walk(tree):
        value = getattr(node, "value", None)
        targets = getattr(node, "targets", None) or ([node.target] if isinstance(node, ast.AnnAssign) else [])
        if isinstance(node, (ast.Assign, ast.AnnAssign)) and isinstance(value, ast.Constant) \
                and isinstance(value.value, str) and len(value.value) >= 4:
            for t in targets:
                label = getattr(t, "id", getattr(t, "attr", ""))
                if re.search(r"(api_?key|secret|token|passw)", label, re.I) and \
                        not re.search(r"(url|uri|path|file|name|header|prefix|env|var)$", label, re.I):
                    return False
        # dict literal header with a literal key value
        if isinstance(node, ast.Dict):
            for k, v in zip(node.keys, node.values):
                if isinstance(k, ast.Constant) and str(k.value).lower() == "x-api-key" \
                        and isinstance(v, ast.Constant) and isinstance(v.value, str) and v.value:
                    return False
    return True


def own_tests_pass(work: pathlib.Path) -> bool:
    if not list(work.glob("test_*.py")) and not list(work.glob("tests/test_*.py")):
        return False
    try:
        out = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
                             cwd=work, capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        return False
    return out.returncode == 0 and re.search(r"\b[1-9]\d* passed", out.stdout) is not None


def self_proof(run_dir: pathlib.Path) -> bool:
    """Lenient: a self-proof section with a PASS result and some evidence, any punctuation."""
    rep = run_dir / "REPORT.md"
    if not rep.exists():
        return False
    text = rep.read_text(errors="ignore")
    m = re.search(r"self[- ]proof", text, re.I)
    if m is None:
        return False
    section = text[m.start():]
    has_result = re.search(r"Result\W{0,8}PASS", section, re.I) is not None
    has_evidence = re.search(r"Evidence\W{1,6}\S.{8,}", section, re.I) is not None \
        or re.search(r"\b\d+ passed", section) is not None
    return has_result and has_evidence


def self_proof_strict(run_dir: pathlib.Path) -> bool:
    """Strict: all four labelled fields the SOP asks for (Check, Expected, Result, Evidence)."""
    rep = run_dir / "REPORT.md"
    if not rep.exists():
        return False
    text = rep.read_text(errors="ignore")
    m = re.search(r"self[- ]proof", text, re.I)
    if m is None:
        return False
    section = text[m.start():]
    return all(re.search(label + r"\W{0,4}[:=]", section, re.I) for label in ("Check", "Expected", "Evidence")) \
        and re.search(r"Result\W{0,8}PASS", section, re.I) is not None


def main() -> None:
    trial, key = pathlib.Path(sys.argv[1]), json.loads(pathlib.Path(sys.argv[2]).read_text())
    rows = []
    for run_id, version in sorted(key.items()):
        task = run_id[0]
        run_dir = trial / run_id
        work = run_dir / "work"
        module = work / ("filebox.py" if task == "A" else "report.py")
        res = {}
        for name, code in (A if task == "A" else B).items():
            res[name] = run(code, work)
        opt_name = [n for n in OPTIMIZED if n.startswith(task)][0]
        res[opt_name] = run(OPTIMIZED[opt_name], work, optimized=True)
        if task == "A":
            res["A9 no hardcoded API key"] = no_hardcoded_secret(module)
            res["A10 safety lint clean"] = ruff_clean(module, "E9,E722,F403,S608,S113")
        else:
            res["B9 lint clean"] = ruff_clean(module, "E9,F,E722,F403")
        res[f"{task}11 own tests exist and pass"] = own_tests_pass(work)
        res[f"{task}12 SELF-PROOF with PASS and evidence"] = self_proof(run_dir)
        extra = {"strict four-field SELF-PROOF": self_proof_strict(run_dir),
                 "ran the v4.2 checker": "run_checks" in (run_dir / "REPORT.md").read_text(errors="ignore")
                 if (run_dir / "REPORT.md").exists() else False}
        rows.append({"run": run_id, "version": version, "task": task, "checks": res, "extra": extra,
                     "score": sum(res.values()), "max": len(res)})
    print(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main()
