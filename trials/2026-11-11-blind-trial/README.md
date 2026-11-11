# Blind trial: SOP v4.0 vs v4.1 vs v4.2

**Date:** 2026-11-11
**Question:** does a newer SOP version make an AI build better than an older one?
**Answer:** not on this test. All three versions produced working, safe code. v4.2 cost more.

## Method

- 18 fresh AI agents. Each got one workspace with one SOP version, picked at random, and one build task.
- Agents were told only "the team's SOPs are in the sop folder, start with INDEX.md." They did not know it was a test or that other versions exist. Changelogs were removed from their copies.
- 2 tasks x 3 versions x 3 runs.
  - Task A (security-focused): `filebox.py` with a file-save function taking a visitor's filename, a quota validator, and a web request using an API key.
  - Task B (neutral): `report.py`, a CSV summary with a command-line total.
- The scoring script (`score.py`) was written and tested before any agent started. It runs each agent's code against hidden checks.
- Model: one small Claude model for all 18 runs.

## Results (hidden checks passed)

- v4.0: 69 of 69 (100 percent). Average 103,997 tokens and 80.8 seconds per run.
- v4.1: 67 of 69 (97.1 percent). Average 106,940 tokens and 86.1 seconds per run.
- v4.2: 69 of 69 (100 percent). Average 111,186 tokens and 94.9 seconds per run.

Every run, in every version: blocked all three path-escape attacks, rejected bad input in normal and optimized mode, used a timeout on the web request, kept the API key out of the code, passed its own tests, and passed lint.

The only two failed checks were both v4.1 runs that left the SELF-PROOF block out of the final report. With 6 runs per version, 2 misses is within noise.

## What differed

- **Tool-checked evidence:** all 6 v4.2 runs ran `checks/run_checks.py` and put its result in SELF-PROOF. No v4.0 or v4.1 run could, because the checker does not exist there.
- **Cost:** v4.2 used about 7 percent more tokens and about 17 percent more time than v4.0.
- **False alarm in the v4.2 checker:** all 3 v4.2 runs on Task A were flagged for a constant named `API_KEY_ENV_VAR` whose value was only an environment-variable name. Each agent renamed it, as `checks/README.md` instructs. That cost an extra step per run.
- **Strict four-field SELF-PROOF** (Check, Expected, Result, Evidence all labelled): v4.0 5 of 6, v4.1 3 of 6, v4.2 5 of 6.

## What this means

1. The v4.0 mistakes fixed in v4.1 (the path rule and the assert example) did not hurt this model. It wrote safe code anyway, from its own knowledge.
2. The tasks were too easy to separate the versions. Every version hit the ceiling.
3. v4.2 has not been shown to build better. It has been shown to add tool-checked proof, at a higher cost.

## Findings to act on

1. Fix the checker's false alarm on names ending in `_VAR`.
2. The Python startup sequence (git init, README, virtual environment, package folders) caused inconsistent behavior in every version. Some agents did parts of it, most skipped it and spent words explaining why. 17 of 18 reports mention it. It should apply to new projects only, not to a small job in an existing folder.
3. To separate the versions, the next trial needs harder tasks, weaker or non-Claude models, or both.

## Limits of this trial

- One model family, 3 runs per cell.
- The agent harness has its own rules (for example it blocked writing `REPORT.md` and discourages unrequested commits and docs), and those sometimes overrode the SOPs. Reports here are each agent's final message, saved afterward.
- About 100,000 tokens per run is mostly fixed harness overhead, so SOP size differences are a small part of the totals.
- Two scoring defects were found and fixed after the first scoring pass, before any conclusion was drawn: the timeout check did not know which environment-variable name each agent chose, and the SELF-PROOF check only accepted one punctuation style. Both fixes were applied the same way to all 18 runs.

## Files

- `score.py` — hidden scoring script (final version)
- `run_to_version_key.json` — which run got which SOP version
- `scores.json` — every check for every run
- `usage.json` — tokens, tool calls and seconds per run
- `reports/` — each agent's final report
