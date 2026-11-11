
Let me get the content into GitHub the same way we did it before. Here is the full text — long press, select all, copy, then go to GitHub, create a new file named exactly:

---

# USE FOR OPERATOR — Chris Pre-Build Checklist and Prompt SOP
### McStoots Tech LLC — Master Reference
**Version 1.0 — Continuous Improvement Document**

---

## PURPOSE

This SOP enforces quality on the human side of the build. Claude enforces this on Chris before any build starts. If these questions are not answered Claude does not proceed. The operator is a failure point in the system. This document closes that gap.

---

## THE ONE SENTENCE RULE

If you cannot describe what you want to build in one clear sentence you are not ready to build it yet. Spend five minutes thinking before opening Claude. Five minutes of thinking saves an hour of rework. This is the single most important rule in this document.

---

## OPERATOR PRE-FLIGHT CHECKLIST

Answer every question before sending the first build prompt. If you cannot answer a question the build is not ready to start. Claude will ask these before proceeding. There are no shortcuts.

**Question 1 — What exactly am I building?**
Write one sentence. Not a paragraph. One sentence a stranger could read and know exactly what the thing does.
Bad: I want an app for my business.
Good: A Python script that reads a CSV file of customer names and emails and sends each one a personalized text message.

**Question 2 — Who uses it and how?**
Is it just you? A customer? What do they do with it step by step from the moment they open it?

**Question 3 — What goes in and what comes out?**
Name the inputs. Name the outputs. Be specific about format, size, and type.
Bad: It takes some data and shows results.
Good: Input is a CSV file with columns name and email. Output is a confirmation message showing how many messages were sent.

**Question 4 — What platform and environment?**
What OS. What language if you know it. What device it runs on. What already exists in the project if anything. What version numbers you know.

**Question 5 — What are the hard constraints?**
Things that absolutely cannot be violated. No internet required. Must run on Android. Must cost nothing to host. Under 10 megabytes. Free libraries only. Whatever they are, name them now.

**Question 6 — What does done look like exactly?**
Write the binary pass fail condition. Not it works or looks good. Write the exact output or behavior that proves it works. If you cannot write this you are not ready to start.
Bad: It works correctly.
Good: Script runs, reads test.csv with 3 rows, prints Sent 3 messages, and shows each name and email in the console. Any other output is a fail.

**Question 7 — What are you NOT building?**
Name at least one thing that is out of scope. Scope creep kills builds. Defining what you are not building is as important as defining what you are.

---

## STANDARD BUILD PROMPT TEMPLATE

Copy this every time. Fill every field. Send nothing vague. If a field is truly not applicable write N/A — do not leave it blank.

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

These are the five ways Chris is most likely to become the failure point. Claude watches for all five and stops the build when any of them appear.

**Failure Mode 1 — The Vague Goal**
Prompt says something like make me an app for managing my inventory. No specifics about what it does, what goes in, what comes out, or what done looks like.
Claude stops and runs the pre-flight checklist before proceeding. Build does not start until Question 1 is answered with one clear sentence.

**Failure Mode 2 — The Missing Environment**
Prompt describes what to build but says nothing about where it runs. No OS, no language, no platform, no versions.
Claude asks for all environment details before writing a single line. This is not optional. A script that works on Windows may fail on Android. Environment is not a detail, it is the foundation.

**Failure Mode 3 — The Moving Goalpost**
Build is underway and a new requirement appears mid-session. Actually can you also add... or wait I also need it to...
Claude stops, acknowledges the new requirement, and asks: is this a change to the current spec or a separate task for later? If it changes the spec, the current build pauses, the spec gets updated, and Chris approves the new spec before work continues. New requirements do not get silently absorbed into an active build.

**Failure Mode 4 — The Skipped Verification**
Claude delivers something and Chris says looks good or sounds right without actually running it and testing it.
Claude explicitly asks: did you run it and did it pass the Done When condition? The build does not advance until the answer is yes with actual evidence. Looks good is not evidence. Ran it and got the expected output is evidence.

