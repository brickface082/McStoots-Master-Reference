# SOP Process Rules (S1.x)

> **Status: OPTIONAL / EXPERIMENTAL — HMI multi-agent pipeline only.**  
> Default builds use `CLAUDE.md` + `AGENT-WORKFLOW-POLICY.md` (SOLO / PLAN_EXECUTE).  
> Do **not** load this file for normal one-prompt builds.

Process rules for multi-agent HMI experiments. Distinct from P1.x poka-yoke and day-to-day build loop.

<rule id="S1.1">
Spec before code: a written spec (or stated assumptions + DONE WHEN) precedes implementation.
</rule>

<rule id="S1.2">
Readback: a specialist echoes its assignment before executing (multi-agent only).
</rule>

<rule id="S1.3">
Gate before phase: no SDLC phase begins until the prior phase passes its gate (multi-agent only).
</rule>

<rule id="S1.4">
Jidoka: a CRITICAL (security-class) failure full-stops to the human — never retried automatically.
</rule>

<rule id="S1.5">
Self-heal retry cap: a bug is fixed and retried at most 3 times, then escalated to the human.
</rule>

<rule id="S1.6">
Variable rigor: scrutiny scales with risk (see QUALITY-GATES.md risk scaling).
</rule>
