# Project Brief

- **Product vision:** A modern Android application emulating NXP MIFARE DESFire-based library ID cards using Host Card Emulation (HCE), targeting library members requiring digital card access and a flagship-tier UI/UX.
- **Target Audience:** Library members expecting seamless, Apple Wallet-tier digital card access.

## Conventions
- **Naming:** camelCase for variables, PascalCase for Kotlin classes, snake_case for XML layouts.
- **File Structure:** Maintain Clean Architecture boundaries. Colocate ViewModels with their associated UI Fragments.

## Key Principles
- Ship the simplest possible solution that solves the user story.
- Performance is a feature. Maintain 60fps UI using optimized Coroutines and RenderEffect glassmorphism.