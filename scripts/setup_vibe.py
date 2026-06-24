import os
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))
dest_root = os.path.join(script_dir, "..", "..")
src_templates = os.path.join(dest_root, "temp_repo", "templates")
dest_workflows = os.path.join(dest_root, "workflows")
os.makedirs(dest_workflows, exist_ok=True)
dest_agent_docs = os.path.join(dest_workflows, "agent_docs")
os.makedirs(dest_agent_docs, exist_ok=True)

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# 1. AGENTS.md
agents_md = read_file(os.path.join(src_templates, "AGENTS.md"))
agents_md = agents_md.replace("[App Name]", "LibraryNFC")
agents_md = agents_md.replace("[One-paragraph description of the project, its core value proposition, and primary users]", "A modern Android application emulating NXP MIFARE DESFire-based library ID cards using Host Card Emulation (HCE), targeting library members requiring digital card access and a flagship-tier UI/UX.")
agents_md = agents_md.replace("[Primary Tech Stack, e.g., Next.js, React, Node, PostgreSQL]", "Android, Kotlin, Coroutines, StateFlow, Hilt, Glassmorphism UI")
agents_md = agents_md.replace("[e.g., Mobile-first design required, Multi-tenant architecture, Strict TypeScript adherence]", "Android API 31+ required for RenderEffect, strict separation of domain and UI via Clean Architecture, Coroutines for asynchronous work.")
agents_md = agents_md.replace("[npm install / pnpm install]", "./gradlew build")
agents_md = agents_md.replace("[npm run dev]", "./gradlew installDebug")
agents_md = agents_md.replace("[npm test]", "./gradlew test")
agents_md = agents_md.replace("[npm run lint]", "./gradlew lint")
agents_md = agents_md.replace("[npm run build]", "./gradlew assembleRelease")

write_file(os.path.join(dest_workflows, "AGENTS.md"), agents_md)

# 2. MEMORY.md
memory_md = read_file(os.path.join(src_templates, "MEMORY.md"))
memory_md = memory_md.replace("e.g., Complete active component or specific route", "e.g., Complete active ViewModel or specific Fragment")
memory_md = memory_md.replace("e.g., Chose Zustand over Redux for local component state to reduce boilerplate.", "e.g., Chose StateFlow over LiveData for ViewModel state to improve testing.")
memory_md = memory_md.replace("e.g., API route X occasionally fails due to rate limits from Third Party Y", "e.g., NFC transceiver occasionally fails due to timing issues on Pixel devices")
memory_md = memory_md.replace("e.g., Database seed script must be run with command Z to avoid PK conflicts", "e.g., EncryptedSharedPreferences requires API 23+")
memory_md = memory_md.replace("- [ ] Database schema creation", "- [ ] Room database schema creation")
write_file(os.path.join(dest_workflows, "MEMORY.md"), memory_md)

# 3. REVIEW-CHECKLIST.md
review_md = read_file(os.path.join(src_templates, "REVIEW-CHECKLIST.md"))
review_md = review_md.replace("No `any` types used (or strictly justified with `unknown` and type guards).", "No forceful unwrapping (`!!`) used unless structurally guaranteed.")
review_md = review_md.replace("Linter passes (`npm run lint` or equivalent).", "Linter passes (`./gradlew lint` or equivalent).")
review_md = review_md.replace("Type check passes (`tsc --noEmit` or equivalent).", "Build passes (`./gradlew assembleDebug` or equivalent).")
write_file(os.path.join(dest_workflows, "REVIEW-CHECKLIST.md"), review_md)

# 4. agent_docs
src_agent_docs = os.path.join(src_templates, "agent_docs")
for file_name in os.listdir(src_agent_docs):
    src_path = os.path.join(src_agent_docs, file_name)
    if os.path.isfile(src_path):
        content = read_file(src_path)
        
        if file_name == "tech_stack.md":
            content = content.replace("[Framework and version, e.g., Next.js 15 App Router]", "Android SDK (API 31+), Kotlin")
            content = content.replace("[Framework and version, e.g., Node.js / Express]", "Clean Architecture with Hilt / Coroutines / StateFlow")
            content = content.replace("[Database version / ORM, e.g., PostgreSQL with Drizzle ORM]", "EncryptedSharedPreferences (AES256-GCM)")
            content = content.replace("[Library, e.g., Tailwind CSS + shadcn/ui]", "Vanilla Android XML + Glassmorphism / RenderEffect")
            content = content.replace("[Tool, e.g., Supabase Auth or NextAuth]", "Android BiometricPrompt API")
            
        elif file_name == "product_requirements.md":
            content = content.replace("[Insert full product requirements, user stories, and acceptance criteria from your PRD.]", read_file(os.path.join(dest_root, "context", "PRD.md")))
            
        elif file_name == "project_brief.md":
            content = content.replace("[Insert core vision, conventions, and key setup commands here.]", read_file(os.path.join(dest_root, "context", "PROJECT.md")))
            
        elif file_name == "testing.md":
            content = content.replace("[Tool, e.g., Vitest]", "JUnit4 / Mockito / kotlinx-coroutines-test")
            content = content.replace("[Tool, e.g., Playwright]", "Espresso / Robolectric")
            content = content.replace("[npm run test]", "./gradlew test")
            content = content.replace("Command to run all tests: `[Command]`", "Command to run all tests: `./gradlew test`")
            content = content.replace("Command to run a single test file: `[Command pattern]`", "Command to run a single test file: `./gradlew testDebugUnitTest --tests \"*MyTestClass\"`")
            
        write_file(os.path.join(dest_agent_docs, file_name), content)

# 5. Tool config (GEMINI.md for Antigravity)
gemini_config = """# GEMINI.md — Gemini CLI / Agent-First IDE Configuration for LibraryNFC

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
"""
write_file(os.path.join(dest_workflows, "GEMINI.md"), gemini_config)

print("Vibe-coding workflow instantiated successfully.")
