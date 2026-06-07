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
