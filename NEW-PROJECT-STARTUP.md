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
