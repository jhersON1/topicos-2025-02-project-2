# Backend Node.js · NestJS Starter

Plantilla mínima con NestJS para el curso LLM Commerce. Expone un endpoint `POST /chat` que reenvía los mensajes del usuario a un LLM (OpenAI u Ollama). Incluye `Dockerfile`, `docker-compose.yml` y guías para ejecución nativa en Windows, macOS y Ubuntu.

---

## 1. Requisitos previos

- Node.js 20.x
- npm 9.x o superior
- (Opcional) Docker y Docker Compose v2+
- Cuenta en OpenAI **o** instalación local de Ollama

---

## 2. Instalación nativa

### macOS / Linux
```bash
npm install
cp .env.example .env
npm run start:dev
```

### Windows (PowerShell)
```powershell
npm install
Copy-Item .env.example .env
npm run start:dev
```

El servidor quedará disponible en `http://localhost:3000/chat`.

Healthcheck rápido:
```bash
curl http://localhost:3000/health
```

### Prueba rápida del endpoint
```bash
curl -X POST http://localhost:3000/chat `
  -H "Content-Type: application/json" `
  -d "{\"message\": \"Busco una laptop para desarrollo web\"}"
```

> Asegúrate de completar `.env` con tus credenciales/ajustes antes de ejecutar.

---

## 3. Ejecución con Docker

```bash
docker-compose up --build
```

- La API se expone en `http://localhost:3000/chat`.
- Detén los servicios con `docker-compose down`.
- El contenedor compila la app (`npm run build`) y luego ejecuta `npm run start:prod`.

---

## 4. Estructura del proyecto
```
backend-nodejs/
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── package.json
├── tsconfig.json
├── tsconfig.build.json
├── nest-cli.json
├── src/
│   ├── main.ts
│   ├── app.module.ts
│   ├── prompts/
│   │   └── system.txt
│   └── chat/
│       ├── chat.module.ts
│       ├── chat.controller.ts
│       ├── chat.service.ts
│       └── dto/create-chat.dto.ts
└── README.md
```

---

## 5. Variables de entorno soportadas

| Variable | Descripción | Valor por defecto |
|----------|-------------|-------------------|
| `LLM_PROVIDER` | Proveedor activo (`openai` u `ollama`) | `openai` |
| `OPENAI_API_KEY` | API key de OpenAI | - |
| `OPENAI_MODEL` | Modelo target (p. ej. `gpt-4o-mini`) | `gpt-4o-mini` |
| `OPENAI_BASE_URL` | URL base de la API de OpenAI | `https://api.openai.com/v1` |
| `OPENAI_TEMPERATURE` | Temperatura del modelo | `0.4` |
| `OLLAMA_BASE_URL` | URL del servicio Ollama | `http://localhost:11434` |
| `OLLAMA_MODEL` | Modelo local a utilizar | `llama3.1` |
| `SYSTEM_PROMPT_PATH` | Ruta personalizada del prompt | `src/prompts/system.txt` |

---

## 6. Scripts npm más usados

| Script | Descripción |
|--------|-------------|
| `npm run start:dev` | Hot-reload con `nest start --watch` |
| `npm run start:prod` | Ejecuta `node dist/main.js` (requiere `npm run build`) |
| `npm run build` | Genera la carpeta `dist/` con TypeScript compilado |
| `npm run lint` | Eslint sobre `src/**/*.ts` |
| `npm run format` | Formatea con Prettier |

---

## 7. Pruebas automatizadas

- Pruebas unitarias/e2e con Jest:
  ```bash
  npm run test       # Jest (unit/integration)
  npm run test:e2e   # Pruebas end-to-end con supertest
  ```

Los archivos de ejemplo viven en `test/app.e2e-spec.ts` y validan el healthcheck y la validación de payloads para `/chat`.

### Ejecutar pruebas dentro del contenedor

```bash
docker-compose run --rm backend-nodejs npm run test:e2e
```

También puedes usar `npm run test` en lugar de `test:e2e` si quieres correr el set completo.

---

## 8. Troubleshooting rápido

| Error | Posible causa | Solución |
|-------|---------------|----------|
| `Missing OPENAI_API_KEY` | No definiste la variable | Edita `.env` y reinicia |
| `ECONNREFUSED` al llamar Ollama | Servicio no iniciado | Ejecuta `ollama serve` o ajusta `OLLAMA_BASE_URL` |
| `Cannot find module` | Dependencias faltantes | Corre `npm install` |
| Respuesta vacía | Prompt o modelo no configurado | Revisa `src/prompts/system.txt` y el provider activo |

---

## 9. Próximos pasos sugeridos

- Añadir logging estructurado (p. ej. `pino`).
- Integrar métricas/observabilidad (Prometheus, OpenTelemetry).
- Conectar con vector store y persistir catálogo.
- Implementar tests con `@nestjs/testing`.

---

¿Sugerencias o mejoras? Abre un issue o PR indicando la cohorte y describe tu aporte.
