# QUALITY-GATES.md — Quality Control
# Load for review, debug, or when a build must be certified

---

## WHEN TO LOAD

| Situation | Load this? |
|-----------|------------|
| Normal SOLO / PLAN_EXECUTE build | Optional — use CLAUDE.md 6-gate summary |
| Debug / review / “is this done?” | **Yes** |
| Security-sensitive (auth, payments, PII) | **Yes** + `POKA-YOKE-CONSTRAINTS.md` |

---

## SIX GATES (all must clear to certify done)

### Gate 1 — Scope
- [ ] Only requested work  
- [ ] No unrelated refactors  
- [ ] No silent scope creep  

### Gate 2 — Real Code
- [ ] Real implementation (no mocks / fake returns / TODO implement)  
- [ ] Intentional hardcodes documented  

### Gate 3 — Syntax / Format
- [ ] Runs without syntax errors  
- [ ] Matches project style  
- [ ] Zero avoidable warnings  

### Gate 4 — Functional
- [ ] DONE WHEN runnable check passes  
- [ ] Basic edge / invalid input considered  
- [ ] Failures error clearly  

### Gate 5 — Self cross-review
Frame: **“I did not write this. Find problems.”**  
- [ ] Logic issues  
- [ ] Security issues  
- [ ] Missed edge cases  

### Gate 6 — Proof of Work
- [ ] SELF-PROOF block complete  
- [ ] Evidence present (command output / path / URL)  
- [ ] Result PASS  

**Gate 6 is not optional.** No proof → not done.

---

## OBJECTIVE EVIDENCE (preferred form)

```
FUNCTION / FEATURE:
CHECK RUN:
INPUT:
EXPECTED:
ACTUAL:
RESULT: PASS | FAIL
```

“I tested it” without the block = invalid.

---

## THREE-PASS REVIEW (before big merge / release)

1. **Structural** — matches goal? missing/hallucinated features?  
2. **Requirement** — DONE WHEN truly satisfied?  
3. **Consistency** — naming, module assumptions, style  

---

## PAUSE POINTS

| When | Check |
|------|--------|
| Before coding | DONE WHEN runnable; stack known; assumptions listed |
| Before claiming done | SELF-PROOF PASS; gates 1–6 |
| Before expanding | MFVP already proven |

---

## RISK SCALING (keep cheap when low risk)

| Risk | Proof bar |
|------|-----------|
| LOW (UI copy, tiny script) | SELF-PROOF once |
| MEDIUM | SELF-PROOF + Gate 5 |
| HIGH / CRITICAL (auth, money, delete data) | Full gates + backup + poka-yoke |

Do not run enterprise ceremony on hello-world.
