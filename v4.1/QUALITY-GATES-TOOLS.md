# Quality Gates — Automated Tool Checks

Programmatic checks run by the HMI platform after code is written. Distinct from
process gates in QUALITY-GATES-CORE.md (Q1.x) — these are the concrete tool
results (linter, tests, coverage) cited when a build fails an automated gate.

<rule id="Q3.0">
Every code file parses cleanly in its language (no truncated or orphaned output).
</rule>

<rule id="Q3.1">
Linter passes with zero errors (ruff for Python).
</rule>

<rule id="Q3.2">
Security scan passes with zero high-severity findings (bandit for Python).
</rule>

<rule id="Q3.3">
All unit tests pass (pytest).
</rule>

<rule id="Q3.4">
Line coverage meets the risk-tier minimum for the project (see Q1.4–Q1.7).
</rule>

<rule id="Q3.5">
Branch coverage meets the risk-tier minimum for the project (see Q1.4–Q1.7).
</rule>

<rule id="Q3.6">
Bidirectional traceability: every REQ-xxx has code (satisfies:) and a test (covers:); no orphan references.
</rule>