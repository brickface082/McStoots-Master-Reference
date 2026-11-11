# Agent Workflow Policy

**Version:** 2.0 | **Updated:** 2026-07-17  
**Evidence:** OpenRouter workflow shootout + SOP A/B test  
`C:\Users\brick\McStoots-Docs\findings\`

---

## North star

**One prompt → working thing.** Working product > dirt-cheap. Still avoid burning a fortune.

---

## How to choose (mandatory decision tree)

Copy this logic every build session:

| # | Condition | Choose |
|---|-----------|--------|
| 1 | Single clear GOAL, known stack, ≤ few files, MFVP fits one pass | **SOLO** |
| 2 | Multi-file, unclear structure, new project skeleton, or “I need a map first” | **PLAN_EXECUTE** |
| 3 | First pass almost works but fails DONE WHEN / gates | **GEN_REGEN** (same agent, fix once) |
| 4 | True parallel independent research/vision tasks | Optional 2nd specialist only; **one owner** of final artifact |
| 5 | Default temptation to spawn translator + coder + validator + … | **STOP — use SOLO or PLAN_EXECUTE** |

### Decision in plain English

- **SOLO** = one strong model does build + self-proof. Fastest and cheapest good path.  
- **PLAN_EXECUTE** = short plan (no code) then same-or-paired execute + self-proof. Best when structure is the risk.  
- **Not default:** multi-agent handoff chains (tested worst quality + higher cost).

### Evidence snapshot

**Workflow patterns (earlier shootout):** plan_execute > solo ≫ agentic_3  
**SOP pack A/B (same model):** proposed one-prompt rules beat long baseline on plan_execute (+18 composite) and tied/slightly beat on solo, at lower cost.

---

## SOLO — rules

**When:** Clear prompt, known stack, small/medium scope.

**Must:**

1. Restate GOAL / CONTEXT / CONSTRAINTS / DONE WHEN  
2. ≤5 assumptions  
3. MFVP only  
4. Real code  
5. SELF-PROOF against DONE WHEN  
6. Stop when PASS  

**Must not:** Spawn agents; write process novels; expand before proof.

---

## PLAN_EXECUTE — rules

**When:** Complex structure, multi-file, new app skeleton, or high ambiguity of *how* not *what*.

### Plan contract (no code)

Plan MUST fit a short block and include only:

| Field | Required |
|-------|----------|
| Files to create/edit | Yes |
| MFVP boundary (what is *not* in v1) | Yes |
| Single DONE WHEN check (runnable) | Yes |
| Out of scope | Yes |
| Ordered steps (≤7) | Yes |

Plan MUST NOT include full implementation code.

### Execute contract

- Implement **only** the plan  
- MFVP first  
- SELF-PROOF  
- Stop on PASS  
- If plan is wrong: revise plan once, then execute (do not freestyle scope)

---

## GEN_REGEN — optional third path

Same agent, same SOP:

1. Keep first artifact  
2. List failures vs DONE WHEN  
3. One surgical rewrite  
4. Self-proof again  

Do **not** add a separate “validator agent” that cannot rewrite (that pattern lost tests).

---

## Multi-agent (restricted)

| Allowed | Not allowed as default |
|---------|-------------------------|
| Main + 1 specialist (research/vision) when truly parallel | Translator → coder → validator chains |
| Cap **2–3** total agents on a task | 6–7 role HMI swarms for one-prompt builds |
| One owner of final working files | Agents editing same files blindly |

Files like `SOP-ENFORCER-AGENT.md`, `REQUIREMENTS-TRANSLATOR.md`, `SOP-PROCESS-RULES.md` are **optional / experimental** — not the default build path.

---

## Definition of Done (all workflows)

```
SELF-PROOF:
  Check:     <command or call>
  Expected:  <binary outcome>
  Result:    PASS | FAIL
  Evidence:  <output summary or path>
```

No SELF-PROOF → not done.  
No runnable DONE WHEN → not done.

---

## Cost control (without sacrificing “works”)

| Do | Don’t |
|----|--------|
| Thin context: CLAUDE + stack BUILD only | Load entire SOP tree every turn |
| Prefer SOLO when clear | Always plan_execute for hello-world |
| Prefer PLAN_EXECUTE when complex | 3+ handoffs for sequential coding |
| Spend slightly more model tier if build fails | Optimize $ first and ship broken |

---

## Filing

- Rules: this repo  
- Test JSON: `C:\Users\brick\McStoots-Docs\findings\`
