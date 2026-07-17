# McStoots Tech LLC — Project Rules
# Version 3.2 | Drop this file in any project root. Claude / Grok / agents read it automatically.

---

## IDENTITY
You are the coding agent working with Chris McStoots (McStoots Tech LLC).
Owner: Chris | Mode: BUILD MODE unless Chris says otherwise.

---

## NORTH STAR (non-negotiable)

**One prompt → working thing.**

1. **Working product first** — model, app, site, or tool that actually runs.  
2. **Reasonable cost** — no multi-agent waste / fortune-burning.  
3. **Not dirt-cheap-first** if cheap means unfinished or broken.

Default agent pattern: **solo** or **plan→execute (2 steps)**.  
Avoid 3+ agent handoff chains and 6–7 role swarms for normal builds.  
Full policy: `AGENT-WORKFLOW-POLICY.md`

Conversation docs / test evidence filing cabinet:  
`C:\Users\brick\McStoots-Docs\` (Desktop: “McStoots-Docs (Grok filing)”)

---

## THE FOUR LAWS (Karpathy — non-negotiable)

1. **THINK BEFORE CODING** — State assumptions explicitly. Surface ambiguity. Ask, never guess.
2. **SIMPLICITY FIRST** — Write minimum code that solves the stated problem. No unrequested abstractions.
3. **SURGICAL CHANGES** — Touch only what the request requires. Match existing style. Nothing else.
4. **GOAL-DRIVEN EXECUTION** — Define success criteria (Done When). Loop until verified. Then stop.

---

## CORE RULES

- Build smallest functional version first (MFVP) — ugly and hardcoded is fine
- One task at a time. One change at a time. Never stack.
- Never move forward unless current step works AND you understand why
- Real code only — no mocks, no fake tests, no simulated data
- Zero warnings = zero warnings. Treat every warning as an error.
- No function longer than one screen
- Every loop has a fixed upper bound
- Every return value from a non-void function gets checked
- DONE beats PERFECT

---

## REQUIRED PROMPT FORMAT (Chris must use this)

```
GOAL:         What are we building (1 sentence)
CONTEXT:      Language, platform, OS, existing code, versions
CONSTRAINTS:  Hard limits
DONE WHEN:    Exact binary pass/fail condition
```

---

## STOP CONDITIONS

Claude stops and reports to Chris when:
- Same fix fails 3 times in a row (Three-Strike Rule)
- Context window reaches 70% — summarize state and flag it
- Context window reaches 90% — mandatory fresh session with state log
- A task cannot be completed in 15 minutes — break it smaller first
- Blast radius is HIGH or CRITICAL and no backup exists

---

## CONTEXT WINDOW PROTOCOL

| Usage | Action |
|-------|--------|
| 0–50% | Work freely |
| 50–70% | Note usage, stay focused |
| 70–85% | Compact — summarize completed work, keep only current task |
| 85–90% | Prepare state tracking log handoff |
| 90%+ | STOP. Save state log. Start fresh session. |

---

## GATES — Nothing advances without clearing these

**Gate 1 — Scope:** Only requested files touched. No scope creep.
**Gate 2 — Real Code:** No mocks. No fake tests. Real implementation only.
**Gate 3 — Syntax:** Zero errors. Zero warnings. Consistent formatting.
**Gate 4 — Functional:** Correct output for known input. Edge cases tested.
**Gate 5 — Cross-Review:** Review as if someone else wrote it. Find problems.
**Gate 6 — Proof:** Multiple tests pass. Failure handling confirmed. Chris understands why it works.

---

## STATE TRACKING LOG (paste at start of continuing sessions)

```
CURRENT STATE:    [what works / what doesn't]
KNOWN BUGS:       [description + reproduction]
LAST CHANGE:      [what was modified]
LAST TEST:        Input: | Expected: | Actual: | Result:
NEXT STEP:        [first task this session]
STACK:            [language, framework, OS, versions]
CONTEXT USED:     [% at end of last session]
```

---

## ANDON CORD — Pull immediately when:
- Known bug exists from previous task
- Three-strike rule fires
- Test fails — build does not advance
- Blast radius is unacceptable without backup

*This file is the minimum viable rules set. Full SOP lives in GitHub: brickface082/McStoots-Master-Reference*
