# McStoots Master Reference — Session Index
# Version 3.0 | READ THIS FIRST every session

---

## WHAT THIS SYSTEM IS

This is the McStoots Tech LLC AI coding and teaching system.
Built by Chris McStoots and Claude. Continuously improved.
GitHub: brickface082/McStoots-Master-Reference

---

## HOW TO USE THIS SYSTEM

**At the start of EVERY session:**
1. Read this index
2. Identify the session type below
3. Load only the files relevant to this session
4. Do not load files you do not need — they waste context

---

## SESSION TYPE → FILE TO LOAD

| What we are doing | Load this file |
|-------------------|----------------|
| Any build (always active) | `CLAUDE.md` |
| General coding, any language | `BUILD-GENERAL.md` |
| Python project | `BUILD-PYTHON.md` |
| Web / HTML / JS / React | `BUILD-WEB.md` |
| Mobile app / Flutter / React Native | `BUILD-MOBILE.md` |
| Embedded / C / C++ / Arduino | `BUILD-EMBEDDED.md` |
| Teaching Chris something | `TEACH.md` |
| Chris writing a prompt | `OPERATOR-CHECKLIST.md` |
| Quality review or debugging | `QUALITY-GATES.md` |
| Starting a brand new project | `NEW-PROJECT-STARTUP.md` |

---

## ALWAYS LOAD

- `CLAUDE.md` — active rules, always, every session, no exceptions

---

## ACTIVE PROJECTS

| Project | Status | Notes |
|---------|--------|-------|
| Fiat Lux PC Brand | Active — Raphael tier | Website build pending |
| MWOS Protocol | Active — v3.0/v4.0 | Search "MWOS" in past chats before responding |
| Polycentric Bang Cosmology | Active — theoretical | 31/35 audit passes |
| DataAnnotation | Active | AI evaluation qualification unlocked |
| DMX Cable Business | Active | 300ft spool, Neutrik connectors |
| Gentleman's Game Novel | Active | Chris=31, Greg=32, Luke=31, Jeff=28 |
| McStoots Handyman SOPs | Complete | Pricing correction needed |
| EPA Region 5 Career Track | Research phase | Strongest federal path |

---

## SOURCE QUALITY LOG (research from these first)

**Tier 1 — Pull from these first:**
- addyo.substack.com — Google engineering lead, AI workflows
- aimaker.substack.com — Claude-specific agent patterns
- tylerfolkman.substack.com — Quality control, multi-agent systems
- oreillyradar.substack.com — Deep quality engineering
- faafospecialist.substack.com — Honest Claude failure analysis

**Tier 2 — Good signal:**
- newsletter.pragmaticengineer.com — Big tech insider data
- newsletter.techworld-with-milan.com — Engineering laws
- devinterrupted.substack.com — Code review benchmarks

**Avoid:** Medium, generic best practices sites, SEO farms

---

## CONTINUOUS IMPROVEMENT LOG

- v1.0 — Initial build. Core execution loop, MFVP, task system, prompt format
- v2.0 — Added spec-first protocol, context packing, three-strike rule, simplicity gate, three-pass review, Claude failure modes, quality gates, source log
- v2.1 — Added NASA JPL Power of 10, Toyota Andon Cord, Poka-Yoke, Go/No-Go Gauge, FMEA, Five Whys, DO-178C, manufacturing master checklist
- v2.2 — Added Aviation CRM sterile cockpit, WHO surgical pause points, SUBSAFE OQE, mise en place, constraint log, five planning conversations, marginal gains
- v3.0 — Full restructure. Modular file system. Added Karpathy four laws, context window protocol (70/85/90 thresholds), token budget per task, deployable CLAUDE.md, code formatting standards by language, AI SOP competitive analysis

*This is a living system. Every session that teaches us something new gets logged here.*
-e 

---


# McStoots Tech LLC — Project Rules
# Version 3.0 | Drop this file in any project root. Claude reads it automatically.

---

## IDENTITY
You are Claude working with Chris McStoots (McStoots Tech LLC).
Owner: Chris | AI: Claude | Mode: BUILD MODE unless Chris says otherwise.

---

## THE FOUR LAWS (Karpathy — non-negotiable)

1. **THINK BEFORE CODING** — State assumptions explicitly. Surface ambiguity. Ask, never guess.
2. **SIMPLICITY FIRST** — Write minimum code that solves the stated problem. No unrequested abstractions.
3. **SURGICAL CHANGES** — Touch only what the request requires. Match existing style. Nothing else.
4. **GOAL-DRIVEN EXECUTION** — Define success criteria (Done When). Loop until verified. Then stop.

---

## CORE RULES

- Build smallest functional version first (MFVP) — ugly and hardcoded is fine
- One task at a time. One change at a time. Never stack.
- Never move forward unless current step works AND you understand why
- Real code only — no mocks, no fake tests, no simulated data
- Zero warnings = zero warnings. Treat every warning as an error.
- No function longer than one screen
- Every loop has a fixed upper bound
- Every return value from a non-void function gets checked
- DONE beats PERFECT

---

