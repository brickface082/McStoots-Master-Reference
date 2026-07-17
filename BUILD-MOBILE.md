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
