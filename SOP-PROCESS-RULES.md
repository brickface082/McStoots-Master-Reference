# SOP Process Rules (Standard Operating Procedure Coordinates)

Process rules enforced by the HMI multi-agent pipeline. These govern *how* work
flows — distinct from Poka-Yoke hard constraints (P1.x) and quality gates (Q1.x).

<rule id="S1.1">
Spec before code: a written, approved spec precedes any implementation.
</rule>

<rule id="S1.2">
Readback: a specialist echoes its assignment before executing.
</rule>

<rule id="S1.3">
Gate before phase: no SDLC phase begins until the prior phase passes its gate.
</rule>

<rule id="S1.4">
Jidoka: a CRITICAL (security-class) failure full-stops to the human — never retried automatically.
</rule>

<rule id="S1.5">
Self-heal retry cap: a bug is fixed and retried at most 3 times, then escalated to the human.
</rule>

<rule id="S1.6">
Variable rigor: scrutiny (gates, validators, coverage) scales with each requirement's risk level (Q1.4–Q1.7).
</rule>