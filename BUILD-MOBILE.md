# BUILD-MOBILE.md â€” Mobile App Build Standards
# Load with CLAUDE.md + BUILD-GENERAL.md
# Workflow: SOLO or PLAN_EXECUTE · Done: SELF-PROOF required
# McStoots Tech LLC | Load when building Flutter or React Native apps

---

## PLATFORM DECISION

**Flutter** â€” best choice for most McStoots Tech builds
- Single codebase for Android, iOS, web, desktop
- Hot reload
- Strong community, 700k+ Google Play apps
- State management: Riverpod (modern, compile-time safe) or BLoC (enterprise)

**React Native** â€” use when JavaScript flexibility is required or team knows JS deeply

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
â”œâ”€â”€ features/               # FEATURE-FIRST â€” same principle as React
â”‚   â”œâ”€â”€ auth/
â”‚   â”‚   â”œâ”€â”€ screens/        # full-page UI
â”‚   â”‚   â”œâ”€â”€ widgets/        # reusable UI components for this feature
â”‚   â”‚   â”œâ”€â”€ models/         # data models for this feature
â”‚   â”‚   â””â”€â”€ providers/      # state management for this feature
â”‚   â”œâ”€â”€ home/
â”‚   â””â”€â”€ settings/
â”œâ”€â”€ core/                   # app-wide shared code
â”‚   â”œâ”€â”€ theme/              # colors, typography, spacing
â”‚   â”œâ”€â”€ utils/              # helper functions
â”‚   â””â”€â”€ constants/          # app-wide constants
â”œâ”€â”€ shared/                 # truly shared widgets across features
â””â”€â”€ main.dart               # entry point only â€” minimal logic here
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
