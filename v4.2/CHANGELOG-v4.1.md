# CHANGELOG — v4.1

**Date:** 2026-11-11
**Built from:** v4.0 (commit of 2026-07-17, "SOP v4: one-prompt workflows, decision tree, thinner AI-efficient rules")
**Rule followed:** nothing overwritten, nothing erased. Every v4.0 file in the repo root is byte-for-byte unchanged. v4.1 lives only in this `v4.1/` folder.

To use v4.1, load files from this folder instead of the repo root. To go back, load from the root.

---

## What changed and why

### 1. POKA-YOKE-CONSTRAINTS.md — rule P1.3 was wrong (security)

- **v4.0 said:** build paths only with `os.path.join()`; "this prevents path traversal."
- **Test:** `os.path.join("/srv/uploads", "/etc/passwd")` returns `/etc/passwd`. `../../etc/passwd` also escapes. Joining does not prevent traversal.
- **v4.1 says:** resolve the path, then confirm it sits inside the allowed base folder; reject anything else. Rule ID P1.3 is kept (same rule, corrected text).

### 2. BUILD-PYTHON.md — input checks used `assert`

- **v4.0 example:** docstring promised `ValueError`, code used `assert`. Python deletes every `assert` under `python -O`.
- **Test:** under `python -O`, v4.0 `calculate_discount(-1, 0.1)` returned `-0.9` with no error.
- **v4.1:** outside-input checks use explicit `raise ValueError`. `assert` is kept only for the internal invariant. The test now uses `pytest.raises(ValueError)` so it fails if the wrong error type comes back. Checklist line updated to match.
- **USE-FOR-CODING.md:** one sentence added to NASA Rule 5 pointing to this.

### 3. SOP-ENFORCER-AGENT.md — contradicted thin load

- **v4.0:** "ALWAYS load `USE-FOR-CODING.md`" and "ALWAYS load `QUALITY-GATES.md`", while `INDEX.md` and `CLAUDE.md` say thin load only.
- **v4.1:** enforcer table and notes now match the `INDEX.md` thin-load table. `CLAUDE.md` is still always loaded.

### 4. CLAUDE.md — context stop came too late

- **v4.0:** single stop at ~90%.
- **v4.1:** restores the tiered protocol already written in `MASTER-BACKUP-COMPLETE-SOP.md` (compact at ~70%, prepare state log at ~85%, stop at ~90%). No new numbers were invented.

### 5. BUILD-EMBEDDED.md and BUILD-MOBILE.md — corrupted characters

- Dashes and folder-tree lines had been double-encoded and showed as garbage (for example `â€”`).
- v4.1 repairs them. With non-ASCII characters ignored, both files are identical to v4.0, so no wording changed.

### 6. Housekeeping

- Stray byte-order marks removed from the top of files.
- Version markers set to 4.1 in `CLAUDE.md`, `README.md`, `INDEX.md`. `INDEX.md` improvement log and inventory updated.

### Files with zero changes

`AGENT-WORKFLOW-POLICY.md`, `BUILD-GENERAL.md`, `BUILD-WEB.md`, `MASTER-BACKUP-COMPLETE-SOP.md`, `NEW-PROJECT-STARTUP.md`, `OPERATOR-CHECKLIST.md`, `QUALITY-GATES.md`, `QUALITY-GATES-CORE.md`, `QUALITY-GATES-TOOLS.md`, `REQUIREMENTS-TRANSLATOR.md`, `SANDBOX-EXECUTOR.md`, `SOP-PROCESS-RULES.md`, `TEACH.md`, `USE-FOR-OPERATOR.md`, `WATCHDOG.md`, `hmi_simple_test.py` (byte-order mark removal aside).

---

## SELF-PROOF

```
GOAL:        Correct the v4.0 errors found by running the rules, without touching v4.0.
WORKFLOW:    PLAN_EXECUTE
DONE WHEN:   corrected examples pass tests in normal and -O mode, lint clean,
             no corrupted characters, v4.0 files unmodified.

SELF-PROOF:
  Check:     pytest on the v4.1 Python example + a P1.3 path-safety function
  Expected:  all pass
  Result:    PASS
  Evidence:  7 passed (discount example; path checks for /etc/passwd, ../../etc/passwd,
             a/../../x, ../sibling, and a symlink escape)

  Check:     python -O, calculate_discount(-1, 0.1)
  Expected:  ValueError (v4.0 returned -0.9)
  Result:    PASS
  Evidence:  "ValueError raised: Price must be >= 0, got -1"

  Check:     ruff on both code samples
  Expected:  zero errors (Q3.1)
  Result:    PASS
  Evidence:  "All checks passed!"

  Check:     bandit on both code samples
  Expected:  zero high-severity findings (Q3.2)
  Result:    PASS
  Evidence:  0 high, 0 medium, 1 low (B101 on the one intentional internal assert)

  Check:     corrupted-character scan of v4.1/*.md
  Expected:  none
  Result:    PASS
  Evidence:  0 matches; BUILD-EMBEDDED and BUILD-MOBILE ASCII-identical to v4.0

  Check:     git status on v4.0 files
  Expected:  no tracked file modified
  Result:    PASS
  Evidence:  only new path is v4.1/
```

---

## Open items (not changed — need Chris)

1. **Evidence is not in the repo.** The workflow shootout and SOP A/B results are cited at `C:\Users\brick\McStoots-Docs\findings\`. Until those files are added here, the "validated by A/B" claims cannot be checked by anyone else.
2. **HMI design vs. v4 policy.** The policy says multi-agent chains tested worst. The seven-role HMI design is a multi-agent chain. One of the two needs to change.
3. **Embedded C examples use `assert()` for input checks.** C removes `assert` when built with `NDEBUG`, the same weakness fixed here for Python. Left alone because the right fix depends on the target hardware.
4. **`SANDBOX-EXECUTOR.md` skeleton is three empty functions.** That breaks the pack's own "no TODO / real code" rule. Needs a real implementation or removal of the stubs.
5. **P1.2 allows only bcrypt.** Still safe. Whether to also allow a newer algorithm is a policy choice, not a bug.
6. **`MASTER-BACKUP-COMPLETE-SOP.md` is an archive** and was not reviewed line by line.
