# checks/ — safety rules enforced by a tool

A rule an AI has to remember can be forgotten. A rule a tool checks cannot.
This folder turns six written rules into an automatic check for Python projects.

## Run it

```
pip install ruff
python checks/run_checks.py <path to your code>
```

It prints a SELF-PROOF block and exits with PASS (0) or FAIL (1).
It uses nothing specific to one operating system. Tested on Linux so far.

## What it enforces

- P1.1 — SQL must be parameterized, never built from strings
- P1.5 — no hardcoded API keys, passwords, or secrets (the linter's rules plus a McStoots check, code MCS105, for names like `API_KEY` that the linter misses)
- P1.6 — every HTTP request has a timeout
- P1.7 — no bare `except:`
- P1.8 — no wildcard imports
- Q3.0 and Q3.1 — the file parses and the linter finds no real errors
- P1.2 (partial) — flags weak hashes such as md5 and sha1

## What it cannot enforce

These still depend on the agent following the written rule in `POKA-YOKE-CONSTRAINTS.md`:

- P1.2 — that passwords are hashed with bcrypt specifically
- P1.3 — that file paths are confirmed inside the allowed folder
- P1.4 — that user input is validated against a whitelist
- P1.9 — reporting a CONSTRAINT_VIOLATION instead of working around a rule

## Known limit

The secret check goes by variable name. It can flag a harmless value whose name contains
`token`, `secret`, or `password`, such as `TOKEN_URL = "https://..."`. If that happens, rename
the variable or load the value from the environment. Do not switch the check off.

## For the agent

If you can run commands, run this check before claiming done and paste its output into SELF-PROOF.
If you cannot run commands, give Chris the command above and write `Result: NOT RUN`.
