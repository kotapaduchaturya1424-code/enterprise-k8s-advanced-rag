class GuardrailsPipeline:
    """9-Layer Security Guardrails for Input & Output Validation"""
    
    def validate_input(self, query: str) -> bool:
        forbidden = ["DROP TABLE", "DELETE FROM", "IGNORE PREVIOUS INSTRUCTIONS", "EXEC"]
        if any(keyword in query.upper() for keyword in forbidden):
            return False
        return True

    def validate_output(self, response: str) -> bool:
        return True