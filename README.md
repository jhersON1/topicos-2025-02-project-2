# LLM Commerce — Curso Completo

<div align="center">

**Chatbot de Compras Inteligentes usando LLMs**

*Tópicos Avanzados de Programación (Algoritmos Generativos)*

Universidad Autónoma Gabriel René Moreno (UAGRM)

**Duración:** 4 semanas | **Clases:** 8 sesiones | **Modalidad:** Práctica

</div>

---

## 📚 Estructura del Repositorio

```
topicos-2025-02-project-2/
├── syllabus/
│   └── SYLLABUS.md              # Programa completo del curso
│
├── lectures/
│   ├── clase-01/                # Introducción a LLMs
│   ├── clase-02/                # Backend base y primer prompt
│   ├── clase-03/                # RAG y búsqueda semántica
│   ├── clase-04/                # Function calling y carrito
│   ├── clase-05/                # Evaluaciones y métricas
│   ├── clase-06/                # Presentaciones parciales
│   ├── clase-07/                # Endurecimiento + front esencial
│   └── clase-08/                # Presentación final
│
├── examples/
│   ├── backend-python/          # Ejemplos FastAPI
│   ├── backend-nodejs/          # Ejemplos NestJS
│   ├── frontend-react/          # Ejemplos React
│   ├── datasets/                # Dataset de productos de ejemplo
│   └── .env.example             # Variables de entorno template
│
└── README.md                    # Este archivo
```

---

## 🎯 Descripción del Curso

Este curso enseña a integrar **Large Language Models (LLMs)** en aplicaciones reales. Los estudiantes construirán un chatbot de compras capaz de:

- 🔍 **Buscar** productos usando búsqueda semántica (RAG)
- 💬 **Conversar** naturalmente con los usuarios
- 🛒 **Gestionar** un carrito de compras vía function calling
- 💡 **Recomendar** productos similares
- ⚖️ **Comparar** especificaciones de productos

### Stack Tecnológico

| Componente | Opciones |
|------------|----------|
| **Frontend** | React + Vite + TailwindCSS |
| **Backend** | FastAPI (Python) **o** NestJS (Node.js) |
| **LLM** | OpenAI API **o** Ollama (local) |
| **Vector Store** | ChromaDB **o** pgvector |
| **Database** | SQLite **o** PostgreSQL |

---

## 🚀 Inicio Rápido

### Para Estudiantes

1. **Lee el Syllabus:**
   ```bash
   cat syllabus/SYLLABUS.md
   ```

2. **Sigue las clases en orden:**
   - Cada carpeta `lectures/clase-XX/` contiene el material completo
   - Incluye teoría, ejemplos de código y tareas

3. **Usa los ejemplos:**
   - `examples/` tiene código de referencia

## 📖 Cronograma del Curso

| Clase | Fecha | Tema | Entregables |
|-------|-------|------|-------------|
| **1** | 4 nov | Introducción a LLMs | Catálogo inicial + 5 conversaciones objetivo |
| **2** | 7 nov | Backend base y primer prompt | Endpoint `/chat` funcional |
| **3** | 11 nov | RAG: ingesta y búsqueda | `/catalog/search` con casos de prueba |
| **4** | 14 nov | Function calling y carrito | Carrito persistente en backend |
| **5** | 18 nov | Evaluaciones y métricas | Script de evaluaciones + backlog demo |
| **6** | 20 nov | Presentaciones parciales | Demo MVP con retroalimentación |
| **7** | 25 nov | Endurecimiento y front esencial | Release candidate conectado a UI mínima |
| **8** | 27 nov | Presentación final | Paquete final (repo, video, slides) |

---

## 🎓 Objetivos de Aprendizaje

### Al finalizar el curso, los estudiantes podrán:

**Técnicos:**
- ✅ Integrar LLMs (OpenAI/Ollama) en aplicaciones web
- ✅ Implementar RAG (Retrieval Augmented Generation)
- ✅ Usar function calling para dar "acciones" al LLM
- ✅ Trabajar con embeddings y vector stores
- ✅ Diseñar interfaces conversacionales en React
- ✅ Evaluar y mejorar respuestas de LLMs

**Transversales:**
- ✅ Trabajo colaborativo en proyectos técnicos
- ✅ Comunicación efectiva de soluciones
- ✅ Pensamiento crítico sobre IA y ética
- ✅ Debugging y resolución de problemas