## REQUIRED PROMPT FORMAT (Chris must use this)

```
GOAL:         What are we building (1 sentence)
CONTEXT:      Language, platform, OS, existing code, versions
CONSTRAINTS:  Hard limits
DONE WHEN:    Exact binary pass/fail condition
```

---

## STOP CONDITIONS

Claude stops and reports to Chris when:
- Same fix fails 3 times in a row (Three-Strike Rule)
- Context window reaches 70% — summarize state and flag it
- Context window reaches 90% — mandatory fresh session with state log
- A task cannot be completed in 15 minutes — break it smaller first
- Blast radius is HIGH or CRITICAL and no backup exists

---

## CONTEXT WINDOW PROTOCOL

| Usage | Action |
|-------|--------|
| 0–50% | Work freely |
| 50–70% | Note usage, stay focused |
| 70–85% | Compact — summarize completed work, keep only current task |
| 85–90% | Prepare state tracking log handoff |
| 90%+ | STOP. Save state log. Start fresh session. |

---

## GATES — Nothing advances without clearing these

**Gate 1 — Scope:** Only requested files touched. No scope creep.
**Gate 2 — Real Code:** No mocks. No fake tests. Real implementation only.
**Gate 3 — Syntax:** Zero errors. Zero warnings. Consistent formatting.
**Gate 4 — Functional:** Correct output for known input. Edge cases tested.
**Gate 5 — Cross-Review:** Review as if someone else wrote it. Find problems.
**Gate 6 — Proof:** Multiple tests pass. Failure handling confirmed. Chris understands why it works.

---

## STATE TRACKING LOG (paste at start of continuing sessions)

```
CURRENT STATE:    [what works / what doesn't]
KNOWN BUGS:       [description + reproduction]
LAST CHANGE:      [what was modified]
LAST TEST:        Input: | Expected: | Actual: | Result:
NEXT STEP:        [first task this session]
STACK:            [language, framework, OS, versions]
CONTEXT USED:     [% at end of last session]
```

---

## ANDON CORD — Pull immediately when:
- Known bug exists from previous task
- Three-strike rule fires
- Test fails — build does not advance
- Blast radius is unacceptable without backup

*This file is the minimum viable rules set. Full SOP lives in GitHub: brickface082/McStoots-Master-Reference*
-e 

---


# BUILD-GENERAL.md — Core Build SOP
# McStoots Tech LLC | Load for any coding session alongside CLAUDE.md

---

## EXECUTION LOOP — THE ENGINE

Run in this exact order. Never skip. Never reorder.

1. Spec-first protocol — get approval
2. Paper thinking — map input, process, output, failure modes
3. Task list — get Chris approval before execution
4. ONE task using structured prompt format
5. Build MFVP — single file, hardcoded values allowed, no polish
6. Run immediately
7. Capture results using error feedback format
8. Fix ONE issue only
9. Retest
10. Log state
11. Repeat until stable
12. Prove working — multiple tests, edge cases, failure handling
13. Expand ONLY after proof

---

## SPEC-FIRST PROTOCOL

Before any code. No exceptions.

**Step 1 — Claude asks until all answered:**
- What does this do in one sentence?
- Who uses it and how?
- What are the inputs and outputs?
- What are the hard constraints?
- What does failure look like?
- What does success look like exactly?

**Step 2 — Spec file:**
```
SYSTEM:       What this does (1-2 lines)
INPUTS:       What goes in
OUTPUTS:      What comes out
CORE FLOW:    input → process → output
STACK:        Language / framework / platform / OS / versions
CONSTRAINTS:  Hard limits
SUCCESS:      Exact binary pass/fail condition
FAILURE MODES: Where it can break
```

**Step 3 — Chris approves. No code until approved.**

---

## PAPER THINKING — REQUIRED AFTER SPEC

```
[INPUT] → [PROCESS] → [OUTPUT]
               ↓
         [FAILURE MODES]
```

Minimum: inputs, outputs, transformations, failure points, simplest path.

---

## TASK SYSTEM

```
T001 — [smallest testable first step, max 15 min]
T002 — [only after T001 passes]
T003 — [continues until proof]
```

Rules:
- Each task = 5–15 minutes maximum
- Each task independently testable
- Max 40 instructions per task — no monolithic plans
- Claude proposes, Chris approves before execution

---

## TOKEN BUDGET PER TASK

Each task gets a maximum of 3 attempts to pass its Done When condition.
If 3 attempts fail, Claude stops, runs Five Whys, surfaces the problem to Chris.
No silent continuation. No fourth guess.

---

## ERROR FEEDBACK FORMAT

```
INPUT:    What you gave it
EXPECTED: What should have happened
ACTUAL:   What actually happened
ERROR:    Exact error message
```

---

## THREE-PASS REVIEW PROTOCOL

Run before declaring any build complete.

**Pass 1 — Structural:** Does code match spec? Hallucinated features? Missing features?
**Pass 2 — Requirement:** Does it actually solve the original problem? Test against Done When.
**Pass 3 — Consistency:** Naming uniform? No contradictions between modules? Style consistent?

---

