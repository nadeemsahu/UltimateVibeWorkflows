# AI & Prompt Engineering Playbook

## Overview
This playbook provides instructions for integrating LLMs natively into the application via RAG, building agentic memory structures, and establishing automated prompt evaluation.

## 1. Retrieval-Augmented Generation (RAG) Setup

### Prompt Template
```markdown
Context:
- Vector Database: {e.g., Pinecone, Qdrant, pgvector}
- Embedding Model: {e.g., text-embedding-3-small}

Task:
1. Implement the document ingestion pipeline: parsing, chunking (overlap of 20%), and embedding generation.
2. Implement the retrieval pipeline: semantic search query generation and vector similarity scoring.
3. Scaffold the LLM synthesis wrapper that injects the retrieved context into the system prompt securely, avoiding prompt injection.
```

## 2. Agentic Memory Workflows

### Prompt Template
```markdown
Task:
1. Design an Agent Memory state machine.
2. Implement Short-Term Memory (in-session conversational context via sliding window).
3. Implement Long-Term Memory (semantic storage of user preferences and past decisions).
4. Provide the logic to conditionally retrieve from Long-Term Memory only when the entity is detected in the user's query.
```

## 3. Prompt Evaluation Loop

### Prompt Template
```markdown
Context:
- Target Prompt: {attached}
- Test Cases (Golden Dataset): {attached expected input/outputs}

Task:
1. Run an LLM-as-a-judge evaluation script.
2. Score the target prompt's output across: Accuracy, Tone, Formatting compliance, and Hallucination rate.
3. Suggest an optimized version of the Target Prompt to improve the score.
```
