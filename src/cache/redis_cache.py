class RedisSemanticCache:
    """Simulated Redis Cache Layer"""
    def __init__(self):
        self.memory_store = {}

    def get(self, key: str):
        return self.memory_store.get(key)

    def set(self, key: str, value: str):
        self.memory_store[key] = value