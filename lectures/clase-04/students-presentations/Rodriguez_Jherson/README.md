# Clase 3 - Prototipo de Adaptación con LLM
**Fecha:** Jueves 13 de noviembre de 2025

---

## Objetivos de la clase

- Implementar sistema de adaptación de contenido usando LLM
- Diseñar prompts específicos para cada red social
- Validar transformaciones de texto y límites de caracteres
- Preparar módulo reutilizable para integración con APIs

---

## Entregables de HOY

### 1️⃣ Exposición 

**Debes presentar:**
1. LLM seleccionado y justificación
2. Arquitectura del sistema
3. Estrategia de prompts para cada red
4. Challenges encontrados y soluciones

**Formato:**
- Slides o presentación visual
- Diagramas de flujo
- Ejemplos de prompts

### 2️⃣ Código + Demo 

#### Sistema funcionando

Tu sistema debe recibir un input y generar adaptaciones para las 5 redes:

**Input:**
```json
{
  "titulo": "Nueva funcionalidad en nuestra plataforma",
  "contenido": "Hoy lanzamos una nueva característica que permite...",
  "target_networks": ["facebook", "instagram", "linkedin", "tiktok", "whatsapp"]
}
```

**Output esperado:**
```json
{
  "facebook": {
    "text": "🎉 Gran noticia...",
    "hashtags": ["#Innovación", "#Tecnología"],
    "character_count": 245,
    "tone": "casual"
  },
  "instagram": {
    "text": "✨ Nueva función...",
    "hashtags": ["#Tech", "#Innovation", "#NewFeature"],
    "character_count": 180,
    "suggested_image_prompt": "Modern tech interface..."
  },
  "linkedin": {
    "text": "Nos complace anunciar...",
    "hashtags": ["#Innovation", "#Technology"],
    "character_count": 320,
    "tone": "professional"
  },
  "tiktok": {
    "text": "🔥 LO QUE ESPERABAS...",
    "hashtags": ["#TechTok", "#Innovation", "#NewFeature"],
    "character_count": 150,
    "tone": "energetic"
  },
  "whatsapp": {
    "text": "Hola! Te contamos sobre nuestra nueva función...",
    "character_count": 200,
    "tone": "personal"
  }
}
```

#### Requisitos técnicos:

- ✅ **Funcionalidad completa** para las 5 redes
- ✅ **Validación de límites** de caracteres por red
- ✅ **Manejo de errores** del LLM (timeout, API down, etc.)
- ✅ **Logging básico** de las llamadas
- ✅ **Código modular** y reutilizable

#### Documentación necesaria:

En `/docs/prompts.md`:
- Prompt system para cada red social
- Variables de temperatura y parámetros
- Iteraciones realizadas (v1 → v2 → v3)
- Justificación de decisiones

#### Casos de prueba (mínimo 3):

Debes demostrar tu sistema con estos escenarios:
1. **Noticia corporativa formal**
2. **Anuncio de producto/servicio**
3. **Invitación a evento**

### Demo en vivo (OBLIGATORIO)

Durante tu presentación debes:
1. Mostrar el código funcionando
2. Input → LLM → Output en tiempo real
3. Explicar diferencias en las adaptaciones
4. Mostrar qué pasa si hay errores
5. Verificar límites de caracteres

---

## Formato de entrega

### Estructura de tu carpeta:

```
lectures/clase-03/students-presentations/[tu-nombre]/
├── README.md
├── src/
│   └── llm_adapter.py (o .ts/.js)
├── docs/
│   ├── prompts.md
│   └── desarrollo.md
├── tests/ (opcional pero recomendado)
├── .env.example
└── presentacion.pdf (o .pptx)
```

### En tu README.md debe incluir:

- Descripción del sistema
- LLM utilizado y por qué
- Instrucciones de instalación
- Cómo ejecutar
- Ejemplos de uso
- Variables de entorno necesarias

---


## Características de cada red social (referencia)

| Red | Max Chars | Tono | Hashtags | Emojis | Formato |
|-----|-----------|------|----------|--------|---------|
| **Facebook** | ~63,206 (práctico: 300-500) | Casual, conversacional | 2-3 | ✅ Sí | Párrafos, links |
| **Instagram** | 2,200 | Visual, inspiracional | 10-30 | ✅✅ Muchos | Líneas cortas, emojis |
| **LinkedIn** | 3,000 | Profesional, formal | 3-5 | ⚠️ Moderado | Párrafos, bullets |
| **TikTok** | 2,200 | Energético, trending | 3-5 | ✅ Sí | Corto, call-to-action |
| **WhatsApp** | 4,096 (práctico: 200-300) | Personal, directo | 0-1 | ⚠️ Moderado | Conversacional |

---

## Recursos útiles

### Documentación de LLMs:
- **OpenAI:** https://platform.openai.com/docs
- **Anthropic (Claude):** https://docs.anthropic.com
- **Ollama:** https://ollama.ai/docs

### Guías de prompt engineering:
- Anthropic Prompt Library: https://docs.anthropic.com/en/prompt-library/library
- OpenAI Prompt Engineering Guide: https://platform.openai.com/docs/guides/prompt-engineering

### Testing:
- Postman: Para probar tu API
- Insomnia: Alternativa a Postman

---

## Tips para la demo

### ✅ Antes de presentar:
- Prueba tu demo al menos 2 veces
- Verifica que tu API key funciona
- Ten casos de prueba preparados
- Prepara plan B si el LLM falla (screenshots de respuestas previas)
- Asegura buena conexión a internet

### ⚠️ Errores comunes a evitar:
- No especificar idioma en el prompt (responde en inglés)
- No validar límites de caracteres
- Prompts genéricos (todas las redes iguales)
- No manejar timeouts del LLM
- Commitear API keys en Git

### 💡 Pro tips:
- Usa ejemplos (few-shot learning) en tus prompts
- Pide formato JSON para parsear más fácil
- Implementa retry si el LLM falla
- Cachea respuestas para ahorrar llamadas
- Mide el tiempo de respuesta

---

## Preguntas frecuentes

**P: ¿Qué LLM debo usar?**
R: Puedes usar OpenAI (gpt-3.5-turbo, gpt-4o-mini), Claude (Sonnet, Haiku), o Ollama (Llama 3.1). Lo importante es justificar tu elección.

**P: ¿Tengo que publicar en las redes reales hoy?**
R: NO. Hoy solo generas el texto adaptado. La publicación real será en Clase 4.

**P: ¿Qué pasa si mi API key se agota?**
R: Ten screenshots/ejemplos de backup. Documenta el intento. Considera usar Ollama (gratis, local).

**P: ¿Puedo usar librerías adicionales?**
R: Sí, pero documenta la instalación en tu README.

**P: ¿Tests son obligatorios?**
R: No obligatorios, pero son un plus y facilitan validar que funciona.

---

## 📢 IMPORTANTE: Tarea para Clase 4

Al final de la clase se explicará la tarea para el **Martes 19 de noviembre**.

**Adelanto:** Integrarás tu sistema con las APIs reales de:
- Facebook
- Instagram
- LinkedIn

Deberás hacer publicaciones REALES de prueba. Empieza a crear tus apps de desarrollador este fin de semana.

---

## Soporte

Si tienes dudas:
1. Revisa la documentación oficial del LLM que elegiste
2. Consulta el archivo `TAREAS-Y-ENTREGABLES.md`
3. Pregunta en el horario de consultas del docente

---

¡Buena suerte! 🚀