## FINAL OUTPUT REQUIREMENT

Every build session ends with all five:
1. Working code that runs
2. How to run it
3. Test cases with known inputs and expected outputs
4. Known failure points and how they are handled
5. Next improvement step

---

## CLAUDE-SPECIFIC FAILURE MODES

| Failure | Fix |
|---------|-----|
| Starting before understanding goal | Spec-first protocol mandatory |
| Task dumping — doing everything at once | Task system enforced |
| Fake tests / mock data | Gate 2 — real code only |
| Context drift across sessions | State tracking log mandatory |
| Over-engineering | MFVP first, KISS gate before every expansion |
| Environment blindness | Context packing — OS, stack, versions in every prompt |
| Self-review false confidence | Gate 5 cross-review with explicit framing |
| Infinite retry spiral | Three-strike rule — hard stop at 3 |
| Touching files not asked | Gate 1 scope check |
| Assuming instead of asking | Spec-first protocol requires questions first |

---

## FMEA — RUN BEFORE BUILDING ANYTHING THAT HANDLES DATA

Before the MFVP, list the top 3 failure modes:
1. What can go wrong? (likelihood 1–10)
2. What happens if it does? (severity 1–10)
3. How detectable before damage? (detectability 1–10)

Multiply L × S ÷ D. Design against highest numbers first.

---

## FIVE WHYS — RUN WHEN THREE-STRIKE FIRES

Ask why five times. Fix the root cause, not the symptom.

Example: Function returned wrong value → Why? No input validation → Why? Not in spec → Why? Skipped FMEA → Why? In a hurry to start coding. Root cause: skipped FMEA. Fix the process, not just the code.

---

## SIMPLICITY GATE

Before expanding: does a simpler version pass the Done When condition?
If yes, build simpler first.
Every line of code is a potential failure point.
-e 

---


# BUILD-PYTHON.md — Python Build Standards
# McStoots Tech LLC | Load when building Python projects

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
-e 

---


# BUILD-WEB.md — Web Build Standards
# McStoots Tech LLC | Load when building web projects (HTML, JS, React, TypeScript)

---

## BUILD SEQUENCE

1. Static HTML/CSS/JS first — no frameworks until MFVP proven
2. One working page, one working interaction
3. Mobile layout works
4. Add backend only if required
5. Deploy to Vercel or Netlify — free, fast, zero config
6. Point domain if needed

---

## PROJECT STARTUP

```bash
mkdir project-name && cd project-name
git init
# Create: index.html, styles.css, main.js, README.md, .gitignore
git add . && git commit -m "chore: initial project setup"
```

---

## STANDARD REACT/TYPESCRIPT STRUCTURE

```
src/
├── app/                    # app config, routing, global layout
├── features/               # FEATURE-FIRST organization
│   └── auth/
│       ├── components/     # UI components for this feature
│       ├── hooks/          # custom hooks for this feature
│       ├── types/          # TypeScript interfaces for this feature
│       └── auth.test.ts    # tests live next to code
├── components/             # truly shared components only
├── lib/                    # shared utilities
├── types/                  # shared TypeScript types
└── api/                    # API layer
```

---

## NAMING CONVENTIONS

| Thing | Convention | Example |
|-------|-----------|---------|
| React components | PascalCase | `UserProfile.tsx` |
| Files for components | PascalCase | `UserProfile.tsx` |
| Variables, functions | camelCase | `getUserData()` |
| Constants | UPPER_SNAKE_CASE | `MAX_ITEMS = 50` |
| CSS files | kebab-case | `user-profile.css` |
| Folders | kebab-case | `user-profile/` |
| Boolean props | is/has/should prefix | `isLoading`, `hasError` |
| Event handlers | handle prefix | `handleClick`, `handleSubmit` |

---

## CODE RULES

- TypeScript is the default for serious React work — use `.tsx` not `.jsx`
- Named exports, not default exports (makes refactoring easier)
- All components are functional — no class components
- TypeScript props interfaces on every component
- Early returns to reduce nesting — if condition fails, return early
- No nested components inside render — extract to separate files
- ESLint and Prettier configured before first component — not optional

---

## HTML FIRST RULE

Every web build starts as plain HTML. No React, no framework, no build tools.
If the HTML version works and is sufficient, ship the HTML version.
Add React only when the complexity genuinely requires it.

---

## DEPLOYMENT (Vercel — simplest path)

```bash
npm install -g vercel
vercel           # follow prompts — done in 2 minutes
```

Or drag the project folder to netlify.com/drop for instant deploy.

---

## VERIFICATION BEFORE DECLARING DONE

- [ ] Page loads without console errors
- [ ] All buttons produce expected behavior
- [ ] Layout holds on mobile (resize browser to 375px width)
- [ ] Forms validate input — valid, invalid, and empty
- [ ] No hardcoded localhost URLs
- [ ] API keys not in source code (use .env)
- [ ] .env in .gitignore

---

## .GITIGNORE MINIMUM

```
node_modules/
.env
.env.local
.DS_Store
dist/
.next/
build/
*.log
```

---

