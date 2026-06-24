# Code Patterns

## Purpose
This file defines the implementation patterns the agent should follow for the LibraryNFC project. Prefer these patterns over inventing new ones. 

## Architecture Pattern
- **Primary pattern:** Clean Architecture & MVVM (Model-View-ViewModel)
- **Rule:** Keep domain logic (NFC APDUs, business rules) strictly separate from the UI layer (Activities/Fragments).
- **Rule:** Use Hilt for Dependency Injection. Never instantiate repositories directly in Views.

## Data Fetching & Storage
- **Primary approach:** Coroutines for all asynchronous work. Room (if a local database is added) or `EncryptedSharedPreferences` for secure storage.
- **Rule:** Do not block the Main Thread. All I/O operations must be dispatched to `Dispatchers.IO`.

## State Management
- **UI State:** `StateFlow` and `SharedFlow` inside ViewModels. 
- **Rule:** The UI layer strictly *collects* state. It never mutates state directly. Actions are sent to the ViewModel as Intents/Events.
- **Rule:** Use `collectLatest` or `repeatOnLifecycle` in fragments to safely observe state.

## Error Handling
- Normalize errors at repository boundaries — never let raw exceptions crash the UI.
- Catch `Exceptions` inside Coroutine `try/catch` blocks or use `CoroutineExceptionHandler`.
- Return UI-safe error states via `StateFlow` to be rendered as Snackbars or Dialogs.

## Validation
- Validate all user inputs and NFC payloads at the ViewModel/Domain boundary.
- Do not trust raw APDU responses. Validate lengths and standard ISO7816 status words.

## File and Naming Conventions
- **Files/Classes:** PascalCase (e.g., `MainActivity.kt`, `PaymentViewModel.kt`)
- **Functions/Variables:** camelCase (e.g., `processApdu()`, `cardId`)
- **Constants:** UPPER_SNAKE_CASE (e.g., `MAX_RETRIES`)
- **XML Layouts:** snake_case (e.g., `fragment_scan.xml`, `item_card.xml`)

## Testing Pattern
- Add unit tests for pure logic and utility functions using JUnit4 and Mockito.
- Use `kotlinx-coroutines-test` for testing ViewModel StateFlow emissions.
- E2E/UI Tests: Use Espresso for UI verifications.
- Run the test suite (`./gradlew test`) after every feature; fix failures before moving on.

## Change Discipline
- Prefer focused, minimal edits over large rewrites.
- Do not introduce new dependencies without explicit approval.
- One feature at a time — commit or checkpoint after each working feature.
