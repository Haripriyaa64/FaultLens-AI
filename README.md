# FaultLens AI
### Intelligent Bug Diagnosis & Fix Recommendation Platform

FaultLens AI is an AI-powered platform designed to help developers analyze software bugs, identify probable root causes, detect duplicate defects, and receive intelligent fix recommendations.

The platform combines Retrieval-Augmented Generation (RAG), semantic search, vector embeddings, and multi-agent AI workflows to make software debugging more efficient and evidence-driven.

## 🎯 Project Objective

To develop an intelligent bug diagnosis system that analyzes bug reports, stack traces, and error logs, retrieves relevant historical defects, and generates context-aware recommendations to assist developers in resolving software issues.

## ✨ Key Features

- **Intelligent Bug Analysis:** Analyze bug descriptions, stack traces, and error logs.
- **Root Cause Detection:** Identify probable causes of software defects.
- **Duplicate Bug Detection:** Find semantically similar historical bug reports.
- **AI Fix Recommendations:** Suggest potential solutions based on retrieved evidence.
- **Historical Defect Knowledge Base:** Build a searchable collection of public software defect reports.
- **Multi-Agent Architecture:** Use specialized AI agents for different diagnosis tasks.

## 🏗️ Proposed Architecture

Developer → React Frontend → FastAPI Backend → Bug Processing Pipeline → AI Intelligence Engine → Diagnosis Results

The AI Intelligence Engine consists of:

1. Triage Agent
2. Log Analysis Agent
3. Root Cause Analysis Agent
4. Duplicate Detection Agent
5. Remediation Agent

The system will use RAG to retrieve relevant historical defects and provide evidence-backed recommendations.

## 🛠️ Proposed Technology Stack

| Technology | Purpose |
|---|---|
| React + TypeScript | Frontend |
| Tailwind CSS | UI styling |
| Python + FastAPI | Backend APIs |
| PostgreSQL + pgvector | Database and vector search |
| Redis + Celery | Background processing |
| Sentence Transformers | Text embeddings |
| LangGraph | Multi-agent orchestration |
| PyTorch | Machine learning |
| Docker | Containerization |
| Pytest | Backend testing |

## 🔄 Proposed Workflow

1. Developer submits a bug report, stack trace, or log file.
2. System validates and processes the submitted information.
3. Triage and log analysis agents examine the issue.
4. Historical defect knowledge base is searched using semantic retrieval.
5. Root cause and duplicate detection agents analyze the results.
6. Remediation agent generates potential fix recommendations.
7. Diagnosis results and supporting evidence are presented to the developer.

## 📚 Planned Historical Data Sources

- Mozilla Bugzilla
- Apache Jira
- Eclipse Bugzilla
- Public software defect datasets

## 📁 Initial Project Structure

```text
FaultLens-AI/
│
├── frontend/
├── backend/
├── ai_engine/
├── datasets/
├── infrastructure/
├── docs/
├── tests/
│
├── README.md
├── SYSTEM_ARCHITECTURE.md
├── TECH_STACK.md
├── DEVELOPMENT_ROADMAP.md
└── .gitignore
```

## 🚀 Development Status

**Current Phase:** Project Planning and Architecture Design

The platform is under active development. Features and architecture described above represent the proposed implementation.


## 📌 Vision

To make software debugging smarter, faster, and more reliable through AI-powered defect intelligence.

---

*Built as part of the Infosys Internship Project.*
