# Android Engineering Playbook

## Overview
This playbook governs the development of Android applications. It enforces Modern Android Development (MAD) standards, including Clean Architecture, Jetpack Compose UI, Coroutines/Flow for asynchronous operations, and Hilt for Dependency Injection.

## 1. Feature Implementation (Clean Architecture)

### Prompt Template
```markdown
Context:
- Target Feature: {attached PRD/Feature spec}
- Architectural Pattern: Clean Architecture + MVVM

Task:
1. Implement the Domain layer: Define the Use Cases and Repository Interfaces. Use Kotlin Coroutines (`suspend`) for one-shot operations and `Flow` for data streams.
2. Implement the Data layer: Provide the concrete Repository implementations mapping DTOs to Domain Models.
3. Implement the Presentation layer: Create the `ViewModel` using `StateFlow` to expose UI state.
4. Scaffold the UI using Jetpack Compose.
5. Provide the Hilt `@Module` bindings required to inject these dependencies.
```

## 2. Hardware & System Services (NFC / Bluetooth)

### Prompt Template
```markdown
Context:
- Target Hardware API: {e.g., Host Card Emulation (HCE), BLE}

Task:
1. Implement the required Android `Service` or `BroadcastReceiver`.
2. Ensure the correct permissions (e.g., `<uses-permission android:name="android.permission.NFC" />`) are defined in the `AndroidManifest.xml`.
3. Wrap the system callbacks into Kotlin `callbackFlow` to expose them cleanly to the rest of the application.
4. Handle lifecycle events securely, ensuring resources are released in `onDestroy()`.
```

## 3. UI/UX Polishing (Jetpack Compose)

### Prompt Template
```markdown
Context:
- Target Screen: {attached screen name}
- Design System: {e.g., Glassmorphism, Material 3}

Task:
1. Refactor the Compose UI to meet the flagship-tier design specifications.
2. Implement required micro-animations using `animate*AsState` or `updateTransition`.
3. Ensure the UI is responsive across different screen sizes and orientations.
4. Use `RenderEffect` (API 31+) if advanced blurs are required, providing fallbacks for older API levels.
```
