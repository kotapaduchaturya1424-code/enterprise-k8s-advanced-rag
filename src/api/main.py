from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.security.pipeline import GuardrailsPipeline
from src.cache.redis_cache import RedisSemanticCache
from src.graph.workflow import rag_graph

app = FastAPI(title="Enterprise K8s Advanced RAG API")
guardrails = GuardrailsPipeline()
cache = RedisSemanticCache()

class QueryRequest(BaseModel):
    query: str

@app.post("/api/v1/chat")
def chat_endpoint(request: QueryRequest):
    if not guardrails.validate_input(request.query):
        raise HTTPException(status_code=400, detail="Input query failed security guardrails.")

    cached_val = cache.get(request.query)
    if cached_val:
        return {"source": "cache", "response": cached_val}

    graph_out = rag_graph.invoke({"query": request.query})
    response_text = graph_out.get("generation", "No answer produced.")

    cache.set(request.query, response_text)
    return {"source": "langgraph_engine", "response": response_text}