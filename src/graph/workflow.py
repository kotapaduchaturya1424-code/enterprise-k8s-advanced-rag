from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from src.retrieval.qdrant_search import HybridRetriever

retriever = HybridRetriever()

class AgentState(TypedDict):
    query: str
    documents: List[str]
    generation: str

def hyde_and_retrieve_node(state: AgentState):
    query = state["query"]
    docs = retriever.search_and_rerank(query)
    return {"documents": docs}

def generate_node(state: AgentState):
    docs = state.get("documents", [])
    context = "\n".join(docs)
    answer = f"K8s Copilot Analysis:\nContext:\n{context}\n\nRecommended Action: Verify pod resource limits."
    return {"generation": answer}

builder = StateGraph(AgentState)
builder.add_node("retrieve", hyde_and_retrieve_node)
builder.add_node("generate", generate_node)

builder.set_entry_point("retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

rag_graph = builder.compile()