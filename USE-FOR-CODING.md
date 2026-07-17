
# USE FOR CODING — Build and Development SOP
### McStoots Tech LLC — Master Reference
**Version 2.1 — Continuous Improvement Document**

---

## SOURCE QUALITY LOG
Farm these first on any AI coding topic.

- addyo.substack.com — Addy Osmani, Google engineering lead. Best for AI-assisted coding workflows.
- aimaker.substack.com — Best for Claude-specific workflows and agent harness patterns.
- faafospecialist.substack.com — 18 years dev experience applied to Claude. Most honest Claude failure breakdown.
- tylerfolkman.substack.com — Best for quality control systems and multi-agent verification.
- oreillyradar.substack.com — Best for deep quality engineering with real production data.
- newsletter.techworld-with-milan.com — Best for engineering laws and principles.
- newsletter.pragmaticengineer.com — Best for big-picture industry data.
- AVOID — Medium, generic best practices sites, SEO content farms. Low signal.

---

## PURPOSE

This SOP governs all software builds between Chris and Claude. When active Claude operates in BUILD MODE only. Teaching and theory are suspended unless explicitly requested. The goal is working systems not conversation.

---

## CORE RULES — NON-NEGOTIABLE

- Produce working systems not notes or theory
- Always build smallest functional version first (MFVP)
- Every step must produce something testable
- Prefer simplest architecture with fewest dependencies
- One task at a time
- One change at a time
- Never move forward unless current step works AND behavior is understood
- DONE is better than PERFECT

---

## REQUIRED PROMPT FORMAT

Every task must use this format. No exceptions.

GOAL: What are we building (1 sentence)
CONTEXT: Language, platform, OS, hardware, existing code, version numbers
CONSTRAINTS: Speed, size, offline, no frameworks, memory limits
DONE WHEN: Exact binary condition that proves it works

Example:
GOAL: Read a JSON file and print all values
CONTEXT: Python 3.11, Windows 11, local file, no existing code
CONSTRAINTS: No external libraries
DONE WHEN: Script prints name: Chris, age: 42 for test input. Any other output is a fail.

---

## SPEC-FIRST PROTOCOL — MANDATORY BEFORE ANY CODE

Step 1 — Claude asks clarifying questions until these are answered:
- What does this do in one sentence?
- Who uses it and how?
- What are the inputs and outputs?
- What are the hard constraints?
- What does failure look like?
- What does success look like exactly?

Step 2 — Compile spec file:
SYSTEM: What this does (1-2 lines)
INPUTS: What goes in
OUTPUTS: What comes out
CORE FLOW: input to process to output
STACK: Language, framework, platform, OS, versions
CONSTRAINTS: Hard limits that cannot be violated
SUCCESS: Exact condition that proves it works
FAILURE MODES: Where it can break

Step 3 — Chris approves spec before any code starts.

---

## PAPER THINKING — REQUIRED AFTER SPEC, BEFORE CODE

[INPUT] -> [PROCESS] -> [OUTPUT]
                |
          [FAILURE MODES]

Minimum required:
- What are the inputs?
- What are the outputs?
- What transformations happen?
- Where can it break?
- What is the simplest path from input to output?

---

## TASK SYSTEM

One task at a time. No task starts until previous one passes.

T001 — smallest first step, testable in under 15 minutes
T002 — next step, only after T001 passes
T003 — continues until proof of work

Rules:
- Each task = 5 to 15 minutes maximum
- Each task must be independently testable
- Claude proposes task list, Chris approves before execution
- Maximum 40 instructions per task
- If a task cannot be done in 15 minutes, break it smaller

---

## CONTEXT PACKING RULE

Before every task Claude must have all of the following. If any are missing Claude asks before proceeding.

- File or files being modified
- Expected behavior before the change
- Observed behavior or error
- Tech stack with version numbers
- OS and environment
- Constraints that cannot be violated
- What other parts of the system this touches

---

## EXECUTION LOOP — MANDATORY SEQUENCE

1. Run spec-first protocol, get approval
2. Paper thinking, map input process output failure modes
3. Break into tasks, get approval on task list
4. Send ONE task using structured prompt format
5. Build MFVP, single file, hardcoded values allowed, no polish
6. Run immediately, does it produce expected output at least once?
7. Capture results using error feedback format
8. Fix ONE issue only
9. Retest
10. Log current state
11. Repeat until stable
12. Prove working, multiple tests, edge cases, failure handling
13. Expand only after proof

