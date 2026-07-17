# McStoots Master Reference

**McStoots Tech LLC** — SOPs, quality gates, and agent rules for AI-assisted building.

**Owner:** Chris McStoots (`brickface082`)  
**Repo:** https://github.com/brickface082/McStoots-Master-Reference  
**Version:** 3.1

---

## Start here

1. Read **[INDEX.md](INDEX.md)** every session.
2. Always load **[CLAUDE.md](CLAUDE.md)** for build work.
3. Load only the stack / mode files you need (see INDEX).

---

## What’s in this repo

| Area | Files |
|------|--------|
| Always-on rules | `CLAUDE.md` |
| Session map | `INDEX.md` |
| Core build SOP | `BUILD-GENERAL.md` |
| Stack standards | `BUILD-PYTHON.md`, `BUILD-WEB.md`, `BUILD-MOBILE.md`, `BUILD-EMBEDDED.md` |
| Operator / teaching | `OPERATOR-CHECKLIST.md`, `TEACH.md`, `NEW-PROJECT-STARTUP.md` |
| Quality | `QUALITY-GATES.md`, `QUALITY-GATES-CORE.md`, `QUALITY-GATES-TOOLS.md` |
| Full coding / operator playbooks | `USE-FOR-CODING.md`, `USE-FOR-OPERATOR.md` |
| Pipeline agents | `REQUIREMENTS-TRANSLATOR.md`, `SANDBOX-EXECUTOR.md`, `SOP-ENFORCER-AGENT.md` |
| Hard constraints | `POKA-YOKE-CONSTRAINTS.md`, `SOP-PROCESS-RULES.md` |
| Ops | `WATCHDOG.md` |
| Archive / master backup | `MASTER-BACKUP-COMPLETE-SOP.md` |
| Smoke test | `hmi_simple_test.py` |

---

## Filename convention

All SOP files use **short, stable names** (e.g. `BUILD-PYTHON.md`).  
No spaces or em-dashes in filenames so agents, scripts, and GitHub links stay reliable.

---

## How agents should use this

- **SOP Enforcer:** see `SOP-ENFORCER-AGENT.md` — maps task type → SOP files.
- **Coordinate tags:** `P1.x` (poka-yoke), `Q1.x` / `Q2.x` / `Q3.x` (quality), `S1.x` (process).
- Prefer loading `INDEX.md` + `CLAUDE.md` first; do not dump the whole repo into context.

---

## Local path (OpenClaw workspace)

If you run OpenClaw on this machine, a checkout may also live at:

`C:\Users\brick\.openclaw\workspace\McStoots-Master-Reference`

Treat **this GitHub repo** as the source of truth. Pull before long sessions.
