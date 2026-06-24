# QA Automation & E2E Testing Playbook

## Overview
This playbook transitions a project from basic unit tests to highly resilient, automated End-to-End (E2E) and Performance testing pipelines.

## 1. E2E Browser / Mobile Testing

### Prompt Template
```markdown
Context:
- Framework: {Playwright / Cypress / Appium}
- Core User Journey: {e.g., User logs in, adds item to cart, checks out}

Task:
1. Write an E2E test script covering the Happy Path.
2. Do NOT rely on fragile CSS selectors or XPaths. Use data-testid or accessible ARIA roles exclusively.
3. Include explicit wait strategies for network requests to prevent flaky tests.
4. Scaffold the teardown logic to clean up any database state created by the test.
```

## 2. Load & Performance Testing

### Prompt Template
```markdown
Context:
- Target endpoint: `/api/v1/checkout`
- Tool: {k6 / Gatling / Locust}

Task:
1. Write a load testing script simulating 1,000 concurrent virtual users (VUs) over a 5-minute ramp-up period.
2. Add assertions to ensure P95 response times remain under 200ms.
3. Assert that the error rate remains under 1%.
```

## 3. Chaos Engineering / Failure Injection

### Prompt Template
```markdown
Task:
1. Design a test suite that deliberately injects network latency (e.g., 5-second delay) and random 500 errors into the API layer.
2. Assert that the frontend UI gracefully degrades, displays appropriate error states/skeletons, and allows user retries without crashing.
```