## COMMIT FORMAT

Same as Python. feat/fix/docs/refactor/test/chore prefix. Under 50 chars. Imperative mood.
-e 

---


# BUILD-MOBILE.md — Mobile App Build Standards
# McStoots Tech LLC | Load when building Flutter or React Native apps

---

## PLATFORM DECISION

**Flutter** — best choice for most McStoots Tech builds
- Single codebase for Android, iOS, web, desktop
- Hot reload
- Strong community, 700k+ Google Play apps
- State management: Riverpod (modern, compile-time safe) or BLoC (enterprise)

**React Native** — use when JavaScript flexibility is required or team knows JS deeply

---

## FLUTTER PROJECT STARTUP

```bash
flutter create project_name
cd project_name
git init
git add . && git commit -m "chore: flutter project init"
```

---

## FLUTTER FOLDER STRUCTURE

```
lib/
├── features/               # FEATURE-FIRST — same principle as React
│   ├── auth/
│   │   ├── screens/        # full-page UI
│   │   ├── widgets/        # reusable UI components for this feature
│   │   ├── models/         # data models for this feature
│   │   └── providers/      # state management for this feature
│   ├── home/
│   └── settings/
├── core/                   # app-wide shared code
│   ├── theme/              # colors, typography, spacing
│   ├── utils/              # helper functions
│   └── constants/          # app-wide constants
├── shared/                 # truly shared widgets across features
└── main.dart               # entry point only — minimal logic here
```

---

## NAMING CONVENTIONS

| Thing | Convention | Example |
|-------|-----------|---------|
| Classes, widgets | PascalCase | `UserProfileScreen` |
| Variables, functions | camelCase | `getUserData()` |
| Files | snake_case | `user_profile_screen.dart` |
| Constants | lowerCamelCase (Dart convention) | `kPrimaryColor` |
| Private members | leading underscore | `_buildHeader()` |
| Screen widgets | Screen suffix | `HomeScreen` |
| Reusable widgets | Widget suffix | `UserAvatarWidget` |

---

## MFVP RULES FOR MOBILE

- One screen
- One feature
- No animations
- No polish
- Must launch on real device or emulator and perform core action once

---

## STATE MANAGEMENT DECISION (make at project start)

Pick one pattern and document it in README. Never mix patterns.

| App size | Recommended |
|----------|-------------|
| Small / prototype | setState + Provider |
| Medium | Riverpod |
| Large / enterprise | BLoC |

---

## VERIFICATION BEFORE DECLARING DONE

- [ ] Runs on real device, not just emulator
- [ ] Tap/click triggers correct state update
- [ ] No crashes on core user flow
- [ ] Loading states visible (user knows something is happening)
- [ ] Error states visible (user knows something went wrong)
- [ ] App startup time acceptable (under 3 seconds cold start)
- [ ] Memory usage not growing unbounded during use

---

## BUILD AND RELEASE

```bash
# Android
flutter build apk --release

# iOS (requires Mac)
flutter build ios --release
```

---

## CONVENTIONS SECTION IN README (required)

Every Flutter project README must include a section titled Conventions that documents:
- State management pattern chosen and why
- Folder structure description
- Naming rules
- How to run tests

This reduces AI drift across sessions and onboards any new contributor in under 5 minutes.
-e 

---


# BUILD-EMBEDDED.md — Embedded and Hardware Build Standards
# McStoots Tech LLC | Load when building C, C++, Arduino, ESP-IDF projects

---

## SAFETY FIRST — READ BEFORE ANY HARDWARE TEST

1. Simulate first if at all possible
2. Define ALL failure modes before powering on
3. Document expected current draw, voltage, and timing
4. Test with safe input and limited power first
5. Never assume environment — verify with the actual device

---

## PROJECT STARTUP

```
project_root/
├── src/
│   ├── main/               # main application
│   │   └── main.c
│   ├── common/             # shared utilities
│   │   └── utils.c
│   └── drivers/            # hardware abstraction layer
├── include/                # all header files
│   ├── main/
│   └── common/
├── lib/                    # external libraries
├── tests/                  # unit tests
│   └── unit_tests/
├── docs/                   # schematics, pinouts, datasheets
├── config/
│   └── linker_scripts/
├── CMakeLists.txt          # or Makefile
└── README.md
```

---

## NAMING CONVENTIONS

| Thing | Convention | Example |
|-------|-----------|---------|
| Functions | snake_case | `read_sensor_value()` |
| Variables | snake_case | `sensor_reading` |
| Constants | UPPER_SNAKE_CASE | `MAX_BUFFER_SIZE` |
| Global constants | UPPER_SNAKE_CASE | `BAUD_RATE = 9600` |
| Structs, typedefs | PascalCase or _t suffix | `SensorData` or `sensor_data_t` |
| Pointer variables | p prefix | `pBuffer` |
| Private/internal | leading underscore | `_internal_calculate()` |
| Macros | UPPER_SNAKE_CASE | `#define LED_PIN 13` |

---

## NASA POWER OF 10 — MANDATORY FOR ALL EMBEDDED CODE

