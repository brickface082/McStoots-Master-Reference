#!/usr/bin/env python3
"""Run the tool-enforced McStoots SOP rules on a Python project.

Usage:  python checks/run_checks.py <path>

Prints a SELF-PROOF style result and exits 0 on PASS, 1 on FAIL,
2 if the checker itself could not run.
"""

import ast
import json
import pathlib
import re
import subprocess
import sys

RULE_FOR_CODE = {
    "E9": "Q3.0 file must parse",
    "F403": "P1.8 no wildcard imports",
    "F": "Q3.1 linter error",
    "E722": "P1.7 no bare except",
    "S608": "P1.1 parameterized SQL only",
    "S105": "P1.5 no hardcoded secrets",
    "S106": "P1.5 no hardcoded secrets",
    "S107": "P1.5 no hardcoded secrets",
    "S113": "P1.6 HTTP requests need a timeout",
    "S324": "P1.2 no weak hashes",
    "MCS105": "P1.5 no hardcoded secrets",
}
TIMEOUT_SECONDS = 300
SECRET_NAME = re.compile(r"(api_?key|secret|token|passw|pwd|credential)", re.IGNORECASE)
NOT_A_SECRET = re.compile(r"(url|uri|path|file|name|header|prefix|env)$", re.IGNORECASE)
MIN_SECRET_LENGTH = 8


def rule_for(code: str) -> str:
    """Return the SOP rule a ruff code enforces (longest prefix wins)."""
    for prefix in sorted(RULE_FOR_CODE, key=len, reverse=True):
        if code.startswith(prefix):
            return RULE_FOR_CODE[prefix]
    return "unmapped"


def hardcoded_secrets(target: pathlib.Path) -> list[dict]:
    """Find string literals assigned to secret-looking names (API_KEY = "...").

    Covers names the linter's own secret rules miss, such as API_KEY.
    """
    files = [target] if target.is_file() else sorted(target.rglob("*.py"))
    findings = []
    for path in files:
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (SyntaxError, UnicodeDecodeError, OSError):
            continue  # the linter reports files that do not parse (Q3.0)
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                names, value = node.targets, node.value
            elif isinstance(node, ast.AnnAssign) and node.value is not None:
                names, value = [node.target], node.value
            else:
                continue
            is_literal = (isinstance(value, ast.Constant) and isinstance(value.value, str)
                          and len(value.value) >= MIN_SECRET_LENGTH)
            for name in names:
                label = getattr(name, "id", getattr(name, "attr", ""))
                if is_literal and SECRET_NAME.search(label) and not NOT_A_SECRET.search(label):
                    findings.append({
                        "code": "MCS105", "filename": str(path),
                        "location": {"row": node.lineno},
                        "message": f"Hardcoded value assigned to secret-looking name: {label}",
                    })
    return findings


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python checks/run_checks.py <path>")
        return 2
    target = pathlib.Path(argv[1])
    if not target.exists():
        print(f"Path not found: {target}")
        return 2

    config = pathlib.Path(__file__).resolve().parent / "ruff.toml"
    command = [sys.executable, "-m", "ruff", "check", "--config", str(config),
               "--output-format", "json", "--no-cache", str(target)]
    try:
        done = subprocess.run(command, capture_output=True, text=True,
                              timeout=TIMEOUT_SECONDS, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        print(f"Could not run ruff: {exc}")
        return 2
    try:
        findings = json.loads(done.stdout or "[]")
    except json.JSONDecodeError:
        print("Could not run ruff. Install it with:  pip install ruff")
        print(done.stderr.strip())
        return 2

    seen = {(pathlib.Path(f.get("filename", "")).name, (f.get("location") or {}).get("row"))
            for f in findings if str(f.get("code", "")).startswith("S10")}
    for extra in hardcoded_secrets(target):
        key = (pathlib.Path(extra["filename"]).name, extra["location"]["row"])
        if key not in seen:  # do not report the same line twice
            findings.append(extra)
    findings.sort(key=lambda f: (pathlib.Path(f.get("filename", "")).name,
                                 (f.get("location") or {}).get("row", 0)))

    print("SELF-PROOF:")
    print(f"  Check:     python checks/run_checks.py {target}")
    print("  Expected:  0 rule violations")
    print(f"  Result:    {'PASS' if not findings else 'FAIL'}")
    print(f"  Evidence:  {len(findings)} violation(s)")
    for item in findings:
        code = item.get("code") or "E9"
        row = (item.get("location") or {}).get("row", "?")
        name = pathlib.Path(item.get("filename", "?")).name
        print(f"    {name}:{row}  {code}  [{rule_for(code)}]  {item.get('message', '')}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
