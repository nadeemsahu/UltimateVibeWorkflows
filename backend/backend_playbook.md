# Backend & Database Engineering Playbook

## Overview
This playbook guides AI Agents in designing robust backend architectures, writing secure API contracts, and orchestrating relational or NoSQL database schemas.

## 1. Database Schema Generation

### Prompt Template
```markdown
Context:
- Project PRD: {attached}
- Target DB: {e.g., PostgreSQL, MongoDB, DynamoDB}

Task:
1. Design a normalized (or appropriately denormalized) database schema supporting the core user stories.
2. Provide the schema definition in the target ORM/Migration language (e.g., Prisma, Flyway SQL, Liquibase).
3. Ensure primary keys are UUIDs, and include created_at/updated_at timestamps on all entities.
4. Document all indexes required for the anticipated query patterns.
```

## 2. API Contract Setup (OpenAPI/gRPC)

### Prompt Template
```markdown
Context:
- Database Schema: {attached}
- User Stories: {attached}

Task:
1. Design the API layer to support the frontend requirements.
2. If REST: Output a strict OpenAPI 3.0 specification covering all endpoints, requests, and responses.
3. If gRPC: Output the `.proto` files with clear message definitions.
4. Ensure all endpoints require appropriate authentication tokens and validate input.
```

## 3. Server Logic & Controller Architecture

### Prompt Template
```markdown
Implement the controller logic for the {Feature} endpoint.

Rules:
- Strictly separate routing logic, business domain logic, and data access (Repository pattern).
- Use dependency injection for all external services.
- Never swallow exceptions; normalize errors through a global error handler that returns standardized API error responses.
- Write unit tests for the business logic layer immediately after implementation.
```
