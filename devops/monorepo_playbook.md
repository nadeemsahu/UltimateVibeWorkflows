# Enterprise Monorepo Orchestration Playbook

## Overview
This playbook provides workflows for managing massive multi-package repositories (Nx, Turborepo, Lerna) safely, ensuring cross-package dependencies do not break during refactors.

## 1. Shared Package Refactoring

### Prompt Template
```markdown
Context:
- Monorepo Tool: {Nx / Turborepo}
- Target Shared Package: {e.g., `packages/ui` or `packages/core`}

Task:
1. You are modifying a shared package. Identify all downstream consuming applications.
2. Refactor the logic in the shared package as requested.
3. You MUST run the monorepo graph build command (e.g., `npx turbo run build --filter=...`) to verify that your changes did not break the downstream consumers.
4. If consumers are broken, refactor the consumers to align with the new shared package API.
```

## 2. Micro-Frontend Scaffolding

### Prompt Template
```markdown
Task:
1. Scaffold a new micro-frontend module within the existing enterprise workspace.
2. Configure the module federation plugin or workspace routing.
3. Ensure the module inherits the global linting and testing configurations from the workspace root.
```
