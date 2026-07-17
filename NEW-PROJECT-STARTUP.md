# NEW-PROJECT-STARTUP.md — New Project Startup
# Load when starting a brand new project

---

## WORKFLOW

Default: **PLAN_EXECUTE** (structure risk is high on new projects).  
Then **SOLO** for each MFVP feature after skeleton works.

---

## STARTUP SEQUENCE

### 1 — One-sentence goal + DONE WHEN
- [ ] What it does (one sentence)  
- [ ] Who uses it  
- [ ] Runnable DONE WHEN for **v1 MFVP only**  
- [ ] Explicit out of scope  

### 2 — Skeleton
```bash
mkdir project-name && cd project-name
git init
```

Create: `README.md`, `.gitignore`, (optional) `LICENSE`

### 3 — Project CLAUDE.md
Copy master `CLAUDE.md` and add: stack, folders, how to run, known landmines.

### 4 — Language tooling
See `BUILD-PYTHON.md` / `BUILD-WEB.md` / `BUILD-MOBILE.md` / `BUILD-EMBEDDED.md`

### 5 — Empty folders, then setup commit
```bash
git add .
git commit -m "chore: initial project setup"
```

### 6 — First MFVP only
Load `CLAUDE.md` + `BUILD-GENERAL.md` + stack file.  
Build the smallest thing that passes DONE WHEN.  
SELF-PROOF. Stop. Expand later.

---

## DO NOT

- Design full architecture before MFVP runs  
- Load multi-agent experimental SOPs by default  
- Skip git init / .gitignore on real projects  
