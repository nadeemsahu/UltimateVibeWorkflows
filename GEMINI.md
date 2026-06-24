# GEMINI.md — Gemini CLI / Agent-First IDE Configuration for LibraryNFC

## Project Context
**App:** LibraryNFC
**Stack:** Android, Kotlin, Coroutines, StateFlow, Hilt
**Stage:** Production-Ready MVP
**User Level:** Developer

## Directives
1. **Master Plan:** Always read `workflows/AGENTS.md` first. It contains the current phase and tasks.
2. **Documentation:** Refer to `workflows/agent_docs/` for tech stack details, code patterns, and testing guides.
3. **Plan-First:** Propose a brief plan and wait for approval before coding.
4. **Incremental Build:** Build one small feature at a time. Test frequently.
5. **Pre-Commit:** If hooks exist, run them before commits; fix failures.
6. **No Linting:** Do not act as a linter. Use `./gradlew lint` if needed.
7. **Communication:** Be concise. Ask clarifying questions when needed.

## Commands
- `./gradlew installDebug` — Start on emulator
- `./gradlew test` — Run tests
- `./gradlew lint` — Check code style
