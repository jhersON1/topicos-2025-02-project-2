# Backend Python · FastAPI Starter

Prototipo mínimo del backend en Python que se usa en el curso LLM Commerce. Expone un endpoint `POST /chat` que reenvía el mensaje del usuario a un LLM (OpenAI u Ollama) y devuelve la respuesta. Incluye opciones para correrlo de forma nativa o en contenedores Docker.

---

## 1. Requisitos previos

- Python 3.10 o superior
- Pip / virtualenv
- (Opcional) Docker y Docker Compose  v2+
- Cuenta en OpenAI **o** instalación local de Ollama

---

## 2. Instalación nativa

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
```

### Windows (PowerShell)
```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Luego edita `.env` con tu configuración:

- `LLM_PROVIDER` → `openai` o `ollama`
- `OPENAI_API_KEY` (si usas OpenAI)
- `OLLAMA_BASE_URL` y `OLLAMA_MODEL` (si usas Ollama local)

### Correr en modo desarrollo
```bash
uvicorn app.main:app --reload --port 8000
```

Prueba el endpoint:
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Recomiéndame una laptop para programación"}'
```

---

## 3. Ejecución con Docker

### Construir y correr con Docker Compose
```bash
docker-compose up --build
```

La API quedará disponible en `http://localhost:8000/chat`.  
Puedes detenerla con `docker-compose down`.

> **Nota:** `.env` no se copia al contenedor por seguridad; el compose monta el archivo local. No olvides definir tus variables antes de levantar los servicios.

---

## 4. Estructura del proyecto
```
backend-python/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── prompts/
│   │   └── system.txt
│   └── services/
│       ├── __init__.py
│       └── llm.py
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── requirements.txt
└── README.md
```

---

## 5. Variables de entorno soportadas

| Variable | Descripción | Valor por defecto |
|----------|-------------|-------------------|
| `LLM_PROVIDER` | Proveedor activo (`openai` u `ollama`) | `openai` |
| `OPENAI_API_KEY` | API key de OpenAI | - |
| `OPENAI_BASE_URL` | URL base de la API de OpenAI | `https://api.openai.com/v1` |
| `OPENAI_MODEL` | Modelo a utilizar (por ejemplo `gpt-4o-mini`) | `gpt-4o-mini` |
| `OPENAI_TEMPERATURE` | Temperatura para las respuestas | `0.4` |
| `OLLAMA_BASE_URL` | URL del servidor Ollama | `http://localhost:11434` |
| `OLLAMA_MODEL` | Modelo local (por ejemplo `llama3.1`) | `llama3.1` |
| `SYSTEM_PROMPT_PATH` | Ruta alternativa del prompt base | `app/prompts/system.txt` |

---

## 6. Puntos de extensión sugeridos

- Agregar validaciones adicionales al payload de entrada (`app/main.py`).
- Loggear cada request/response en un archivo o base de datos.
- Integrar almacenamiento de sesiones para carrito o contexto conversacional.
- Añadir pruebas con `pytest` y `httpx.AsyncClient`.

---

## 7. Troubleshooting común

| Error | Posible causa | Solución |
|-------|---------------|----------|
| `RuntimeError: OPENAI_API_KEY is required` | Variable sin definir | Edita `.env` y reinicia el servidor |
| `Connection refused` usando Ollama | Servicio Ollama no está corriendo | `ollama serve` y confirma el puerto |
| Timeout desde el LLM | Modelo lento o red inestable | Incrementa `HTTP_TIMEOUT` en el código / Compose |
| Respuesta vacía | Modelo sin contenido útil | Revisa el prompt base en `prompts/system.txt` |

---

## 8. Pruebas automatizadas

Este starter incluye pruebas `pytest` básicas para el healthcheck y la validación de payloads.

```bash
pytest
```

Los tests viven en `tests/test_app.py` y usan `httpx.AsyncClient` para evitar levantar un servidor real.

### Ejecutar pruebas dentro del contenedor

```bash
docker-compose run --rm backend-python pytest
```

Este comando construye la imagen (si no existe) y corre los tests en un contenedor efímero.

---

¿Quieres contribuir? Abre un issue o PR con mejoras al prompt, manejo de errores o integración de nuevas herramientas.