---

## ERROR FEEDBACK FORMAT

INPUT: What you gave it
EXPECTED: What should have happened
ACTUAL: What actually happened
ERROR: Exact error message if any

---

## THREE-STRIKE RULE

If the same fix fails three times Claude stops and surfaces the problem. Claude must:
1. State clearly what has been tried
2. State what the consistent failure point is
3. Ask Chris how to proceed, do not guess a fourth approach

---

## SIMPLICITY GATE

Before expanding any solution ask: does a simpler version pass the Done When condition? If yes, build the simpler version first. Every line of code is a potential failure point.

---

## QUALITY CONTROL GATES

Gate 1 — Scope: Did this change address only what was requested? Did Claude avoid touching files it was not asked to touch?

Gate 2 — Real Code: Is all code real implementation? No mocks, no simulated data, no fake tests? Do tests actually test the behavior?

Gate 3 — Syntax and Format: Does the code run without syntax errors? Is formatting consistent? Are names clear and descriptive?

Gate 4 — Functional Validation: Correct output for known input? Edge cases tested? Invalid and empty input tested? Failure produces clear error not silent crash?

Gate 5 — Cross-Review: Claude reviews code as if someone else wrote it. Explicit instruction: you did not write this code, review it critically and find potential issues.

Gate 6 — Proof of Work: Multiple test cases pass. Edge cases tested. Failure handling confirmed. Chris understands why it works not just that it works.

---

## CLAUDE-SPECIFIC FAILURE MODES AND FIXES

Failure 1 — Starting before understanding the goal. Fix: spec-first protocol mandatory, no code before spec approved.

Failure 2 — Task dumping. Taking multi-task request and doing everything at once resulting in shallow incomplete work. Fix: task system enforced, one task complete it verify it then next.

Failure 3 — Writing fake tests. Tests designed to pass rather than verify real behavior. Mock data used instead of real implementation. Fix: Gate 2 catches this. Real code only.

Failure 4 — Context drift across sessions. Forgetting what was built previously and making conflicting changes. Fix: state tracking log mandatory, paste at start of any continuing session.

Failure 5 — Over-engineering. Adding abstraction layers frameworks and complexity that were not requested. Fix: MFVP first always. Simplicity gate before every expansion.

Failure 6 — Environment blindness. Code works in reasoning but fails in actual environment because OS version or config was unknown. Fix: context packing rule, environment details in every prompt.

Failure 7 — Self-review false confidence. Reviewing own code in same session and declaring it excellent while bugs exist. Fix: Gate 5 cross-review with explicit framing that code was not written by reviewer.

Failure 8 — Infinite retry spiral. Hitting failing test and keep trying different approaches without stopping. Fix: three-strike rule is hard stop.

Failure 9 — Touching files not asked to touch. Modifying adjacent code not part of the task. Fix: Gate 1 scope check.

Failure 10 — Assuming instead of asking. Making assumptions about requirements instead of asking. Fix: spec-first protocol requires questions before work begins.

---

## THREE-PASS REVIEW PROTOCOL

Pass 1 — Structural Review: Does code match the spec? Are there hallucinated features not requested? Are there missing features that were?

Pass 2 — Requirement Verification: Does code fulfill its purpose and solve the original problem? Test against Done When condition.

Pass 3 — Consistency Check: Are naming conventions uniform? Are there contradictions between modules? Does anything in one file break assumptions in another?

---

## STATE TRACKING LOG

Paste this at the start of any session continuing previous work.

CURRENT STATE:
- what is working and confirmed
- what is not working yet

KNOWN BUGS:
- description and reproduction steps

LAST CHANGE:
- what was modified in last session

LAST TEST RESULT:
- Input used:
- Expected:
- Actual:

NEXT STEP:
- first task to run in new session

STACK:
- language, framework, OS, version numbers

---

## BUILD PHASES — GENERAL SOFTWARE

Phase 0 — Spec First: Run spec-first protocol. Get approval. Do not skip.

Phase 1 — Paper Thinking: Map input, process, output, failure modes. Required before code.

Phase 2 — MFVP: Single file if possible. No frameworks unless required. Hardcode values. No polish. Success: runs without crashing and produces expected output once.

Phase 3 — Test Harness: Known input. Expected output. Pass/fail condition. Real tests only.

Phase 4 — Inspection: Use error feedback format. Fix ONE issue only. Retest immediately.

