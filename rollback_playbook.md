# Rollback & Disaster Recovery Playbook

## Overview
This playbook governs how Agents respond to catastrophic failures, broken deployments, or corrupted main branches. Agents MUST execute these workflows instead of attempting ad-hoc fixes if production is blocked.

## 1. Git Revert & State Rollback

### Prompt Template
```markdown
Context:
- Broken Commit SHA: {attached}
- Error Logs: {attached}

Task:
1. The recent feature merge broke the build. Execute a clean `git revert` of the broken commit.
2. Resolve any merge conflicts that arise from the revert locally.
3. Push the reverted state to restore the `main` branch to green.
4. Update `BUG_GRAPH.json` to reopen the bugs that were supposedly fixed by the reverted commit.
```

## 2. Database Down-Migration

### Prompt Template
```markdown
Context:
- Target Schema: {attached}
- Broken Migration File: {attached}

Task:
1. The recent schema migration failed or corrupted data.
2. Write and execute the exact down-migration script (e.g., `DROP COLUMN`, `RESTORE FROM BACKUP`) to return the schema to its previous version.
3. Validate that the application can successfully boot against the rolled-back schema.
```
