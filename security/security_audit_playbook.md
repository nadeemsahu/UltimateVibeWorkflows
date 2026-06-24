# Security Audit & Code Review Playbook

## Overview
This playbook is used by Agents acting in a "Security Auditor" role to systematically verify code integrity, cryptography, and vulnerability mitigation.

## 1. Automated Dependency Audit

### Prompt Template
```markdown
Context:
- Package file: `package.json` / `build.gradle` / `go.mod`

Task:
1. Scan the dependencies for known CVEs or heavily deprecated packages.
2. Identify dependencies that request excessive permissions.
3. Recommend exact version bumps to resolve identified issues.
```

## 2. Injection & Flaw Checklist Review

### Prompt Template
```markdown
Context:
- Target files: {List of recently modified files handling user input or DB queries}

Task:
Review the code for the following OWASP Top 10 vulnerabilities:
- [ ] SQL/NoSQL Injection: Are parameterized queries strictly enforced?
- [ ] XSS: Is all user-generated content sanitized before rendering?
- [ ] Broken Access Control: Do API endpoints verify the user's authority over the requested resource ID?
- [ ] CSRF: Are anti-CSRF tokens implemented on state-mutating endpoints?

Output a detailed audit report. If a vulnerability is found, provide the exact code diff to patch it.
```

## 3. Cryptography & Storage Audit

### Prompt Template
```markdown
Context:
- Application handling sensitive data (e.g., PII, Tokens, NFC Payloads).

Task:
1. Verify that sensitive data is NEVER written to standard SharedPreferences or local storage without AES256-GCM encryption.
2. Ensure HTTPS/TLS 1.2+ is enforced on all network boundaries.
3. Verify that passwords or keys are not hardcoded anywhere in the repository.
```