These rules apply to every file. No exceptions.

1. **Simple control flow** — no goto, no recursion, no deeply nested conditionals
2. **Bounded loops** — every loop has a hard maximum iteration count defined before the loop
3. **No dynamic memory in critical paths** — allocate at init, not during operation
4. **Functions fit on one screen** — if it scrolls, split it
5. **Two assertions per function minimum** — one on input, one on output
6. **Variables at smallest scope** — declare inside the block where used
7. **Check every return value** — if a function can fail, the caller checks
8. **Readable code** — no magic numbers, no clever tricks, no abbreviations
9. **One level of dereference** — no pointer-to-pointer-to-pointer chains
10. **Zero warnings** — compile with maximum warnings. All warnings are errors.

---

## EVERY C FUNCTION STRUCTURE

```c
/**
 * @brief Read temperature from sensor
 * @param sensor_pin GPIO pin number (0-39)
 * @param reading Output: temperature in Celsius
 * @return 0 on success, -1 on error
 */
int read_temperature(uint8_t sensor_pin, float* reading) {
    /* Input assertions — NASA Rule 5 */
    assert(sensor_pin <= 39);
    assert(reading != NULL);
    
    /* Implementation */
    float raw = analogRead(sensor_pin);
    *reading = (raw / 4095.0f) * 100.0f;
    
    /* Output assertion — NASA Rule 5 */
    assert(*reading >= -40.0f && *reading <= 125.0f);
    
    return 0;
}
```

---

## HEADER FILE STRUCTURE

```c
/* sensor.h */
#ifndef SENSOR_H        /* Include guard — required on every header */
#define SENSOR_H

#include <stdint.h>     /* Standard fixed-width types */
#include "config.h"     /* Project configuration */

/* Constants */
#define SENSOR_MAX_READING  4095
#define SENSOR_TIMEOUT_MS   1000

/* Type definitions */
typedef struct {
    float temperature;
    float humidity;
    uint32_t timestamp;
} SensorData_t;

/* Function declarations */
int sensor_init(uint8_t pin);
int sensor_read(SensorData_t* data);
void sensor_reset(void);

#endif /* SENSOR_H */
```

---

## MISRA C RULES (safety-critical builds)

Required for any code where failure causes physical risk:
- No dynamic memory allocation after init
- No goto
- No continue
- Array indexing only — no pointer arithmetic
- Explicit casting — no implicit type conversions
- No unreachable code

---

## ARDUINO-SPECIFIC

```cpp
void setup() {
    // Hardware init goes here — all of it, before loop()
    Serial.begin(9600);
    pinMode(LED_PIN, OUTPUT);
    sensor_init(SENSOR_PIN);
}

void loop() {
    // Keep loop() short
    // Move all logic to functions
    uint32_t iteration_count = 0;
    const uint32_t MAX_ITERATIONS = 1000;  // NASA Rule 2
    
    while (condition && iteration_count < MAX_ITERATIONS) {
        do_work();
        iteration_count++;
    }
}
```

---

## VERIFICATION CHECKLIST

- [ ] Compiles with zero warnings at maximum warning level
- [ ] Every loop has a hard iteration limit
- [ ] Every function has at minimum one input and one output assertion
- [ ] Every return value is checked
- [ ] No function is longer than one screen
- [ ] No dynamic memory allocation in the main execution path
- [ ] Tested with safe input and limited power before full operation
- [ ] Failure modes documented before power-on
-e 

---


# QUALITY-GATES.md — Complete Quality Control System
# McStoots Tech LLC | Load when reviewing, debugging, or verifying builds

---

## THE SIX GATES — Nothing advances without clearing all six

### Gate 1 — Scope Control
- [ ] Change addresses only what was requested
- [ ] No unrelated refactors
- [ ] No unintended files modified
- [ ] No scope creep absorbed silently

### Gate 2 — Real Code
- [ ] All code is real implementation — no mocks, no simulated data
- [ ] Tests verify actual behavior, not just pass to pass
- [ ] No hardcoded fake return values
- [ ] If something is hardcoded intentionally, it is documented

### Gate 3 — Syntax and Format
- [ ] Code runs without syntax errors
- [ ] Formatting matches surrounding code
- [ ] Zero warnings from compiler or linter
- [ ] Variable and function names are clear and descriptive

### Gate 4 — Functional Validation
- [ ] Correct output for known input
- [ ] Edge cases tested
- [ ] Invalid input tested
- [ ] Empty input tested
- [ ] Failure produces clear error, not silent crash

### Gate 5 — Cross-Review (Independent Verification)
**Explicit instruction required:** "You did not write this code. Review it critically. Find problems."
- [ ] Logic errors caught
- [ ] Security issues caught
- [ ] Edge cases not already tested identified
- [ ] Performance problems flagged

### Gate 6 — Proof of Work
- [ ] Multiple test cases pass
- [ ] Edge cases pass
- [ ] Failure handling confirmed
- [ ] Chris understands WHY it works, not just that it works
- [ ] Three-pass review complete

---

## THREE-PASS REVIEW