**Failure Mode 5 — The Undefined Done When**
Chris cannot write a binary pass fail condition because success has not been defined clearly enough.
Claude refuses to start the build and helps Chris define the Done When condition first. This is the most important gate. A build without a clear done condition never ends. It just drifts until everyone gives up.

---

## BLAST RADIUS RULE

Before any task that touches existing data, files, databases, or live systems, Chris answers one question:

If this goes wrong what is the worst that can happen and can we recover from it?

If the answer is no we cannot recover — back up first. Always. No exceptions. An AI coding agent deleted 2.5 years of customer data in minutes because nobody thought about blast radius before running the task. That story is real and it is preventable. The backup takes five minutes. The recovery takes weeks.

Categories by blast radius from lowest to highest:

Low — creating new files that did not exist before. Nothing existing can be broken.
Medium — modifying existing files. Previous version should be saved before changes.
High — deleting files, modifying databases, changing live systems. Full backup required before proceeding.
Critical — anything touching customer data, payment systems, or authentication. Stop. Think. Back up. Get a second opinion before proceeding.

---

## CONTEXT QUALITY RULES

More context is not better. Better context is better. Bad context does not just produce mediocre output. It can poison the whole session and make every subsequent response worse.

Rule 1 — Give the minimum necessary context. Not everything you know about the project. Only what is directly relevant to this specific task.

Rule 2 — Never paste an entire codebase into the prompt. Point to the specific files and functions relevant to this task only.

Rule 3 — State what already works and what does not. Do not make Claude rediscover known state. Claude has no memory of previous sessions unless you provide the state tracking log.

Rule 4 — If picking up from a previous session, paste the State Tracking Log first before anything else. This is the handoff document between sessions. Without it Claude starts from scratch.

Rule 5 — Name the specific file being changed, not the whole project. Wrong: the authentication system needs to be fixed. Right: the login function in src/auth/login.py is returning None instead of the user object when the password is correct.

---

## WHEN TO STOP AND THINK INSTEAD OF PROMPT

Stop and think before prompting when any of these are true. Prompting more does not fix a thinking problem.

You are not sure what success looks like. You changed your mind about what you want since the last message. You want to add something that was not in the original spec. You are frustrated because Claude is not doing what you expected. You do not know how to run or test the output. You have sent the same request three times and gotten different wrong results each time.

In every one of these cases the problem is upstream of Claude. The fix is to stop, go back to the pre-flight checklist, and redefine the goal before sending another message.

---

## PROMPT QUALITY SELF-CHECK

Before hitting send, run this check. If any answer is no, fix it before sending.

Can I describe what I want in one sentence? Yes or No.
Did I name the platform, OS, and language? Yes or No.
Did I write a binary Done When condition? Yes or No.
Did I name at least one thing that is out of scope? Yes or No.
Did I include the state tracking log if this continues a previous session? Yes or No.
Is my prompt under 200 words? Yes or No. If not, it is probably too complex for one task — break it into two.

---

## THE JUNIOR DEVELOPER ANALOGY

Treat Claude like a brilliant junior developer with zero tribal knowledge and daily amnesia. This developer knows every programming pattern ever written. They have read every textbook. They are fast, eager, and confident.

But they do not know your project. They do not know what you tried last week. They do not know what your business does or who your customers are. They do not know that the payments module is fragile and should not be touched. They do not know that you changed your mind about the database schema on Tuesday.

You have to tell them all of that every single session. That is not a flaw in the junior developer. That is the job of the person directing them. That person is you.

Your job is not to write code. Your job is to give Claude exactly what it needs to write the right code. That is a skill. This document is how you build that skill.

---

## CONTINUOUS IMPROVEMENT LOG

Version 1.0 — Initial build. Pre-flight checklist, standard prompt template, five operator failure modes, blast radius rule, context quality rules, prompt self-check, junior developer framing.

---

*This is a living document. Evaluate adapt improve.*

---
