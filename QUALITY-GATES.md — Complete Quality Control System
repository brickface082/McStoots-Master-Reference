# QUALITY-GATES.md — Complete Quality Control System
# McStoots Tech LLC | Load when reviewing, debugging, or verifying builds

---

## THE SIX GATES — Nothing advances without clearing all six

### Gate 1 — Scope Control
- [ ] Change addresses only what was requested
- [ ] No unrelated refactors
- [ ] No unintended files modified
- [ ] No scope creep absorbed silently

### Gate 2 — Real Code
- [ ] All code is real implementation — no mocks, no simulated data
- [ ] Tests verify actual behavior, not just pass to pass
- [ ] No hardcoded fake return values
- [ ] If something is hardcoded intentionally, it is documented

### Gate 3 — Syntax and Format
- [ ] Code runs without syntax errors
- [ ] Formatting matches surrounding code
- [ ] Zero warnings from compiler or linter
- [ ] Variable and function names are clear and descriptive

### Gate 4 — Functional Validation
- [ ] Correct output for known input
- [ ] Edge cases tested
- [ ] Invalid input tested
- [ ] Empty input tested
- [ ] Failure produces clear error, not silent crash

### Gate 5 — Cross-Review (Independent Verification)
**Explicit instruction required:** "You did not write this code. Review it critically. Find problems."
- [ ] Logic errors caught
- [ ] Security issues caught
- [ ] Edge cases not already tested identified
- [ ] Performance problems flagged

### Gate 6 — Proof of Work
- [ ] Multiple test cases pass
- [ ] Edge cases pass
- [ ] Failure handling confirmed
- [ ] Chris understands WHY it works, not just that it works
- [ ] Three-pass review complete

---

## THREE-PASS REVIEW

**Pass 1 — Structural**
Does code do what it was designed to do? Does it match the spec?
Hallucinated features? Missing features? Correct architecture?

**Pass 2 — Requirement Verification**
Does code fulfill its purpose — not just run, but actually solve the problem?
Test against the Done When condition from the original prompt.

**Pass 3 — Consistency**
Are naming conventions uniform throughout?
Contradictions between modules?
Anything in one file that breaks assumptions in another?

---

## OBJECTIVE QUALITY EVIDENCE FORMAT (SUBSAFE-derived)

Every significant function needs a completed test record before build closes:

```
FUNCTION TESTED:   [function name and file]
INPUT USED:        [exact input values]
EXPECTED OUTPUT:   [exact expected result]
ACTUAL OUTPUT:     [what actually happened]
RESULT:            PASS or FAIL
DATE:              [date tested]
```

"I tested it" is not Objective Quality Evidence.
A completed record above is.

---

## WHO SURGICAL PAUSE POINTS

Full stop at these three moments. No exceptions. No time pressure overrides this.

**Pause 1 — Before coding starts:**
- [ ] Spec approved
- [ ] Environment confirmed
- [ ] Task defined with Done When condition
- [ ] State tracking log loaded (if continuing)
- [ ] Constraints identified

**Pause 2 — Before first test runs:**
- [ ] Code complete for this task
- [ ] Assertions in place
- [ ] Return values checked
- [ ] Gate 1 scope confirmed — no unintended files

**Pause 3 — Before declaring done:**
- [ ] Done When condition tested with evidence
- [ ] All five Final Output Requirements met
- [ ] Continuous Improvement Log updated

---

## MANUFACTURING QUALITY MASTER CHECKLIST

### Prevention (Poka-Yoke Level 1)
- [ ] Spec-first protocol ran and was approved before code started
- [ ] Every task had binary go/no-go Done When condition
- [ ] FMEA run on top 3 failure modes before building

### Detection (Poka-Yoke Level 2)
- [ ] Every function has input and output assertions
- [ ] Every loop has a hard upper bound
- [ ] Every return value checked
- [ ] All code passes with zero warnings
- [ ] All tests are real — no mocks

### Verification (DO-178C Independent Review)
- [ ] Gate 5 cross-review ran with explicit "you did not write this" framing
- [ ] Three-pass review complete
- [ ] Go/no-go Done When produced binary pass

### Root Cause (Five Whys)
- [ ] For every failure during build, Five Whys was run
- [ ] Root cause addressed, not just symptom
- [ ] New failure modes added to Continuous Improvement Log

### Proof
- [ ] Working code runs
- [ ] Instructions to run it documented
- [ ] Test cases with known inputs and expected outputs exist
- [ ] Known failure points documented
- [ ] Next improvement step identified

---

## ANDON CORD — PULL IMMEDIATELY

Stop everything and report to Chris when any of these fire:

- Three consecutive failures on same fix
- Known bug from previous task is unresolved and new task starting
- Test fails — build does not advance
- Blast radius is unacceptable without backup
- Context window hits 90%

**When Andon fires:**
1. State clearly what was tried
2. State what the consistent failure point is
3. Run Five Whys on the failure
4. Ask Chris how to proceed — do not guess

---

## BLAST RADIUS ASSESSMENT

Before any task touching existing data, files, or systems:

| Risk Level | Situation | Action Required |
|-----------|-----------|-----------------|
| Low | Creating new files only | Proceed |
| Medium | Modifying existing files | Save previous version |
| High | Deleting files, modifying database | Full backup required |
| Critical | Customer data, payments, auth | Stop. Think. Back up. Get second opinion. |

---

## CONTEXT WINDOW HEALTH CHECK

| Usage | Status | Action |
|-------|--------|--------|
| 0–50% | Green | Work freely |
| 50–70% | Yellow | Stay focused, avoid topic changes |
| 70–85% | Orange | Summarize completed work, compact if possible |
| 85–90% | Red | Prepare state tracking log |
| 90%+ | Critical | Stop. Save state log. Start fresh session. |