**Pass 1 — Structural**
Does code do what it was designed to do? Does it match the spec?
Hallucinated features? Missing features? Correct architecture?

**Pass 2 — Requirement Verification**
Does code fulfill its purpose — not just run, but actually solve the problem?
Test against the Done When condition from the original prompt.

**Pass 3 — Consistency**
Are naming conventions uniform throughout?
Contradictions between modules?
Anything in one file that breaks assumptions in another?

---

## OBJECTIVE QUALITY EVIDENCE FORMAT (SUBSAFE-derived)

Every significant function needs a completed test record before build closes:

```
FUNCTION TESTED:   [function name and file]
INPUT USED:        [exact input values]
EXPECTED OUTPUT:   [exact expected result]
ACTUAL OUTPUT:     [what actually happened]
RESULT:            PASS or FAIL
DATE:              [date tested]
```

"I tested it" is not Objective Quality Evidence.
A completed record above is.

---

## WHO SURGICAL PAUSE POINTS

Full stop at these three moments. No exceptions. No time pressure overrides this.

**Pause 1 — Before coding starts:**
- [ ] Spec approved
- [ ] Environment confirmed
- [ ] Task defined with Done When condition
- [ ] State tracking log loaded (if continuing)
- [ ] Constraints identified

**Pause 2 — Before first test runs:**
- [ ] Code complete for this task
- [ ] Assertions in place
- [ ] Return values checked
- [ ] Gate 1 scope confirmed — no unintended files

**Pause 3 — Before declaring done:**
- [ ] Done When condition tested with evidence
- [ ] All five Final Output Requirements met
- [ ] Continuous Improvement Log updated

---

## MANUFACTURING QUALITY MASTER CHECKLIST

### Prevention (Poka-Yoke Level 1)
- [ ] Spec-first protocol ran and was approved before code started
- [ ] Every task had binary go/no-go Done When condition
- [ ] FMEA run on top 3 failure modes before building

### Detection (Poka-Yoke Level 2)
- [ ] Every function has input and output assertions
- [ ] Every loop has a hard upper bound
- [ ] Every return value checked
- [ ] All code passes with zero warnings
- [ ] All tests are real — no mocks

### Verification (DO-178C Independent Review)
- [ ] Gate 5 cross-review ran with explicit "you did not write this" framing
- [ ] Three-pass review complete
- [ ] Go/no-go Done When produced binary pass

### Root Cause (Five Whys)
- [ ] For every failure during build, Five Whys was run
- [ ] Root cause addressed, not just symptom
- [ ] New failure modes added to Continuous Improvement Log

### Proof
- [ ] Working code runs
- [ ] Instructions to run it documented
- [ ] Test cases with known inputs and expected outputs exist
- [ ] Known failure points documented
- [ ] Next improvement step identified

---

## ANDON CORD — PULL IMMEDIATELY

Stop everything and report to Chris when any of these fire:

- Three consecutive failures on same fix
- Known bug from previous task is unresolved and new task starting
- Test fails — build does not advance
- Blast radius is unacceptable without backup
- Context window hits 90%

**When Andon fires:**
1. State clearly what was tried
2. State what the consistent failure point is
3. Run Five Whys on the failure
4. Ask Chris how to proceed — do not guess

---

## BLAST RADIUS ASSESSMENT

Before any task touching existing data, files, or systems:

| Risk Level | Situation | Action Required |
|-----------|-----------|-----------------|
| Low | Creating new files only | Proceed |
| Medium | Modifying existing files | Save previous version |
| High | Deleting files, modifying database | Full backup required |
| Critical | Customer data, payments, auth | Stop. Think. Back up. Get second opinion. |

---

## CONTEXT WINDOW HEALTH CHECK

| Usage | Status | Action |
|-------|--------|--------|
| 0–50% | Green | Work freely |
| 50–70% | Yellow | Stay focused, avoid topic changes |
| 70–85% | Orange | Summarize completed work, compact if possible |
| 85–90% | Red | Prepare state tracking log |
| 90%+ | Critical | Stop. Save state log. Start fresh session. |
-e 

---


# OPERATOR-CHECKLIST.md — Chris Pre-Build Checklist
# McStoots Tech LLC | Run before every build session

---

## THE ONE SENTENCE RULE

If you cannot describe what you want to build in one clear sentence,
you are not ready to build it yet.
Five minutes of thinking saves an hour of rework.

---

## PRE-FLIGHT CHECKLIST

Answer every question before sending the first prompt.
Claude will ask these before proceeding. There are no shortcuts.

**Q1 — What exactly am I building?**
One sentence. A stranger reads it and knows exactly what the thing does.
Bad: An app for my business.
Good: A Python script that reads a CSV and sends each row a personalized text message.

**Q2 — Who uses it and how?**
Is it just you? A customer? Walk through what they do step by step.

**Q3 — What goes in and what comes out?**
Name the inputs. Name the outputs. Include format, type, and size.

**Q4 — What platform and environment?**
OS. Language. Device. Existing code. Version numbers you know.

**Q5 — What are the hard constraints?**
Things that absolutely cannot be violated.
No internet. Android only. Free hosting. Under 10MB. No paid libraries.

