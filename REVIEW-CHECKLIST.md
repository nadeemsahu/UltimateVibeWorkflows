# Artifact Review Checklist 🔍

> **AGENTS:** Do not mark a feature or task as "Complete" until you verify these checks manually or via automated test runs. Provide terminal logs or browser testing results as proof. 
> **HUMANS:** Use this checklist before merging Agent-generated code.

## Code Quality & Safety
- [ ] No forceful unwrapping (`!!`) used unless structurally guaranteed.
- [ ] Protected files/directories (like infrastructure or migrations) were NOT modified without permission.
- [ ] No existing, unrelated tests were deleted or skipped.
- [ ] Component/Function is modular and doesn't violently break established architecture boundaries.

## Execution & Testing
- [ ] Application compiles without fatal errors.
- [ ] Linter passes (`./gradlew lint` or equivalent).
- [ ] Build passes (`./gradlew assembleDebug` or equivalent).
- [ ] Related Unit/Integration tests pass.
- [ ] UI is decently responsive across Desktop and Mobile viewports (if applicable).

## Artifact Handoff
- [ ] The `MEMORY.md` file was updated with any new architectural decisions made during this task.
- [ ] Any obsolete spec files in the workspace have been marked as resolved or archived.