class FacebookAdapter:
    def build_prompt(self, title, body):
        return f"""
        Eres un experto en marketing digital. Genera un post para Facebook usando el siguiente título y contenido:
        Título: {title}
        Contenido: {body}
        Reglas:
        - Usa tono casual y emojis.
        - Incluye 3-5 hashtags relevantes.
        - Limita el texto a 250 caracteres.
        El resultado debe ser un JSON con las claves: text, hashtags, character_count.
        """