**Q6 — What does done look like exactly?**
Write the binary pass/fail condition.
Bad: It works correctly.
Good: Script reads test.csv with 3 rows, prints "Sent 3 messages", shows each name. Any other output is a fail.

**Q7 — What are you NOT building?**
At least one thing that is explicitly out of scope.

---

## STANDARD BUILD PROMPT TEMPLATE

Copy this. Fill every field. Send nothing vague.

```
WHAT IT DOES:    [one sentence]
WHO USES IT:     [who and how]
INPUTS:          [what goes in, format, type]
OUTPUTS:         [what comes out, format, type]
PLATFORM:        [OS, language, device, existing code, versions]
CONSTRAINTS:     [hard limits that cannot be violated]
OUT OF SCOPE:    [what we are NOT building]
DONE WHEN:       [exact binary pass/fail condition]
```

---

## THE FIVE OPERATOR FAILURE MODES

**Failure 1 — The Vague Goal**
Claude stops and runs pre-flight before proceeding.

**Failure 2 — The Missing Environment**
Claude asks for OS, language, platform, versions before writing a single line.

**Failure 3 — The Moving Goalpost**
If a new requirement appears mid-build:
Claude stops, asks: "Is this a change to the current spec or a new task?"
If it changes the spec, the current build pauses and spec gets re-approved first.

**Failure 4 — The Skipped Verification**
Claude explicitly asks: "Did you run it? Did it pass the Done When condition?"
"Looks good" is not a pass. Running it and getting expected output is a pass.

**Failure 5 — The Undefined Done When**
Claude refuses to start and helps Chris define the Done When condition first.

---

## BLAST RADIUS RULE

Before any task touching existing data, files, or live systems:
"If this goes wrong, what is the worst that can happen? Can we recover?"

If the answer is NO — back up first. Always. No exceptions.

---

## CONTEXT QUALITY RULES

- Give minimum necessary context — not everything you know
- Never paste entire codebase — point to specific files and functions
- State what already works and what does not
- If continuing previous session — paste State Tracking Log FIRST

---

## SESSION MISE EN PLACE

Before sending first prompt, confirm all:
- [ ] Spec can be described in one sentence
- [ ] Platform and environment are identified
- [ ] Done When condition is binary and written
- [ ] At least one thing is explicitly out of scope
- [ ] Blast radius assessed — backup done if needed
- [ ] State tracking log ready if continuing previous work

---

## PROMPT QUALITY SELF-CHECK

Before hitting send:
- [ ] Can I describe what I want in one sentence?
- [ ] Did I name the platform, OS, and language?
- [ ] Did I write a binary Done When condition?
- [ ] Did I name at least one thing out of scope?
- [ ] Is my prompt under 200 words? (If not, probably too complex — break into two tasks)

---

## WHEN TO STOP AND THINK INSTEAD OF PROMPT

Stop and think when:
- You are not sure what success looks like
- You changed your mind since the last message
- You want to add something not in the original spec
- You are frustrated and want to send the same thing again
- You do not know how to run or test the output

In every case, the problem is upstream of Claude.
Prompting more does not fix a thinking problem.
-e 

---


# TEACH.md — Learning and Instruction SOP
# McStoots Tech LLC | Load when Claude is teaching Chris something

---

## TEACHING MODE ACTIVE

When this file is loaded:
- Build mode is SUSPENDED
- Claude teaches, explains, and demonstrates
- Theory connects to practice — Chris learns by doing
- Switch back to BUILD-GENERAL.md when ready to build

---

## HOW CHRIS LEARNS — CRITICAL CONTEXT

- Learns by doing, not by reading walls of text
- Listens to responses read aloud while working — no tables, no bullet walls
- 20 years industrial/manufacturing experience — connect concepts to physical analogies
- Strong BS detector — get to the point, no padding
- Short testable provable steps work better than long comprehensive lessons
- If Chris already knows it, skip it

---

## TEACHING LOOP

1. Identify what Chris wants to be ABLE TO DO — not just know
2. Connect to something he already understands (see analogy library below)
3. Teach smallest useful piece first
4. Give Chris something to try immediately
5. Ask what happened — do not explain what should happen before he tries
6. Correct only what is actually wrong
7. Prove with real example or test
8. Confirm understanding before moving forward
9. Expand only after proof

---

## TEACHING MODES

**Mode 1 — Concept Teaching**
Use analogy first, then detail. Keep under 90 seconds spoken. Then apply immediately.

**Mode 2 — Skill Building**
Smallest working version of the skill first. No theory until he has tried it.

**Mode 3 — Troubleshooting**
Diagnostic tree — eliminate causes one at a time. Chris arrives at the answer, not just receives it.

**Mode 4 — Exam Prep**
Q&A format. Track score. Drill weak areas only. Do not re-drill what he knows.

**Mode 5 — Prompt Literacy**
After every prompt Chris sends, show the cleaner version at the end:
```
CLEANER PROMPT WOULD HAVE BEEN:
[rewritten version]
WHY: [one sentence explanation]
```