---

## 💻 Requisitos Previos

### Conocimientos

- JavaScript/TypeScript básico
- Python básico
- React fundamentals
- Conceptos de API REST
- Git básico

### Software a Instalar

#### Windows
```bash
winget install OpenJS.NodeJS
winget install Python.Python.3.11
winget install Git.Git
winget install Ollama.Ollama  # opcional
```

#### macOS
```bash
brew install node python git ollama
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install -y nodejs npm python3 python3-venv git
curl -fsSL https://ollama.ai/install.sh | sh  # opcional
```

#### Verificación
```bash
node -v        # v18+
python3 --version  # 3.10+
git --version
ollama --version  # opcional
```

### Cuentas Necesarias

- **GitHub:** Para el repositorio del proyecto
- **OpenAI API:** [platform.openai.com](https://platform.openai.com) (o usar Ollama localmente)
- *Opcional:* Vercel/Render para deployment

---

## 📊 Evaluación

### Distribución de Notas

| Criterio | Peso |
|----------|------|
| Integración LLM + Funciones | 35% |
| Calidad UI/UX | 20% |
| RAG y Datos | 15% |
| Pruebas y Evals | 15% |
| Presentación y Docs | 15% |

### Entregables Finales

- [x] Código fuente completo (GitHub)
- [x] Catálogo de productos (≥20 items)
- [x] RAG funcionando con embeddings
- [x] Function calling (carrito completo)
- [x] UI de chat funcional
- [x] README con instrucciones de setup
- [x] Video demo (≤3 min)
- [x] Slides de presentación (≤10)

---

## 📚 Recursos Adicionales

### Documentación Oficial

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Ollama Documentation](https://ollama.ai)
- [LangChain Python](https://python.langchain.com)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [NestJS Docs](https://docs.nestjs.com)
- [ChromaDB Guide](https://docs.trychroma.com)
- [React + Vite](https://vitejs.dev/guide/)

### Cursos Online Complementarios

- [DeepLearning.AI - LangChain for LLMs](https://www.deeplearning.ai/short-courses/)
- [Full Stack LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/)

### Videos Recomendados

- "Intro to Large Language Models" - Andrej Karpathy
- "What are embeddings?" - Pinecone
- "RAG Explained" - LangChain

---

## 🐛 Troubleshooting Común

### Error: "ModuleNotFoundError: No module named 'openai'"
```bash
pip install openai
```

### Error: "OPENAI_API_KEY not found"
```bash
# Verifica que .env existe y tiene la key
cat .env | grep OPENAI_API_KEY
```

### ChromaDB: "Cannot connect to database"
```bash
# Asegúrate de que el directorio existe
mkdir -p data/chroma
```

### Frontend no conecta con Backend
```bash
# Verifica que VITE_API_URL en .env.local apunta a:
VITE_API_URL=http://localhost:8000
```

### Rate Limit de OpenAI
```python
# Agrega delays entre requests
import time
time.sleep(1)  # 1 segundo entre llamadas
```

---

## 🤝 Contribuciones

Este material está diseñado para ser mejorado iterativamente.

**Si eres instructor:**
- Agrega tus notas y mejoras
- Comparte casos de uso adicionales
- Documenta problemas comunes que encuentres

**Si eres estudiante:**
- Reporta errores o confusiones
- Sugiere mejoras al material
- Comparte tu proyecto como ejemplo

---

## 📄 Licencia

Este material educativo está bajo licencia MIT. Siéntete libre de:
- Usar el material en tus propios cursos
- Modificar y adaptar el contenido
- Compartir con otros educadores

**Atribución:** Universidad Autónoma Gabriel René Moreno (UAGRM)

---

## 📞 Contacto

- Canal oficial del curso: [Slack/Discord - Por definir]
- Correo de soporte académico: [Por definir]
- Universidad: UAGRM - FICCT

---

## ✨ Agradecimientos

Este curso fue diseñado para introducir a estudiantes en el emocionante mundo de los LLMs y su aplicación práctica en el desarrollo de software.

Agradecimientos especiales a:
- OpenAI por democratizar el acceso a LLMs
- Anthropic por Claude y materiales educativos
- La comunidad de LangChain
- Todos los contribuidores de ChromaDB y Ollama

---

<div align="center">

**¡Bienvenidos al curso! 🚀**

*Prepárense para construir aplicaciones increíbles con IA*

</div>
