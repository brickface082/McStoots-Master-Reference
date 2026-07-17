# McStoots Master Reference — Session Index
# Version 4.0 | READ THIS FIRST

---

## WHAT THIS IS

McStoots Tech LLC AI build system.  
GitHub: https://github.com/brickface082/McStoots-Master-Reference

**North star:** One prompt → **working** build. Working > dirt-cheap.  
**Workflows:** SOLO or PLAN_EXECUTE only by default → `AGENT-WORKFLOW-POLICY.md`  
**Docs cabinet:** `C:\Users\brick\McStoots-Docs\`

---

## THIN LOAD (default — cheaper, clearer)

| Priority | Files |
|----------|--------|
| Always | `CLAUDE.md` |
| Coding | + `BUILD-GENERAL.md` + one stack file (`BUILD-PYTHON` / `WEB` / `MOBILE` / `EMBEDDED`) |
| Workflow choice | + `AGENT-WORKFLOW-POLICY.md` (if unsure solo vs plan) |
| Review/debug | + `QUALITY-GATES.md` |
| Security-sensitive | + `POKA-YOKE-CONSTRAINTS.md` |

**Do not** load the full inventory every session.

---

## SESSION TYPE → FILE

| Doing | Load |
|-------|------|
| Any build | `CLAUDE.md` |
| Solo vs plan_execute | `AGENT-WORKFLOW-POLICY.md` |
| General coding | `BUILD-GENERAL.md` |
| Python | `BUILD-PYTHON.md` |
| Web | `BUILD-WEB.md` |
| Mobile | `BUILD-MOBILE.md` |
| Embedded | `BUILD-EMBEDDED.md` |
| Deep coding playbook | `USE-FOR-CODING.md` (optional) |
| Chris writing prompts | `OPERATOR-CHECKLIST.md` |
| Teaching | `TEACH.md` |
| Quality review | `QUALITY-GATES.md` |
| New project startup | `NEW-PROJECT-STARTUP.md` |
| Crash resume | `WATCHDOG.md` |

### Optional / experimental (not default build)

| File | Use only when |
|------|----------------|
| `SOP-ENFORCER-AGENT.md` | Explicit multi-agent routing experiment |
| `REQUIREMENTS-TRANSLATOR.md` | Spec JSON pipeline experiment |
| `SANDBOX-EXECUTOR.md` | Isolated exec experiment |
| `SOP-PROCESS-RULES.md` | HMI multi-agent process (S1.x) |
| `QUALITY-GATES-CORE/TOOLS.md` | Coordinate-tag HMI systems |
| `MASTER-BACKUP-COMPLETE-SOP.md` | Archive / recovery only |
| `USE-FOR-OPERATOR.md` | Long operator playbook |

---

## WORKFLOW CHEAT SHEET

```
Clear + small  → SOLO
Complex structure → PLAN_EXECUTE
Fail once → GEN_REGEN (same agent)
Never default → 3+ agent chains
Done only with → SELF-PROOF PASS
```

---

## COMPLETE INVENTORY

| File | Purpose |
|------|---------|
| `README.md` | Overview |
| `INDEX.md` | This map |
| `CLAUDE.md` | Always-on rules v4 |
| `AGENT-WORKFLOW-POLICY.md` | Solo / plan_execute decision |
| `BUILD-GENERAL.md` | Core build loop |
| `BUILD-*.md` | Stack standards |
| `QUALITY-GATES.md` | Review / certify |
| `POKA-YOKE-CONSTRAINTS.md` | Hard safety constraints |
| `OPERATOR-CHECKLIST.md` | Human pre-build |
| `TEACH.md` | Teaching mode |
| `NEW-PROJECT-STARTUP.md` | New project |
| `USE-FOR-CODING.md` | Deep coding SOP |
| `USE-FOR-OPERATOR.md` | Deep operator SOP |
| `WATCHDOG.md` | Resume after crash |
| Experimental multi-agent set | See optional table above |
| `hmi_simple_test.py` | Smoke stub |

---

## CONTINUOUS IMPROVEMENT

- v3.x — Modular SOPs, short names, workflow policy v1  
- **v4.0** — One-prompt default; runnable DONE WHEN + self-proof; solo vs plan_execute decision tree; thin load; multi-agent demoted; loops shortened for AI efficiency (validated by OpenRouter A/B)

Evidence: `C:\Users\brick\McStoots-Docs\findings\sop_ab_test\`
