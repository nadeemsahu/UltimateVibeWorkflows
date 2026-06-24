# AGENTS.md — Master Plan for LibraryNFC

## Project Overview & Stack
**App:** LibraryNFC
**Overview:** A modern Android application emulating NXP MIFARE DESFire-based library ID cards using Host Card Emulation (HCE), targeting library members requiring digital card access and a flagship-tier UI/UX.
**Stack:** Android, Kotlin, Coroutines, StateFlow, Hilt, Glassmorphism UI
**Critical Constraints:** Android API 31+ required for RenderEffect, strict separation of domain and UI via Clean Architecture, Coroutines for asynchronous work.

## Setup & Commands
Execute these commands for standard development workflows. Do not invent new package manager commands.
- **Setup:** `./gradlew build`
- **Development:** `./gradlew installDebug`
- **Testing:** `./gradlew test`
- **Linting & Formatting:** `./gradlew lint`
- **Build:** `./gradlew assembleRelease`

## Protected Areas
Do NOT modify these areas without explicit human approval:
- **Core HCE Logic:** `LibraryCard/src/main/java/com/piotrekwitkowski/libraryhce/HCEService.java` (Highly sensitive NFC APDU flows).
- **Security Logic:** Biometric prompt implementations and `EncryptedSharedPreferences` setups.
- **Build Configurations:** Gradle build scripts (`build.gradle.kts`, `settings.gradle.kts`) unless adding explicitly approved dependencies.

## Coding Conventions
- **Formatting:** Enforce standard Kotlin style guidelines (`ktlint`). Maintain clean imports.
- **Architecture rules:** Strict Clean Architecture. UI (`Activities`/`Fragments`) MUST only communicate with domain logic via `ViewModels` and `StateFlows`. No logic in the View layer.
- **Testing Expectations:** All new utilities must have unit tests (JUnit4/Mockito). Core user flows require Espresso UI tests or Robolectric.
- **Type Safety:** Leverage Kotlin's strict null-safety (`?`). Avoid forceful unwrapping (`!!`) unless structurally guaranteed.

## Agent Behaviors
These rules apply across all AI coding assistants (Cursor, Copilot, Claude, Gemini):
1. **Plan Before Execution:** ALWAYS propose a brief step-by-step plan before changing more than one file.
2. **Refactor Over Rewrite:** Prefer refactoring existing functions incrementally rather than completely rewriting large blocks of code.
3. **Context Compaction:** Write states to `workflows/MEMORY.md` or a `spec.md` instead of filling context history during long sessions.
4. **Iterative Verification:** Run tests or linters after each logical change. Fix errors before proceeding (See `workflows/REVIEW-CHECKLIST.md`).
5. **Team Coordination:** If working in Agent Teams, require the Team Lead to approve teammate PRs or plans.

---

## Vibe Coding Workflow Integration

This project embraces the **Vibe Coding** paradigm: "fully give in to the vibes, embrace exponentials, and forget that the code even exists."

All workflows, prompt templates, and playbooks are now centralized in the `workflows/` directory.
- See `workflows/custom_master_workflow.md` for the overarching 5-Pillar KDnuggets Vibe Coding methodology.
- See `workflows/vibe-coding-workflows.md` for Session Lifecycle, Artifact management, and Work-Type Playbooks.
- See `workflows/vibe-coding-prompt-template.md` for KhazP's advanced vibe coding prompt templates.
