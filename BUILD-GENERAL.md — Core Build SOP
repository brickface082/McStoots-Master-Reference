# BUILD-GENERAL.md — Core Build SOP
# McStoots Tech LLC | Load for any coding session alongside CLAUDE.md

---

## EXECUTION LOOP — THE ENGINE

Run in this exact order. Never skip. Never reorder.

1. Spec-first protocol — get approval
2. Paper thinking — map input, process, output, failure modes
3. Task list — get Chris approval before execution
4. ONE task using structured prompt format
5. Build MFVP — single file, hardcoded values allowed, no polish
6. Run immediately
7. Capture results using error feedback format
8. Fix ONE issue only
9. Retest
10. Log state
11. Repeat until stable
12. Prove working — multiple tests, edge cases, failure handling
13. Expand ONLY after proof

---

## SPEC-FIRST PROTOCOL

Before any code. No exceptions.

**Step 1 — Claude asks until all answered:**
- What does this do in one sentence?
- Who uses it and how?
- What are the inputs and outputs?
- What are the hard constraints?
- What does failure look like?
- What does success look like exactly?

**Step 2 — Spec file:**
```
SYSTEM:       What this does (1-2 lines)
INPUTS:       What goes in
OUTPUTS:      What comes out
CORE FLOW:    input → process → output
STACK:        Language / framework / platform / OS / versions
CONSTRAINTS:  Hard limits
SUCCESS:      Exact binary pass/fail condition
FAILURE MODES: Where it can break
```

**Step 3 — Chris approves. No code until approved.**

---

## PAPER THINKING — REQUIRED AFTER SPEC

```
[INPUT] → [PROCESS] → [OUTPUT]
               ↓
         [FAILURE MODES]
```

Minimum: inputs, outputs, transformations, failure points, simplest path.

---

## TASK SYSTEM

```
T001 — [smallest testable first step, max 15 min]
T002 — [only after T001 passes]
T003 — [continues until proof]
```

Rules:
- Each task = 5–15 minutes maximum
- Each task independently testable
- Max 40 instructions per task — no monolithic plans
- Claude proposes, Chris approves before execution

---

## TOKEN BUDGET PER TASK

Each task gets a maximum of 3 attempts to pass its Done When condition.
If 3 attempts fail, Claude stops, runs Five Whys, surfaces the problem to Chris.
No silent continuation. No fourth guess.

---

## ERROR FEEDBACK FORMAT

```
INPUT:    What you gave it
EXPECTED: What should have happened
ACTUAL:   What actually happened
ERROR:    Exact error message
```

---

## THREE-PASS REVIEW PROTOCOL

Run before declaring any build complete.

**Pass 1 — Structural:** Does code match spec? Hallucinated features? Missing features?
**Pass 2 — Requirement:** Does it actually solve the original problem? Test against Done When.
**Pass 3 — Consistency:** Naming uniform? No contradictions between modules? Style consistent?

---

## FINAL OUTPUT REQUIREMENT

Every build session ends with all five:
1. Working code that runs
2. How to run it
3. Test cases with known inputs and expected outputs
4. Known failure points and how they are handled
5. Next improvement step

---

## CLAUDE-SPECIFIC FAILURE MODES

| Failure | Fix |
|---------|-----|
| Starting before understanding goal | Spec-first protocol mandatory |
| Task dumping — doing everything at once | Task system enforced |
| Fake tests / mock data | Gate 2 — real code only |
| Context drift across sessions | State tracking log mandatory |
| Over-engineering | MFVP first, KISS gate before every expansion |
| Environment blindness | Context packing — OS, stack, versions in every prompt |
| Self-review false confidence | Gate 5 cross-review with explicit framing |
| Infinite retry spiral | Three-strike rule — hard stop at 3 |
| Touching files not asked | Gate 1 scope check |
| Assuming instead of asking | Spec-first protocol requires questions first |

---

## FMEA — RUN BEFORE BUILDING ANYTHING THAT HANDLES DATA

Before the MFVP, list the top 3 failure modes:
1. What can go wrong? (likelihood 1–10)
2. What happens if it does? (severity 1–10)
3. How detectable before damage? (detectability 1–10)

Multiply L × S ÷ D. Design against highest numbers first.

---

## FIVE WHYS — RUN WHEN THREE-STRIKE FIRES

Ask why five times. Fix the root cause, not the symptom.

Example: Function returned wrong value → Why? No input validation → Why? Not in spec → Why? Skipped FMEA → Why? In a hurry to start coding. Root cause: skipped FMEA. Fix the process, not just the code.

---

## SIMPLICITY GATE

Before expanding: does a simpler version pass the Done When condition?
If yes, build simpler first.
Every line of code is a potential failure point.
