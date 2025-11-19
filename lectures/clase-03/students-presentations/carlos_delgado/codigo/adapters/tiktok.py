class TikTokAdapter:
    def build_prompt(self, title, body):
        """
        Prompt TikTok:
        Eres un creador de contenido viral. Genera un caption para TikTok usando el siguiente título y contenido:
        Título: {title}
        Contenido: {body}
        Reglas:
        - Sé breve, creativo y usa hashtags virales.
        - Incluye sugerencia de música o efecto visual.
        - Limita el texto a 100 caracteres.
        El resultado debe ser un JSON con las claves: text, hashtags, music_suggestion, character_count.
        """
        return f"""
        Eres un creador de contenido viral. Genera un caption para TikTok usando el siguiente título y contenido:
        Título: {title}
        Contenido: {body}
        Reglas:
        - Sé breve, creativo y usa hashtags virales.
        - Incluye sugerencia de música o efecto visual.
        - Limita el texto a 100 caracteres.
        El resultado debe ser un JSON con las claves: text, hashtags, music_suggestion, character_count.
        """
