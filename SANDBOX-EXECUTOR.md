> **OPTIONAL / EXPERIMENTAL** — not default one-prompt path.

# Sandbox Executor + Self-Healing Loop

**Purpose:** Execute generated code in isolation, parse errors, and route surgical fixes back to the Coding Specialist.

## Core Components
- Sandbox Executor: Isolated environment (Python subprocess or Docker).
- Error Parser: Convert stack traces to structured JSON (language, file, line, error_type, message, severity).
- Re-Entry Router: Send targeted fix instructions (not full rebuilds).
- Max Retries: 3 (enforced by SOP gate).
- Jidoka: CRITICAL severity triggers full stop and human alert.

## Implementation Skeleton (Python)
```python
import subprocess
import json

def execute_code(code, language='python'):
    # Isolated execution logic
    pass

def parse_error(stderr):
    # Return structured error dict
    pass

def re_entry_router(error, code):
    # Return targeted fix instruction
    pass
```

Coordinate References:
- Error handling: P1.7, Q1.3
- Jidoka: Q1.8