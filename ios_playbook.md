# iOS Engineering Playbook

## Overview
This playbook provides iOS/Swift targeted workflows for native Apple platforms, complementing the Android ecosystem.

## 1. SwiftUI Architecture Scaffold

### Prompt Template
```markdown
Context:
- PRD: {attached}
- Target: iOS 16+, SwiftUI

Task:
1. Scaffold the core View layer using modern SwiftUI paradigms.
2. Implement the state management using `ObservableObject` or the modern `@Observable` macro.
3. Decouple domain logic from the View. Provide an `Environment` injected dependency container.
```

## 2. CoreData / SwiftData Setup

### Prompt Template
```markdown
Task:
1. Generate the SwiftData models for the following entities: {Entities}.
2. Provide a generic local storage repository that abstracts the SwiftData context.
3. Ensure background context saving is handled properly to avoid main-thread hangs.
```