---

## ANALOGY LIBRARY — Connect to these domains first

- Industrial and manufacturing — flow, pressure, tolerance, quality control
- Water treatment — chemistry, flow rates, system balance, contamination
- Wrestling — technique before strength, drilling, muscle memory, strategy
- Fabrication and welding — fit and finish, structural integrity, tolerances
- Automotive — diagnosis, cause and effect, systems thinking
- Electronics — circuits, signals, troubleshooting

---

## LEARNING STAGES

**Stage 1 — Awareness:** Knows concept exists. Cannot apply.
**Stage 2 — Understanding:** Can explain how it works. Has not proven it.
**Stage 3 — Application:** Has used it in a real task. Worked at least once.
**Stage 4 — Proven Ability:** Can apply consistently, explain to others, troubleshoot. THIS is learned.

Identify Chris's current stage at the start. Target the next stage.

---

## PACING RULES

- One concept at a time — never stack new ideas
- If response would take more than 90 seconds to read aloud — too long, break it up
- Always end on a question or task — never end on pure information
- If Chris demonstrates understanding, move forward — do not repeat
- If Chris is stuck — go smaller, find the step inside the step

---

## STOP CONDITIONS FOR TEACHING

Do NOT move to next concept until:
- Chris can explain what he just learned in his own words
- Chris has applied it at least once with successful result
- Chris can identify at least one way it could go wrong

---

## WHAT CLAUDE NEVER DOES IN TEACHING MODE

- No wall of text before Chris tries anything
- No tables — Chris listens, tables do not translate to audio
- No re-explaining what Chris already demonstrated he knows
- No skipping the analogy step for complex concepts
- No moving forward just because Chris says he understands — verify with task
- No conflating teaching mode with build mode — switch files when building
-e 

---


# NEW-PROJECT-STARTUP.md — New Project Startup Checklist
# McStoots Tech LLC | Load when starting any brand new project

---

## THE PROFESSIONAL STARTING LINE

Every professional starts here before writing a single line of code.
Do not skip any step. The order matters.

---

## UNIVERSAL STARTUP SEQUENCE

### Step 1 — Define before building
Answer these before touching a keyboard:
- [ ] What does this do in one sentence?
- [ ] Who uses it?
- [ ] What goes in and what comes out?
- [ ] What does done look like exactly (binary pass/fail)?
- [ ] What is explicitly NOT in scope?

### Step 2 — Create project structure
```bash
mkdir project-name
cd project-name
git init
```

### Step 3 — Create foundation files BEFORE any code
```bash
# Create these first — in this order
touch README.md
touch .gitignore
touch LICENSE    # if project will be shared
```

### Step 4 — Create CLAUDE.md for this project
Copy the master CLAUDE.md and add project-specific context:
- Stack and versions
- Folder structure with one-line description of each folder
- Naming conventions in use
- How to run the tests
- Things that commonly cause problems in this specific codebase

### Step 5 — Set up language-specific tooling
See BUILD-PYTHON.md, BUILD-WEB.md, BUILD-MOBILE.md, or BUILD-EMBEDDED.md

### Step 6 — Create folder structure
Create all folders empty before writing code.

### Step 7 — First commit — SETUP ONLY, no code
```bash
git add .
git commit -m "chore: initial project setup"
```

### Step 8 — Then and only then — start coding
Load BUILD-GENERAL.md and the relevant language file.
Run spec-first protocol.
Begin with MFVP.

---

## README.md MUST CONTAIN

Every README answers: **What, Why, and How**

```markdown
# Project Name

One sentence description of what this does.

## Why

Why this exists. What problem it solves.

## Quick Start

Exact commands to install and run from scratch:
```bash
git clone [url]
cd project-name
[setup commands]
[run command]
```

## Folder Structure

Brief description of each folder and what lives there.

## Conventions

- Naming conventions used
- State management pattern (if app)
- How to run tests
- Anything that commonly trips people up
```

---

## .GITIGNORE — CREATE FROM TEMPLATE

Visit gitignore.io and generate for your stack.
Minimum rules regardless of stack:
```
.env
*.log
.DS_Store
```

**Never commit:**
- API keys or secrets
- .env files
- Passwords, tokens
- Build artifacts that can be regenerated

---

## MARGINAL GAINS PROTOCOL — NEW PROJECT EDITION

Every session that adds a rule or fix to CLAUDE.md is a marginal gain.
Every failure mode discovered and documented is a marginal gain.
These compound across projects.

The CLAUDE.md that exists after 10 projects is dramatically better than the one that exists today because each project added something.

Update CLAUDE.md at the end of every session with:
- New rule learned
- Failure mode discovered
- Convention established

---

## ASSESS BLAST RADIUS — BEFORE EVERY CHANGE

This project is NEW, so most blast radius is LOW (new files only).
As the project grows, reassess before every significant change.

| What you are doing | Blast Radius |
|-------------------|-------------|
| Creating new files | Low |
| Modifying existing files | Medium — save previous state |
| Deleting files | High — backup first |
| Database operations | Critical — full backup + second opinion |
