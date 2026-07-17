# BUILD-PYTHON.md — Python Build Standards
# Load with CLAUDE.md + BUILD-GENERAL.md for Python work

**Workflow:** SOLO or PLAN_EXECUTE per `AGENT-WORKFLOW-POLICY.md`.  
**Done:** runnable DONE WHEN + SELF-PROOF required.

---

## PROJECT STARTUP SEQUENCE

Before first line of code, in this order:
1. `mkdir project_name && cd project_name`
2. `git init`
3. Create `README.md`, `.gitignore`, `requirements.txt`
4. `git add . && git commit -m "chore: initial project setup"`
5. Create folder structure below
6. Then start coding

---

## STANDARD FOLDER STRUCTURE

```
project_name/
├── project_name/        # source package (same name as project)
│   ├── __init__.py
│   ├── core/            # business logic
│   │   └── __init__.py
│   ├── services/        # external integrations, APIs
│   │   └── __init__.py
│   ├── models/          # data models
│   │   └── __init__.py
│   └── utils/           # helper functions
│       └── __init__.py
├── tests/               # mirrors source structure
│   ├── test_core.py
│   └── test_utils.py
├── docs/
├── .env.example         # template — never commit .env itself
├── .gitignore
├── requirements.txt
├── README.md
└── main.py              # entry point
```

---

## NAMING CONVENTIONS

| Thing | Convention | Example |
|-------|-----------|---------|
| Variables | snake_case | `user_name` |
| Functions | snake_case, verb phrase | `calculate_total()` |
| Classes | PascalCase | `UserAccount` |
| Constants | UPPER_SNAKE_CASE | `MAX_RETRIES = 3` |
| Files | snake_case | `user_service.py` |
| Private | leading underscore | `_internal_helper()` |
| Tests | test_ prefix | `test_calculate_total.py` |

---

## CODE FORMATTING RULES

- 4 spaces indentation (never tabs)
- Max 79 characters per line (PEP 8)
- Two blank lines between top-level functions and classes
- One blank line between methods inside a class
- Imports at top: stdlib → third-party → local, separated by blank lines
- No wildcard imports (`from module import *`)
- Type hints on all function signatures
- Docstrings on all public functions and classes

---

## EVERY FUNCTION GETS

```python
def calculate_discount(price: float, rate: float) -> float:
    """
    Calculate discounted price.
    
    Args:
        price: Original price, must be >= 0
        rate: Discount rate between 0.0 and 1.0
    
    Returns:
        Discounted price
    
    Raises:
        ValueError: If price < 0 or rate not in [0, 1]
    """
    assert price >= 0, f"Price must be >= 0, got {price}"        # NASA Rule 5
    assert 0 <= rate <= 1, f"Rate must be 0-1, got {rate}"       # NASA Rule 5
    
    result = price * (1 - rate)
    
    assert result >= 0, "Result must be non-negative"             # NASA Rule 5
    return result
```

---

## VIRTUAL ENVIRONMENT — ALWAYS

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

Never `pip install` without updating `requirements.txt`.

---

## .GITIGNORE MINIMUM

```
venv/
__pycache__/
*.pyc
.env
*.log
.DS_Store
dist/
build/
*.egg-info/
```

---

## TEST FORMAT (every significant function)

```python
def test_calculate_discount():
    # Known input
    result = calculate_discount(100.0, 0.10)
    
    # Expected output
    expected = 90.0
    
    # Pass/fail
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Edge case
    assert calculate_discount(0, 0.5) == 0
    
    # Error case
    try:
        calculate_discount(-1, 0.1)
        assert False, "Should have raised ValueError"
    except (ValueError, AssertionError):
        pass  # Expected
```

---

## COMMIT MESSAGE FORMAT

```
feat: add user authentication module
fix: correct price calculation rounding error
docs: update README with setup instructions
refactor: extract validation logic to utils
test: add edge cases for discount calculator
chore: update dependencies to latest versions
```

Subject line under 50 characters. Imperative mood. No period at end.

---

## NASA RULE CHECKLIST FOR PYTHON

- [ ] Every loop has a maximum iteration count
- [ ] Every function fits on one screen
- [ ] Every function has at minimum one input assertion and one output assertion
- [ ] Every return value is checked by the caller
- [ ] No variable lives longer than it needs to
- [ ] Zero warnings from linter
