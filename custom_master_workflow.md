# Custom Master Vibe Coding Workflow

This custom workflow is synthesized from the top 10 Vibe Coding methodologies, specifically adapted to be practical and actionable for the **LibraryNFC** Android project. It merges Prompting, Context Engineering, Safety, Orchestration, and Token Optimization into a unified execution pipeline.

---

## Pillar 1: Context Engineering (The Foundation)
Before any code is generated, the AI must have perfect, zero-guesswork context.
1. **The Rulebook (`workflows/AGENTS.md`):** The single source of truth for architectural constraints, allowed dependencies, and global behaviors.
2. **Persistent Artifacts:** Do not rely on chat history. Actively maintain `docs/PRD.md` (Product Requirements), `docs/TECH_DESIGN.md` (Architecture), and `workflows/NOTES.md` (Running logs and decisions). 

## Pillar 2: Prompt Templates & Style Compression
1. **Session Openers:** Always start a session with a strict template defining the Task, the Context, and the boundary of what *not* to touch.
2. **Token-Compressed Instructions:** Maintain dense, concise guidelines in `workflows/agent_docs/` to leave maximum context window for analyzing the Kotlin codebase.
3. **The Vibe Brief:** For any new feature, write a "Vibe Brief" detailing User Stories and the "Definition of Done".

## Pillar 3: Agent Orchestration & State Tracking
Instead of relying on external Kanban software, orchestration is handled entirely within the repository to ensure continuous sync.
1. **Markdown Task Tracking:** Use transient task lists (`task.md`) and persistent check-offs in `workflows/NOTES.md` to track sub-agent progress.
2. **Global Agent Settings:** Ensure AI tools (Cursor, Copilot, Gemini) all respect the directives defined in `workflows/GEMINI.md` and `workflows/AGENTS.md`.

## Pillar 4: Live Context Verification
Do not blindly guess codebase structure. Replace static hallucinations with live verification.
1. **Static Analysis as "Vibe Check":** Instead of requiring a standalone MCP server, use local Android tooling. Run `./gradlew lint` or `grep_search` to verify code state against expected domain logic.
2. **Component Mapping:** Maintain and update UI-to-Logic graph definitions when adding new Views or ViewModels to prevent state drift.

## Pillar 5: Safety & Execution Verification
AI agents are forbidden from committing unverified code.
1. **Native Sandboxing:** For Android modules, use Gradle testing (`./gradlew test`). For Backend/Cloud infrastructure modules, rely on Docker sandboxing. All generated code must be validated to isolate and catch logic errors.
2. **Compile-Time Observability:** A successful build (`./gradlew build` or `docker build`) is mandatory before marking any Vibe Brief or implementation plan as "Done."
3. **Infinite Loop Breaker (CRITICAL):** If an Agent runs tests and fails 3 consecutive times trying to fix the same bug, the Agent MUST immediately pause execution, stop modifying code, and explicitly escalate the issue to the human developer.

---

## The Execution Loop
When starting a task on LibraryNFC, follow this exact loop:
1. **Initialize:** Read `workflows/AGENTS.md` and `docs/PRD.md`.
2. **Prompt:** Use a Session Opener template to define scope.
3. **Query:** Use `grep_search` and `view_file` to verify live code structure.
4. **Execute:** Write the Kotlin/XML code.
5. **Sandbox & Verify:** Test the code locally using `./gradlew test` and `./gradlew build`.
6. **Track:** Mark the task as completed in the Markdown task tracker.
7. **Persist:** Document outcomes in `docs/CHANGELOG.md` and `workflows/NOTES.md`.
