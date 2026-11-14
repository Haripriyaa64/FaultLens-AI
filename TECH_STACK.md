# FaultLens AI – Technology Stack

## 1. Frontend
- React
- TypeScript
- Vite
- Tailwind CSS

## 2. Backend
- Python 3.11
- FastAPI

## 3. Database and Storage
- PostgreSQL
- pgvector
- SQLAlchemy
- Alembic
- Local file storage (initial implementation)

## 4. AI and Machine Learning
- PyTorch
- Sentence Transformers
- BAAI/bge-base-en-v1.5 (initial embedding model candidate)
- Cross-Encoder for reranking

## 5. Retrieval and RAG
- PostgreSQL Full-Text Search
- pgvector similarity search
- Hybrid retrieval
- Custom Python RAG pipeline

## 6. Agent Orchestration
- LangGraph
- Triage Agent
- Log Analysis Agent
- Root Cause Analysis Agent
- Duplicate Detection Agent
- Remediation Agent

## 7. Background Processing
- Celery
- Redis

## 8. Testing
- Pytest
- Vitest

## 9. Deployment and Development Tools
- Docker
- Docker Compose
- Git
- GitHub
- GitHub Actions

## 10. LLM Integration
A provider-independent LLM integration layer will be developed. The final LLM provider and model will be selected after evaluating reasoning quality, structured output, latency, cost and availability.

## Note
This is the proposed technology stack for FaultLens AI. Technologies and model choices will be validated during implementation and testing.
