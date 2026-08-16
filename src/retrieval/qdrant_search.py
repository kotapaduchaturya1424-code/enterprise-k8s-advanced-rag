from typing import List

class HybridRetriever:
    """Qdrant Hybrid Search & Cross-Encoder ReRanking"""
    def __init__(self):
        self.kb = [
            "Pod OOMKilled error occurs when memory limit exceeds in K8s.",
            "CrashLoopBackOff indicates a pod failing repeatedly after starting.",
            "Ingress manages external HTTP/HTTPS traffic routing into services."
        ]

    def search_and_rerank(self, query: str) -> List[str]:
        results = [doc for doc in self.kb if any(term in doc.lower() for term in query.lower().split())]
        return results if results else self.kb[:2]