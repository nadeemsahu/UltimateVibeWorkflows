# Testing Strategy

## Frameworks
- **Unit Tests:** JUnit4 / Mockito / kotlinx-coroutines-test
- **E2E Tests:** Espresso / Robolectric

## Rules & Requirements
- **Coverage:** Aim for [X]% code coverage on critical paths.
- **Before Commit:** Always run `./gradlew test` before verifying a task is complete.
- **Failures:** NEVER skip tests or mock out assertions to make a pipeline pass without Human approval. If an Agent breaks a test, the Agent must fix it.

## Execution
- Command to run all tests: `./gradlew test`
- Command to run a single test file: `./gradlew testDebugUnitTest --tests "*MyTestClass"`