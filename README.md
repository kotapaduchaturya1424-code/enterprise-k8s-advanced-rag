# Enterprise Advanced RAG for Kubernetes IT Operations

Production-grade Enterprise RAG system designed for Kubernetes SRE Copilot using LangGraph, FastAPI, Qdrant, PostgreSQL, and Redis.

## How to Run
1. Start Services: `docker-compose up -d`
2. Activate Virtual Env & Install: `pip install -r requirements.txt`
3. Run API: `python -m uvicorn src.api.main:app --reload`
4. Run UI: `streamlit run src/ui/app.py`