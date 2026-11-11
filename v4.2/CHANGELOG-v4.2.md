# CHANGELOG — v4.2 "for all AI"

**Date:** 2026-11-11
**Built from:** v4.1
**Rule followed:** nothing overwritten, nothing erased. v4.0 (repo root) and `v4.1/` are byte-for-byte unchanged. v4.2 lives only in this `v4.2/` folder.

To use v4.2, copy the contents of this folder into a project root, or load files from here.

---

## Goal

Make the SOPs work the same for every AI model and tool, and move rules out of memory and into checks where a tool can enforce them.

## What changed

### 1. `AGENTS.md` is now the one always-on rules file

- `AGENTS.md` is the instruction file that Codex, Cursor, GitHub Copilot, Gemini CLI, Windsurf and most other coding tools read on their own.
- Claude Code reads `CLAUDE.md`, so `CLAUDE.md` is now one line, `@AGENTS.md`, which imports the same rules.
- For chat apps and API calls, paste `AGENTS.md` as the system prompt.
- Every rule from the v4.1 `CLAUDE.md` is still present. Checked with a 42-item concept audit: 0 missing.

### 2. Model-neutral wording

- 41 places that addressed one model by name now say "the agent" (`OPERATOR-CHECKLIST.md`, `TEACH.md`, `USE-FOR-CODING.md`, `USE-FOR-OPERATOR.md`).
- 20 references to `CLAUDE.md` in 11 files now point to `AGENTS.md`.
- Left as written: the source-quality notes, the version history lines, and the archive.

### 3. One copy of the workflow decision

- The SOLO / PLAN_EXECUTE decision now lives only in `AGENTS.md`. `BUILD-GENERAL.md` and `INDEX.md` point to it instead of repeating it.
- GEN_REGEN was added to that one copy so the always-on file is complete.

### 4. Safety rules enforced by a tool (`checks/`)

- `python checks/run_checks.py <path>` checks Python code for P1.1, P1.5, P1.6, P1.7, P1.8, part of P1.2, and Q3.0 / Q3.1, and prints a SELF-PROOF block.
- The linter alone missed `API_KEY = "..."`, so a small McStoots check (MCS105) was added for secret-looking names.
- P1.3, P1.4, P1.9 and the bcrypt part of P1.2 cannot be checked by a tool and still rely on the written rule.

### 5. New rule for models that cannot run commands

- A chat-only model has no way to run DONE WHEN. v4.0 and v4.1 left it free to write PASS anyway.
- v4.2: such a model must write `Result: NOT RUN`, give Chris the exact command and expected output, and wait. Not done until someone runs it.

### 6. Terms defined once

- MFVP, DONE WHEN, SELF-PROOF and Andon are defined at the top of `AGENTS.md`. They were used in every file but never defined in the thin load, which a model new to the pack has to guess at.

### 7. No tables in the always-on and map files

- `AGENTS.md`, `INDEX.md` and `README.md` use lines and lists instead of tables (67 table lines in v4.1, 0 in v4.2). `INDEX.md` merged three overlapping file lists into one.

### Not changed

All 32 tagged rules (P1.x, Q1.x, Q2.x, Q3.x, S1.x) are word-for-word the same as v4.1. Stack files, quality gates and experimental files changed only in the file name they point to.

---

## Size, measured (tokens, OpenAI o200k tokenizer; other models differ slightly)

- Always-on file: 970 → 1,029. Slightly larger, because it gained four things: term definitions, GEN_REGEN, the no-tools rule, and the checks pointer.
- `INDEX.md`: 1,074 → 865.
- Session start (always-on + index): 2,044 → 1,894, about 7 percent smaller.
- Thin load for a Python build: 2,882 → 2,938, about 2 percent larger.

Plain statement: v4.2 is not a big compaction. The v4.0 always-on file was already tight. The gain in v4.2 is that every AI reads the same rules and six rules no longer depend on the AI remembering them.

---

## SELF-PROOF

```
GOAL:        One SOP pack every AI can use; tool-enforce what a tool can check.
WORKFLOW:    PLAN_EXECUTE
DONE WHEN:   checker fails bad code and passes clean code; no rule lost; no broken
             references; v4.0 and v4.1 unmodified.

SELF-PROOF:
  Check:     python checks/run_checks.py on a file breaking P1.1, P1.2, P1.5, P1.6, P1.7, P1.8
  Expected:  FAIL, each rule named
  Result:    PASS
  Evidence:  9 violations reported, exit code 1; every targeted rule appears

  Check:     python checks/run_checks.py on a clean file, and on checks/ itself
  Expected:  PASS
  Result:    PASS
  Evidence:  0 violations, exit code 0, both runs

  Check:     pytest on the MCS105 secret check and the rule mapping
  Expected:  all pass
  Result:    PASS
  Evidence:  4 passed

  Check:     tagged rule comparison v4.1 vs v4.2
  Expected:  same IDs, same text
  Result:    PASS
  Evidence:  32 IDs in each, 0 missing, 0 changed

  Check:     AGENTS.md concept audit against v4.1 CLAUDE.md
  Expected:  nothing missing
  Result:    PASS
  Evidence:  42 of 42 present

  Check:     file reference scan of v4.2
  Expected:  no reference to a file that does not exist
  Result:    PASS
  Evidence:  0 broken

  Check:     git status on v4.0 and v4.1 files
  Expected:  no tracked file modified
  Result:    PASS
  Evidence:  only new path is v4.2/

  Check:     compliance A/B across models (does v4.2 get followed better than v4.0?)
  Expected:  equal or better
  Result:    NOT RUN
  Evidence:  needs Chris's OpenRouter A/B harness on his PC
```

---

## Open items (need Chris)

1. **Run the A/B test.** v4.2 has not been measured against v4.0 on real builds. Until it is, treat it as a candidate.
2. **`run_checks.py` was tested on Linux only.** It uses nothing platform-specific, but it has not been run on Windows.
3. **The secret check goes by variable name** and can flag a harmless value such as `TOKEN_URL`. See `checks/README.md`.
4. **Checks cover Python only.** Web, mobile and embedded have no tool-enforced set yet.
5. Open items 1 to 6 from `CHANGELOG-v4.1.md` still stand.