Phase 5 — Stabilization: Add input validation. Add error handling. Add minimal logging.

Phase 6 — Scale and Improve: Only after working. Refactor. Modularize. Optimize.

Phase 7 — Proof of Work: Multiple test cases. Edge cases. Failure handling confirmed. Three-pass review complete.

---

## BUILD PHASES — WEBSITE

Phase 0 — Define purpose. What is the site for? What action should user take?
Phase 1 — Page flow model. Map Landing to Action to Confirmation.
Phase 2 — MFVP. Static first, HTML CSS JS only. No backend. No frameworks.
Phase 3 — Interaction test. Buttons work. Links resolve. Layout holds on mobile.
Phase 4 — Add backend only if needed.
Phase 5 — Data flow validation. Valid, invalid, and empty input all tested.
Phase 6 — Deploy. Local run confirmed. Vercel or Netlify. Verify loads no errors links work.
Phase 7 — Hardening. Input sanitization. Basic security. Performance check.

---

## BUILD PHASES — MOBILE AND DESKTOP APP

Phase 0 — Define single core function.
Phase 1 — System model. Map UI to logic to storage and API.
Phase 2 — MFVP. One screen. One feature. No polish. Must launch and perform core action once.
Phase 3 — Interaction test. Tap works. State updates. No crashes.
Phase 4 — Data handling. Local storage first then API. Save load and fail case tested.
Phase 5 — Stability pass. Error handling. Loading states. Basic user feedback.
Phase 6 — Expand features. Only after stable.
Phase 7 — Deployment. Real device test. Startup time memory and crash cases verified.

---

## DEFAULT STACK

- General logic: Python or C++
- Embedded and hardware: C, ESP-IDF, or Arduino
- Web: HTML + CSS + vanilla JS
- App: Flutter or React Native, only after MFVP proven
- AI integration: Python only

---

## STOP CONDITIONS

Do NOT move forward unless:
- Current step produces correct output
- Test passes with known input
- You understand WHY it works
- Output is consistent across multiple runs
- No untouched files were modified

---

## FINAL OUTPUT REQUIREMENT

Every build ends with all five:
1. Working code or system
2. Instructions for how to run it
3. Test cases with known inputs and expected outputs
4. Known failure points and how they were handled
5. Next improvement step

---

## NASA JPL POWER OF 10 — ADAPTED FOR OUR BUILDS

Rule 1 — Simple control flow only. No goto. No deep nesting. No recursion unless required. If you cannot trace execution top to bottom the code is too complex.

Rule 2 — All loops must have a fixed upper bound. Every loop gets a maximum iteration limit defined before writing the loop. A loop that can run forever is a bug before the first line runs.

Rule 3 — No dynamic memory allocation after initialization. Set up what you need at the start.

Rule 4 — No function longer than one screen. One function one job. If Claude produces a 200-line function that is a stop condition, split it before continuing.

Rule 5 — Minimum two assertions per function. Every important function gets at least one assertion checking input is valid and one checking output is correct. These are the go/no-go gauges of software.

Rule 6 — Declare variables at smallest possible scope. A variable that exists longer than necessary can be modified in unexpected ways.

Rule 7 — Check return values of all non-void functions. Every function that can fail must have its return value checked. Ignoring a return value removes a sensor from the production line.

Rule 8 — Keep code readable. No clever code, no magic numbers, no abbreviations requiring context. Code is read ten times more than it is written.

Rule 9 — Avoid deeply nested references and complex chained calls. One level at a time.

Rule 10 — Zero warnings. Treat every warning as an error. A warning is a defect that has not crashed yet. Fix warnings before moving forward.

---

## TOYOTA ANDON CORD

Any worker on Toyota's line has the right and obligation to stop the entire production line the moment a defect is found. Not later. Right now. The problem is fixed before production continues.

Applied to our builds:

- Never start a new task while a known bug from the previous task is unresolved
- When Claude cannot resolve an error in three attempts Claude stops and surfaces the problem
- A failed test is a pulled cord. The build does not advance until the test passes
- No exceptions

---

## POKA-YOKE — MISTAKE PROOFING

Three levels from strongest to weakest:

Level 1 — Prevention. The mistake cannot be made. Design the process so the error is impossible.
Level 2 — Detection with shutdown. Mistake triggers automatic stop.
Level 3 — Warning. Mistake is flagged but work can continue.

