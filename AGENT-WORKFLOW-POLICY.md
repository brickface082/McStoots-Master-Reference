# Agent Workflow Policy

**Version:** 1.0 | **Cemented:** 2026-07-17  
**Evidence:** OpenRouter workflow shootout (see McStoots-Docs findings)

---

## North star

**One prompt → working thing.**

Chris’s priority order:

1. **Ship a working** model / app / site / tool (real code, real run).  
2. Keep cost **reasonable** (no fortune burned on coordination theater).  
3. **Not** “dirt cheap first” if cheap means broken or half-built.

MFVP is allowed. Fake mocks and plan-only output are not “done.”

---

## Default patterns (proven)

| Pattern | Agents | When to use | Notes |
|---------|--------|-------------|--------|
| **solo** | 1 strong model + full SOP prompt | Clear goal, ship MFVP | Best value ($/quality) in shootout |
| **plan_execute** | 2: planner → builder | Complex build, need structure first | Best quality composite in shootout |
| **gen_regen** | 1 + optional rewrite | Borderline quality needs one retry | OK secondary |
| **agentic_3+** | 3+ handoffs (translator→coder→validator…) | **Avoid as default** | Worst composite + highest cost in test |
| **6–7 role swarms** | Full HMI roster | Research/experimental only | Not the one-prompt default |

### Shootout snapshot (composite)

1. plan_execute **54.7**  
2. solo **49.3**  
3. gen_regen **44.7**  
4. spec_code **39.3**  
5. agentic_3 **24.6** ← multi-agent handoffs nerfed output  

Raw data: `C:\Users\brick\McStoots-Docs\findings\agent-workflow-shootouts\`

---

## Decision rule

```
IF task is sequential build/coding (normal McStoots work):
  USE solo OR plan_execute
  DO NOT spawn 3+ agents by default

IF true parallel independent subtasks (rare):
  MAY spawn limited specialists (cap 2–3 total)
  MUST keep one owner of the final working artifact

IF cost pressure AND task is simple:
  Prefer solo (cheapest strong path that still works)

IF quality of working artifact is at risk:
  Prefer plan_execute or one stronger model — spend a bit more
```

---

## Required output shape

Every build response should drive toward:

- GOAL / CONTEXT / CONSTRAINTS / DONE WHEN  
- Real implementation  
- Evidence it runs (command output, screenshot path, or URL)  
- Stop when DONE WHEN is true  

---

## Filing

Lasting rules live in this repo.  
Test JSON and conversation evidence live in:

`C:\Users\brick\McStoots-Docs\`
