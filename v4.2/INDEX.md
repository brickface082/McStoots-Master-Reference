# McStoots Master Reference — Session Index
# Version 4.2 | READ THIS FIRST

McStoots Tech LLC AI build system, for any AI model or coding tool.
GitHub: https://github.com/brickface082/McStoots-Master-Reference
North star: one prompt → working build. Working beats dirt-cheap.
Docs cabinet on Chris's PC: `C:\Users\brick\McStoots-Docs\`

## HOW EACH AI GETS THE RULES

- Codex, Cursor, GitHub Copilot, Gemini CLI, Windsurf and most coding tools read `AGENTS.md` from the project root on their own.
- Claude Code reads `CLAUDE.md`, which is one line that imports `AGENTS.md`.
- Chat apps and API calls (OpenRouter, TypingMind, any model): paste `AGENTS.md` as the system prompt, then add the stack file.

One file, same rules everywhere. Edit `AGENTS.md` only.

## THIN LOAD (default)

- Always: `AGENTS.md` (rules, workflow decision, definition of done)
- Coding: add `BUILD-GENERAL.md` and one stack file
- Do not load the full inventory every session.

## FILES — LOAD WHEN

Stack files:
- `BUILD-PYTHON.md` — Python
- `BUILD-WEB.md` — web
- `BUILD-MOBILE.md` — mobile
- `BUILD-EMBEDDED.md` — embedded and hardware

On demand:
- `BUILD-GENERAL.md` — any coding session
- `AGENT-WORKFLOW-POLICY.md` — unsure solo vs plan; evidence
- `QUALITY-GATES.md` — review, debug, certify
- `POKA-YOKE-CONSTRAINTS.md` — security-sensitive work
- `checks/README.md` — safety rules enforced by a tool (`checks/run_checks.py`, `checks/ruff.toml`)
- `NEW-PROJECT-STARTUP.md` — new project
- `OPERATOR-CHECKLIST.md` — Chris writing prompts
- `TEACH.md` — teaching
- `WATCHDOG.md` — resume after a crash
- `USE-FOR-CODING.md` — optional deep coding playbook
- `USE-FOR-OPERATOR.md` — optional long operator playbook

Experimental, not the default build path:
- `SOP-ENFORCER-AGENT.md` — explicit multi-agent routing experiment
- `REQUIREMENTS-TRANSLATOR.md` — spec JSON pipeline experiment
- `SANDBOX-EXECUTOR.md` — isolated execution experiment
- `SOP-PROCESS-RULES.md` — HMI multi-agent process (S1.x)
- `QUALITY-GATES-CORE.md`, `QUALITY-GATES-TOOLS.md` — coordinate-tag HMI systems

Reference only:
- `README.md` — overview
- `CLAUDE.md` — one-line import of `AGENTS.md`
- `MASTER-BACKUP-COMPLETE-SOP.md` — archive and recovery
- `hmi_simple_test.py` — smoke stub
- `CHANGELOG-v4.1.md`, `CHANGELOG-v4.2.md` — changes and proof

## CONTINUOUS IMPROVEMENT

- v3.x — Modular SOPs, short names, workflow policy v1
- v4.0 — One-prompt default; runnable DONE WHEN + self-proof; solo vs plan_execute decision tree; thin load; multi-agent demoted (validated by OpenRouter A/B)
- v4.1 — Corrections found by running the rules. Details: `CHANGELOG-v4.1.md`
- **v4.2** — For all AI: model-neutral `AGENTS.md`; one copy of the workflow decision; safety rules enforced by a tool; no tables in the always-on and map files. Details: `CHANGELOG-v4.2.md`

Evidence: `C:\Users\brick\McStoots-Docs\findings\sop_ab_test\` (on Chris's PC — not yet in this repo)
