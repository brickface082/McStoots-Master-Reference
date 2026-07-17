# BUILD-GENERAL.md — Core Build SOP
# Load with CLAUDE.md for any coding session

---

## MODE

**Default: ONE-PROMPT BUILD**

- Infer missing details; list assumptions (≤5).  
- Do **not** wait for multi-step human approval to start MFVP.  
- Ask Chris only if: missing secrets, destructive/irreversible external action, or illegal/impossible goal.

**Collab mode** (only if Chris says so): ask before each phase.

---

## CHOOSE WORKFLOW

See `AGENT-WORKFLOW-POLICY.md` and `CLAUDE.md`.

| Situation | Workflow |
|-----------|----------|
| Clear + small/medium | **SOLO** |
| Multi-file / structure risk | **PLAN_EXECUTE** |
| Almost works | **GEN_REGEN** (same agent) |

---

## EXECUTION LOOP (short)

```
1. Capture GOAL / CONTEXT / CONSTRAINTS / DONE WHEN (runnable)
2. Pick SOLO or PLAN_EXECUTE
3. [If PLAN] short plan only — files, MFVP boundary, DONE WHEN, out-of-scope
4. Build MFVP (real code)
5. SELF-PROOF (run the check)
6. Fix ONE issue if FAIL (max 3 attempts → Andon)
7. STOP when PASS — expand only after proof
```

Do not reorder. Do not skip 5–7.

---

## SPEC (lightweight, one-prompt)

If Chris did not give full GOAL block, invent the minimum and label assumptions:

```
SYSTEM:        one sentence
INPUTS / OUTPUTS:
STACK:
CONSTRAINTS:
DONE WHEN:     runnable check
OUT OF SCOPE:
```

Full multi-question interview is **optional** (collab mode), not required for every build.

---

## PAPER THINKING (keep tiny)

One line: `INPUT → PROCESS → OUTPUT` + top 1–3 failure modes.  
Skip long essays.

---

## TASKS

- Prefer **one** MFVP task that hits DONE WHEN.  
- Split only if blocked after a failed attempt.  
- Max 3 attempts per DONE WHEN → Andon + Five Whys.

---

## ERROR FEEDBACK

```
INPUT:
EXPECTED:
ACTUAL:
ERROR:
```

---

## SELF-PROOF (required before done)

```
Check:
Expected:
Result: PASS | FAIL
Evidence:
```

---

## FINAL OUTPUT (session end)

1. Working code  
2. How to run  
3. SELF-PROOF  
4. Known limits  
5. Next optional improvement (do not implement yet)

---

## FAILURE MODES (watch for)

| Failure | Fix |
|---------|-----|
| Start without DONE WHEN | Write runnable check first |
| Task dump / overbuild | MFVP only |
| Mocks / fake tests | Real code gate |
| Infinite retries | Three-strike |
| Scope creep | Surgical rule |
| Multi-agent by habit | SOLO / PLAN_EXECUTE only |
| Approval stall on clear goals | One-prompt mode — proceed |

---

## FMEA (data/auth/payments only)

Before MFVP on sensitive data: top 3 failure modes (likelihood × severity). Design against worst first.

---

## SIMPLICITY GATE

If a simpler design still passes DONE WHEN → build that first.
