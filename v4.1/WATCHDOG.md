# Watchdog Protocol (Agent Crash / Resume)

Use this when an OpenClaw agent (e.g. Az) shuts down, crashes, or goes silent mid-task.

## Recovery loop

1. OpenClaw gateway auto-restarts the main session
2. On boot, the agent reads `RESUME.md` in the workspace root
3. If `RESUME.md` exists and contains an incomplete task, continue from the last completed step
4. Delete `RESUME.md` only when the full task is marked `COMPLETE`

## RESUME.md minimum template

```markdown
# RESUME
STATUS: INCOMPLETE
GOAL: [one sentence]
LAST COMPLETED STEP: [step N]
NEXT STEP: [step N+1]
STACK: [language / OS / versions]
KNOWN BLOCKERS: [none | list]
```

## Technical notes

- OpenClaw Gateway supports `gateway restart` with optional `continuationMessage` for post-restart delivery
- Sessions auto-reconnect after Gateway restart
- `boot-md` hook fires on session bootstrap
- `gateway:startup` hook fires after channels start and hooks are loaded

## Related SOPs

- Always-on rules: `CLAUDE.md` (context window / three-strike stop conditions)
- Process rules: `SOP-PROCESS-RULES.md` (`S1.5` self-heal retry cap)
