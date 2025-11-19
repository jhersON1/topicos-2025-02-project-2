

# Social Content LLM

Genera contenido adaptado automáticamente para Facebook, Instagram, LinkedIn, TikTok y WhatsApp usando un modelo de lenguaje (LLM) como Mistral-7B vía Ollama.

## ¿Qué hace este sistema?
Permite crear publicaciones personalizadas para 5 redes sociales a partir de un contenido original, usando inteligencia artificial. Solo envía el título, el contenido base y la red social destino, y el sistema generará el post ideal según las reglas y el estilo de cada plataforma.

## Entregables requeridos
- Sistema funcionando localmente
- Adaptación para Facebook, Instagram, LinkedIn, TikTok y WhatsApp
- Documentación de prompts utilizados
- Demo en vivo con 3 casos de prueba
- Exposición de 15 minutos sobre el desarrollo

## Estructura del proyecto
```
social_content_llm/
  api.py                # API principal con FastAPI
  content_engine.py     # Motor que gestiona prompts y generación
  llm_client.py         # Cliente para interactuar con el modelo LLM
  adapters/             # Adaptadores para cada red social (Facebook, Instagram, LinkedIn, TikTok, WhatsApp)
  requirements.txt      # Dependencias del proyecto
  README.md             # Documentación
```

## Instalación y ejecución
1. Instala las dependencias:
   ```bash
   pip install -r social_content_llm/requirements.txt
   ```
2. (Opcional) Instala Ollama y descarga el modelo Mistral-7B si quieres usar el LLM real:
   - [Ollama instalación](https://ollama.com/)
   - Descarga el modelo: `ollama pull mistral:7b`
3. Ejecuta la API en modo desarrollo:
   ```bash
   uvicorn social_content_llm.api:app --reload
   ```

## Cómo usar la API
Haz una petición POST a `/generate` con el siguiente JSON:
```json
{
  "title": "Lanzamiento de nuevo producto",
  "body": "Hoy presentamos nuestra nueva línea de productos...",
  "network": "facebook"
}
```

La respuesta será un JSON con el contenido generado para la red social elegida.


## Adaptadores disponibles
- **facebook**: Post casual, con emojis y hashtags.
- **instagram**: Caption creativo, muchos emojis, hashtags y prompt para imagen.
- **linkedin**: Post formal y profesional, sin emojis, orientado a negocios.
- **tiktok**: Caption breve, creativo, hashtags virales y sugerencia de música/efecto.
- **whatsapp**: Mensaje directo, breve, claro y cercano.

Cada adaptador tiene su prompt documentado en el código fuente (`adapters/`).

## Documentación de prompts
Cada adaptador tiene su propio prompt documentado en el código fuente dentro de la carpeta `adapters/`. Puedes consultarlos y modificarlos según las necesidades del proyecto.

## Personalización
Puedes agregar nuevas redes sociales creando un archivo en la carpeta `adapters/` y siguiendo el patrón de los adaptadores existentes.

## Requisitos
- Python 3.10+
- FastAPI
- (Opcional) Ollama y modelo Mistral-7B para generación real

## Demo y pruebas
Incluye una demo en vivo con al menos 3 casos de prueba. Puedes crear scripts de ejemplo en la carpeta `tests/`.

## Licencia
MIT
