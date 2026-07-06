# Quality Gates (Core Tagged Rules)

<rule id="Q1.1">
Every phase must pass its pre-flight checklist before starting. The Master Orchestrator cannot bypass this gate.
</rule>

<rule id="Q1.2">
Every phase output must be validated by the SOP Gate Validator (different model family from the Coding Specialist).
</rule>

<rule id="Q1.3">
GATE_FAIL must cite the specific coordinate violated.
</rule>

<rule id="Q1.4">
CRITICAL risk: 5 gates, 3 validators, ≥90% line + branch coverage.
</rule>

<rule id="Q1.5">
HIGH risk: 3 gates, 2 validators, ≥80% coverage.
</rule>

<rule id="Q1.6">
MEDIUM risk: 2 gates, 1 validator, ≥70% coverage.
</rule>

<rule id="Q1.7">
LOW risk: 1 gate, 1 validator, no coverage required.
</rule>

<rule id="Q1.8">
Jidoka full-stop: CRITICAL-severity errors (security-class) halt the self-healing loop immediately and escalate to the human — no automatic retry.
</rule>