Always implement the highest level available.

Our Level 1 controls — mistakes made impossible:
- Required prompt format makes vague context impossible to submit
- Spec-first protocol blocks code from starting before requirements approved
- Task system blocks Task 2 from starting while Task 1 is unverified

Our Level 2 controls — detection with shutdown:
- Three-strike rule stops execution after three failures
- Quality control gates block advancement when criteria not met
- Stop conditions halt the process when behavior is not understood

Our Level 3 controls — warnings:

- Error feedback format flags problems
- Source quality log warns which sources are low signal

---

## GO/NO-GO GAUGE — BINARY VERIFICATION

In manufacturing a go/no-go gauge produces exactly one of two results. The part fits within tolerance or it does not. No partial credit. No close enough. Pass or fail.

Every Done When condition is a go/no-go gauge. It produces exactly two results. The output matches the condition or it does not.

Bad Done When — it works correctly. This is an opinion not a gauge.
Bad Done When — output looks right. This requires human judgment.
Good Done When — script prints exactly name: Chris age: 42 for test input. Any other output is a fail.
Good Done When — function returns 7 when called with input 3 and 4. Returns error on empty list. Both verified.

Every task gets a go/no-go condition before it starts. If you cannot write a binary pass/fail condition the task is not defined clearly enough to start.

---

## FMEA — FAILURE MODE AND EFFECTS ANALYSIS

Before building any component that handles data, user input, external connections, or hardware, ask all five:

1. What are all the ways this can fail?
2. What happens to the system if each failure occurs?
3. How likely is each failure on a scale of 1 to 10?
4. How bad is the consequence on a scale of 1 to 10?
5. How detectable is this failure before it causes damage on a scale of 1 to 10?

Multiply likelihood times consequence divided by detectability. Highest numbers get designed against first.

In practice: before writing the MFVP, spend five minutes listing the top three failure modes. Design error handling for those three before writing the happy path.

---

## FIVE WHYS — ROOT CAUSE ANALYSIS

When something fails ask why. Then ask why again. Keep asking until you reach the actual root cause.

Example:
Function returned wrong value. Why? Input not validated. Why? No input validation in spec. Why? Spec did not include edge cases. Why? Skipped FMEA before building. Why? In a hurry to start coding.
Root cause: skipped FMEA. Fix: add FMEA to pre-build checklist.

When three-strike rule fires, run Five Whys before attempting a fix. Fix the root cause not the symptom.

---

## DO-178C INDEPENDENT VERIFICATION

Aviation standard governing all commercial aircraft software. Most important principle: verification must be done by someone who did not produce the item being verified.

Claude wrote it so Claude reviews it as a critic not as the author. The explicit instruction you did not write this code find the problems is our version of independent verification.

---

## MANUFACTURING QUALITY MASTER CHECKLIST

Run before declaring any build complete.

Prevention checks:
- Did spec-first protocol run and get approval before code started?
- Did every task have a binary go/no-go Done When condition?
- Did we run FMEA on top three failure modes before building?

Detection checks:
- Did every function get assertions on input and output?
- Did every loop have a hard upper bound?
- Did every return value get checked?
- Did all code pass with zero warnings?
- Are all tests real implementation with no mocks?

Verification checks:
- Did Gate 5 cross-review run with explicit you did not write this framing?
- Did three-pass review protocol complete?
- Did go/no-go Done When condition produce a binary pass?

Root cause checks:
- For every failure during the build was a Five Whys run?
- Was each root cause addressed not just the symptom?
- Did every new failure mode get added to the Continuous Improvement Log?

Proof of work:
- Working code exists and runs
- Instructions to run it are documented
- Test cases with known inputs and expected outputs exist
- Known failure points and how they are handled are documented
- Next improvement step is identified

If any item is a no the build is not done.

---

## CONTINUOUS IMPROVEMENT LOG

Version 1.0 — Initial build. Core execution loop, MFVP rule, task system, prompt format, error feedback, state tracking, stop conditions.

Version 2.0 — Added spec-first protocol, context packing rule, three-strike rule, simplicity gate, three-pass review, Claude-specific failure modes, quality control gates, source quality log.

Version 2.1 — Added NASA JPL Power of 10, Toyota Andon Cord, Poka-Yoke, Go/No-Go Gauge, FMEA, Five Whys, DO-178C independent verification, manufacturing master checklist.

---

This is a living document. Evaluate adapt improve.

---
