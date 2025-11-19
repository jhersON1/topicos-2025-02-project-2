class WhatsAppAdapter:
    def build_prompt(self, title, body):
        """
        Prompt WhatsApp:
        Eres un experto en comunicación directa. Genera un mensaje para WhatsApp usando el siguiente título y contenido:
        Título: {title}
        Contenido: {body}
        Reglas:
        - Sé breve, claro y directo.
        - Usa lenguaje informal y cercano.
        - Limita el texto a 80 caracteres.
        El resultado debe ser un JSON con las claves: text, character_count.
        """
        return f"""
        Eres un experto en comunicación directa. Genera un mensaje para WhatsApp usando el siguiente título y contenido:
        Título: {title}
        Contenido: {body}
        Reglas:
        - Sé breve, claro y directo.
        - Usa lenguaje informal y cercano.
        - Limita el texto a 80 caracteres.
        El resultado debe ser un JSON con las claves: text, character_count.
        """
