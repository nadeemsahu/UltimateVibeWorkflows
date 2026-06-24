Title: Live Content

Description: Fetched live

Source: https://raw.githubusercontent.com/KhazP/vibe-coding-prompt-template/main/README.md

---

<p align="center">
  <img src="https://img.shields.io/badge/Vibe--Coding-Workflow-blueviolet?style=for-the-badge&logo=rocket&logoColor=white" alt="Vibe-Coding Workflow" height="40"/>
</p>

<h3 align="center">A practical AI workflow for shipping MVPs</h3>

<p align="center">
  <strong>Turn an idea into an MVP with structured prompts, agent docs, and AI-assisted coding workflows.</strong>
</p>

<p align="center">
  Used on projects like <a href="https://vibeworkflow.app">vibeworkflow.app</a>, <a href="https://moneyvisualiser.com">moneyvisualiser.com</a>, <a href="https://caglacabaoglu.com">caglacabaoglu.com</a>, and <a href="https://alpyalay.org/realdex">RealDex App</a>.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" alt="MIT License"/></a>
  <a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"/></a>
  <a href="https://github.com/KhazP/vibe-coding-prompt-template/stargazers"><img src="https://img.shields.io/github/stars/KhazP/vibe-coding-prompt-template?style=flat-square&color=yellow" alt="Stars"/></a>
  <a href="https://github.com/KhazP/vibe-coding-prompt-template/issues"><img src="https://img.shields.io/github/issues/KhazP/vibe-coding-prompt-template?style=flat-square" alt="Issues"/></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Claude-Anthropic-orange?style=flat-square&logo=anthropic" alt="Claude"/>
  <img src="https://img.shields.io/badge/Gemini-Google-4285F4?style=flat-square&logo=google" alt="Gemini"/>
  <img src="https://img.shields.io/badge/ChatGPT-OpenAI-412991?style=flat-square&logo=openai" alt="ChatGPT"/>
  <img src="https://img.shields.io/badge/Cursor-Editor-000000?style=flat-square&logo=cursor" alt="Cursor"/>
  <img src="https://img.shields.io/badge/VS_Code-Microsoft-007ACC?style=flat-square&logo=visualstudiocode" alt="VS Code"/>
</p>

---

## Table of contents
- [Built with this workflow](#built-with-this-workflow)
- [Workflow overview](#workflow-overview)
- [Quick start and the 5 steps](#quick-start-and-the-5-steps)
- [Prerequisites and tools](#prerequisites-and-tools)
- [Advanced agent practices](#advanced-agent-practices)
- [Project structure and deployment](#project-structure-and-deployment)
- [Common pitfalls and troubleshooting](#common-pitfalls-and-troubleshooting)
- [Further reading](#further-reading)

---

## Built with this workflow

This repo documents the workflow behind a handful of shipped projects. The goal is simple: do the thinking upfront, hand clean context to your tools, and keep the build phase moving.

| Project | What it is |
| :-- | :-- |
| [vibeworkflow.app](https://vibeworkflow.app) | An interactive web app built around the same structured vibe-coding workflow documented here. |
| [moneyvisualiser.com](https://moneyvisualiser.com) | A money visualization website that visualized money in a 3D environment. |
| [caglacabaoglu.com](https://caglacabaoglu.com) | A production portfolio and gallery site built with the same PRD-to-agent execution approach. |
| [alpyalay.org/realdex](https://alpyalay.org/realdex) | A mobile app built on React Native that lets you catch animals, and put them in a Pokemon-like collection. |

<p align="center">
  <sub>Maintained by <a href="https://x.com/alpyalay">Alp Yalay</a>.</sub>
</p>

---

## Workflow overview

The process moves through five stages, from idea validation to working code:

```mermaid
flowchart LR
    subgraph Phase1[" "]
        A[💡 Idea]
    end

    subgraph Phase2["Research"]
        B[📊 Market Analysis]
    end

    subgraph Phase3["Define"]
        C[📋 PRD]
    end

    subgraph Phase4["Design"]
        D[🏗️ Tech Design]
    end

    subgraph Phase5["Generate"]
        E[🤖 AGENTS.md]
    end

    subgraph Phase6["Build"]
        F[🚀 MVP]
    end

    A --> B --> C --> D --> E --> F

    style A fill:#667eea,stroke:#667eea,color:#fff
    style B fill:#764ba2,stroke:#764ba2,color:#fff
    style C fill:#f093fb,stroke:#f093fb,color:#fff
    style D fill:#4facfe,stroke:#4facfe,color:#fff
    style E fill:#00f2fe,stroke:#00f2fe,color:#000
    style F fill:#43e97b,stroke:#43e97b,color:#000
```

<p align="center">
  <a href=".claude/README.md">
    <img src="https://img.shields.io/badge/Using_Claude_Code%3F-Click_here_for_built--in_skills-667eea?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code Skills"/>
  </a>
  <a href="https://vibeworkflow.app/#/vibe-coding">
    <img src="https://img.shields.io/badge/Try_the_Website-Open_Vibe--Coding_Webapp-43e97b?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Vibe-Coding Website"/>
  </a>
</p>

---

## Quick start and the 5 steps

> TL;DR: run research, turn it into a PRD, choose the stack, generate your agent files, then build in small passes.

### Phase 1: thinking through the product
Do the first three steps in ChatGPT, Claude.ai, Gemini, or any other chat tool. You do not need a repo yet.

### ![Step 1](https://img.shields.io/badge/Step_1-Deep_Research-764ba2?style=flat-square) Deep Research
<details open>
<summary><b>Check whether the idea is worth building</b> - 20-30 min</summary>

This step gives you a quick read on demand, competitors, and whether the scope looks realistic.

1. Open [`part1-deepresearch.md`](part1-deepresearch.md) and **copy all of its contents**.
2. **Paste it** into your preferred AI platform Chat (like Claude.ai, ChatGPT, or Gemini) and press **Enter**.
3. The AI will ask you a few questions about your idea. Answer them truthfully in the chat.
4. The AI will generate a comprehensive research document based on your answers.
5. **Save the output** into a local file named `research-[YourAppName].md` (or `.txt`) or simply **keep this chat open** for Step 2.

Tip: if your chat tool supports web search, turn it on so the stats and competitor references are current.
</details>

### ![Step 2](https://img.shields.io/badge/Step_2-Product_Requirements-f093fb?style=flat-square) Product Requirements (PRD)
<details open>
<summary><b>Write down what the MVP actually needs to do</b> - 15-20 min</summary>

This turns the rough idea into a scope you can build against.

1. Copy the contents of [`part2-prd-mvp.md`](part2-prd-mvp.md).
2. **Option A (Same Chat):** If you kept your chat open, paste the prompt right below the Deep Research output.
3. **Option B (New Chat):** Start a fresh chat, paste your saved `research-[YourAppName].md` content, and then paste the Part 2 prompt below it.
4. Press Enter, answer any clarifying questions the AI asks, and let it generate your requirements.
5. **Save the final output** as `PRD-[YourAppName]-MVP.md`.
</details>

### ![Step 3](https://img.shields.io/badge/Step_3-Technical_Design-4facfe?style=flat-square) Technical Design
<details open>
<summary><b>Pick a stack you can actually ship with</b> - 15-20 min</summary>

This step helps you choose the stack 

