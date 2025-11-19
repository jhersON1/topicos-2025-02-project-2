class LinkedInAdapter:
    def build_prompt(self, title, body):
        return f"""
        Eres un profesional de negocios. Genera un post para LinkedIn usando el siguiente título y contenido:
        Título: {title}
        Contenido: {body}
        Reglas:
        - Usa tono formal y profesional.
        - No uses emojis, o muy pocos y discretos.
        - Limita el texto a 500 caracteres.
        El resultado debe ser un JSON con las claves: text, hashtags, character_count, tone.
        """
