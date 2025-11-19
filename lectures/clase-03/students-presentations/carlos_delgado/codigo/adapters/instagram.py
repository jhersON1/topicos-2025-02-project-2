class InstagramAdapter:
    def build_prompt(self, title, body):
        return f"""
        Eres un creador de contenido visual. Genera un caption para Instagram usando el siguiente título y contenido:
        Título: {title}
        Contenido: {body}
        Reglas:
        - Usa muchos emojis y tono creativo.
        - Incluye 3-5 hashtags y un prompt para imagen generativa.
        - Limita el texto a 180 caracteres.
        El resultado debe ser un JSON con las claves: text, hashtags, image_prompt, character_count.
        """
