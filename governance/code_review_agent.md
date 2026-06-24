# Code Review Agent Playbook

## Overview
This playbook runs an autonomous Agent that strictly acts as a Code Reviewer, checking PRs or generated code against the master `AGENTS.md` guidelines.

## 1. Automated PR Critique

### Prompt Template
```markdown
Context:
- `workflows/AGENTS.md` (Master Guidelines)
- Proposed Code Diff: {attached}

Task:
You are the Principal Architect. Review the diff strictly against the Master Guidelines.
1. Fail the review if there are architectural violations (e.g., UI touching data layers directly).
2. Fail the review if forceful unwrapping is used without structural proof.
3. Fail the review if there are missing unit tests for new business logic.
4. Output a formatted PR Review with inline comments for the authoring Agent to fix.
```
