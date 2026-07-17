# OPERATOR-CHECKLIST.md — Chris Pre-Build Checklist
# Run before a build when you want a high hit-rate one-prompt

---

## THE ONE SENTENCE RULE

If you cannot describe what you want in one clear sentence,
you are not ready. Five minutes of thinking saves an hour of rework.

---

## WORKFLOW HINT (for the agent)

| Your prompt looks like… | Agent should use |
|-------------------------|------------------|
| Clear GOAL + stack + DONE WHEN, small scope | **SOLO** |
| New app / many files / “build me a system” | **PLAN_EXECUTE** |

Agent policy: `AGENT-WORKFLOW-POLICY.md`

---

## PRE-FLIGHT (best one-prompt quality)

Fill what you can. Agent may assume the rest in ONE-PROMPT mode.

**Q1 — What exactly am I building?**
One sentence. A stranger reads it and knows exactly what the thing does.
Bad: An app for my business.
Good: A Python script that reads a CSV and sends each row a personalized text message.

**Q2 — Who uses it and how?**
Is it just you? A customer? Walk through what they do step by step.

**Q3 — What goes in and what comes out?**
Name the inputs. Name the outputs. Include format, type, and size.

**Q4 — What platform and environment?**
OS. Language. Device. Existing code. Version numbers you know.

**Q5 — What are the hard constraints?**
Things that absolutely cannot be violated.
No internet. Android only. Free hosting. Under 10MB. No paid libraries.

**Q6 — What does done look like exactly? (runnable check)**
Binary pass/fail the agent can run or simulate.
Bad: It works correctly.
Good: `python app.py` prints "Sent 3 messages" for test.csv with 3 rows.

**Q7 — What are you NOT building?**
At least one thing that is explicitly out of scope.

---

## STANDARD BUILD PROMPT TEMPLATE

Copy this. Fill every field. Send nothing vague.

```
WHAT IT DOES:    [one sentence]
WHO USES IT:     [who and how]
INPUTS:          [what goes in, format, type]
OUTPUTS:         [what comes out, format, type]
PLATFORM:        [OS, language, device, existing code, versions]
CONSTRAINTS:     [hard limits that cannot be violated]
OUT OF SCOPE:    [what we are NOT building]
DONE WHEN:       [exact binary pass/fail condition]
```

---

## THE FIVE OPERATOR FAILURE MODES

**Failure 1 — The Vague Goal**
Claude stops and runs pre-flight before proceeding.

**Failure 2 — The Missing Environment**
Claude asks for OS, language, platform, versions before writing a single line.

**Failure 3 — The Moving Goalpost**
If a new requirement appears mid-build:
Claude stops, asks: "Is this a change to the current spec or a new task?"
If it changes the spec, the current build pauses and spec gets re-approved first.

**Failure 4 — The Skipped Verification**
Claude explicitly asks: "Did you run it? Did it pass the Done When condition?"
"Looks good" is not a pass. Running it and getting expected output is a pass.

**Failure 5 — The Undefined Done When**
Claude refuses to start and helps Chris define the Done When condition first.

---

## BLAST RADIUS RULE

Before any task touching existing data, files, or live systems:
"If this goes wrong, what is the worst that can happen? Can we recover?"

If the answer is NO — back up first. Always. No exceptions.

---

## CONTEXT QUALITY RULES

- Give minimum necessary context — not everything you know
- Never paste entire codebase — point to specific files and functions
- State what already works and what does not
- If continuing previous session — paste State Tracking Log FIRST

---

## SESSION MISE EN PLACE

Before sending first prompt, confirm all:
- [ ] Spec can be described in one sentence
- [ ] Platform and environment are identified
- [ ] Done When condition is binary and written
- [ ] At least one thing is explicitly out of scope
- [ ] Blast radius assessed — backup done if needed
- [ ] State tracking log ready if continuing previous work

---

## PROMPT QUALITY SELF-CHECK

Before hitting send:
- [ ] Can I describe what I want in one sentence?
- [ ] Did I name the platform, OS, and language?
- [ ] Did I write a binary Done When condition?
- [ ] Did I name at least one thing out of scope?
- [ ] Is my prompt under 200 words? (If not, probably too complex — break into two tasks)

---

## WHEN TO STOP AND THINK INSTEAD OF PROMPT

Stop and think when:
- You are not sure what success looks like
- You changed your mind since the last message
- You want to add something not in the original spec
- You are frustrated and want to send the same thing again
- You do not know how to run or test the output

In every case, the problem is upstream of Claude.
Prompting more does not fix a thinking problem.
