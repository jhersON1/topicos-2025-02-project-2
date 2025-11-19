class LLMClient:
    def __init__(self, model: str = "mistral:7b"):
        try:
            import ollama
            self.ollama = ollama
            self.model = model
        except ImportError:
            self.ollama = None
            self.model = None

    def generate(self, prompt: str, max_tokens: int = 256, temperature: float = 0.7):
        if self.ollama:
            response = self.ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                options={"temperature": temperature, "num_predict": max_tokens, "format": "json"}
            )
            return response["message"]["content"]
        return {"error": "LLM no disponible. Instala ollama para usar el modelo."}
