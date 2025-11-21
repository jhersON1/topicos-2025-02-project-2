# 🚀 Sistema de Publicación Automatizada en Redes Sociales

## 📖 Descripción General

Este sistema permite a los usuarios crear contenido para redes sociales de la **Facultad de Ingeniería de Ciencias de la Computación y Telecomunicaciones (FICCT)** a través de un chat inteligente. La IA detecta automáticamente cuando el usuario quiere generar contenido para redes sociales, crea el contenido específico para cada plataforma, genera una imagen acompañante, y permite la publicación simultánea en Facebook, Instagram y LinkedIn.

## 🎯 Objetivo

Automatizar completamente el proceso de creación y publicación de contenido en múltiples redes sociales, desde la idea inicial hasta la publicación efectiva, manteniendo coherencia y profesionalismo en todas las plataformas.

---

## 🔄 Flujo Completo del Sistema

### **Fase 1: Entrada del Usuario**

1. **Usuario ingresa una noticia/evento** en el chat

   ```
   Ejemplo: "Mañana habrá una conferencia sobre Inteligencia Artificial en la FICCT a las 3 PM"
   ```

2. **Sistema detecta automáticamente** si es contenido relacionado con la FICCT
   - Utiliza el `systemPrompt` configurado
   - Analiza palabras clave relacionadas con la facultad

### **Fase 2: Generación de Contenido**

3. **IA genera contenido específico** para cada red social

   ```json
   {
     "facebook": {
       "caption": "🤖 ¡No te pierdas la conferencia sobre Inteligencia Artificial mañana a las 3 PM en la FICCT! Ven a descubrir las últimas tendencias en IA. 🎓 #FICCT #IA #Conferencia"
     },
     "instagram": {
       "caption": "✨ Conferencia de Inteligencia Artificial 🤖\n📅 Mañana 3 PM\n📍 FICCT\n¡Te esperamos! 🎓\n#FICCT #IA #TechTalk #Universidad #Conferencia"
     },
     "linkedin": {
       "caption": "La Facultad de Ingeniería de Ciencias de la Computación y Telecomunicaciones (FICCT) invita a la conferencia sobre Inteligencia Artificial que se realizará mañana a las 3 PM. Una excelente oportunidad para conocer las últimas tendencias tecnológicas."
     },
     "whatsapp": {
       "titulo": "Conferencia IA - FICCT Mañana 3 PM"
     },
     "tiktok": {
       "titulo": "Conferencia IA en FICCT",
       "hashtags": ["#FICCT", "#IA", "#TechTalk", "#Universidad"]
     }
   }
   ```

4. **Sistema automáticamente genera imagen** usando DALL-E
   - Prompt optimizado para la FICCT
   - Diseño profesional y moderno
   - Elementos tecnológicos y universitarios

### **Fase 3: Confirmación del Usuario**

5. **Frontend muestra vista previa** con:

   - Contenido específico para cada red social
   - Imagen generada
   - Estado: "Pendiente de confirmación"
   - Botón verde: "✅ Publicar en todas las redes sociales"

6. **Usuario confirma la publicación** con un solo clic

### **Fase 4: Publicación Automática**

7. **Sistema publica simultáneamente** en:

   - Facebook (imagen + caption)
   - Instagram (imagen + caption)
   - LinkedIn (imagen + caption profesional)

8. **Resultados mostrados** en tiempo real:
   - ✅ Enlaces directos a cada publicación exitosa
   - ❌ Errores detallados si algo falla
   - Estado final: "Publicado" o "Error"

---

## 🏗️ Arquitectura Técnica

### **Backend (NestJS)**

#### **1. Base de Datos (Prisma)**

```prisma
model Mensaje {
  id                     String             @id @default(uuid())
  contenido             String
  tipo                  TipoContenido      @default(TEXTO)
  contenidoRedesSociales Json?             // JSON con contenido para cada red
  estadoPublicacion     EstadoPublicacion?
  imagenGenerada        String?            // Ruta de imagen para redes sociales
  rutaImagen            String?            // Ruta de imagen regular
  emisor                Emisor
  chatId                String

  publicaciones         Publicacion[]      // Relación con publicaciones
  // ... otros campos
}

enum TipoContenido {
  TEXTO
  IMAGEN
  CONTENIDO_REDES_SOCIALES  // Nuevo tipo
}

enum EstadoPublicacion {
  PENDIENTE_CONFIRMACION
  CONFIRMADO
  PUBLICANDO
  PUBLICADO
  ERROR
}
```

#### **2. Servicios**

**RedesSocialesService**

- Centraliza la lógica de publicación
- Maneja Facebook, Instagram y LinkedIn APIs
- Procesa imágenes y captions específicos
- Registra resultados por plataforma

**SocketChatGateway**

- Detecta contenido de redes sociales automáticamente
- Genera imágenes con DALL-E
- Maneja confirmación de publicación
- Emite eventos WebSocket en tiempo real

#### **3. APIs Integradas**

| Red Social    | Funcionalidad                       | Endpoint                              |
| ------------- | ----------------------------------- | ------------------------------------- |
| **Facebook**  | Publicar texto/imagen               | Graph API `/feed` y `/photos`         |
| **Instagram** | Crear contenedor → Publicar         | Graph API `/media` → `/media_publish` |
| **LinkedIn**  | Registrar upload → Subir → Publicar | API v2 `/ugcPosts`                    |

### **Frontend (Next.js + React)**

#### **1. Componentes**

**Chat Component**

- Renderizado específico para contenido de redes sociales
- Estados visuales (pendiente, publicando, publicado, error)
- Botón de confirmación
- Resultados con enlaces externos

#### **2. WebSocket Events**

| Evento                             | Descripción             |
| ---------------------------------- | ----------------------- |
| `social-content-generated`         | Contenido JSON generado |
| `social-image-generation-complete` | Imagen lista            |
| `social-publish-start`             | Inicio de publicación   |
| `social-publish-complete`          | Publicación exitosa     |
| `social-publish-error`             | Error en publicación    |

---

## 🔧 Configuración Requerida

### **Variables de Entorno**

```env
# OpenAI (para IA y generación de imágenes)
OPENAI_API_KEY=sk-your-openai-key

# Facebook & Instagram (Graph API - Token Unificado)
META_ACCESS_TOKEN=your-meta-access-token
FB_PAGE_ID=your-facebook-page-id
IG_USER_ID=your-instagram-user-id

# LinkedIn (API v2)
LINKEDIN_TOKEN=your-linkedin-access-token
LINKEDIN_URN_PERSON=urn:li:person:your-person-id

# Backend Configuration
BACKEND_URL=http://localhost:4000
DATABASE_URL=postgresql://username:password@localhost:5432/llm_db
```

### **Configuración de APIs**

#### **Facebook & Instagram**

1. Crear App en Facebook Developers
2. Configurar permisos: `pages_manage_posts`, `instagram_basic`, `instagram_content_publish`
3. Obtener tokens de larga duración para la página

#### **LinkedIn**

1. Crear App en LinkedIn Developers
2. Solicitar permisos: `w_member_social`
3. Configurar OAuth y obtener access token

---

## 📱 Flujo de Usuario (UI/UX)

### **1. Estado Inicial**

```
Usuario: "Conferencia de IA mañana en FICCT"
Chat: [Procesando...]
```

### **2. Contenido Generado**

```
[🤖 IA] Contenido para Redes Sociales
⏰ Pendiente

[Imagen generada automáticamente]

📘 Facebook
"🤖 ¡No te pierdas la conferencia sobre IA mañana..."

📸 Instagram
"✨ Conferencia de Inteligencia Artificial 🤖..."

💼 LinkedIn
"La FICCT invita a la conferencia sobre IA..."

[✅ Publicar en todas las redes sociales]
```

### **3. Publicando**

```
[🤖 IA] Contenido para Redes Sociales
🔄 Publicando...

[Misma vista con spinner]
```

### **4. Resultado Final**

```
[🤖 IA] Contenido para Redes Sociales
✅ Publicado

[Imagen]
[Contenido de cada red]

Resultados de la publicación:
✅ Facebook - Ver post ↗️
✅ Instagram - Ver post ↗️
✅ LinkedIn - Ver post ↗️
```

---

## 🛠️ Instalación y Configuración

### **1. Backend Setup**

```bash
cd backend-llm

# Instalar dependencias
npm install

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus tokens

# Ejecutar migraciones
npx prisma migrate dev

# Iniciar servidor
npm run start:dev
```

### **2. Frontend Setup**

```bash
cd frontend-llm

# Instalar dependencias
npm install

# Configurar variables de entorno
cp .env.example .env.local
# Editar .env.local

# Iniciar aplicación
npm run dev
```

---

## 🔍 Casos de Uso

### **Casos Exitosos**

✅ **Conferencias y Eventos**

```
Input: "Conferencia de Blockchain el viernes"
Output: Contenido + imagen + publicación automática
```

✅ **Anuncios Académicos**

```
Input: "Inscripciones abiertas para el curso de Python"
Output: Contenido profesional para cada red social
```

✅ **Celebraciones**

```
Input: "Feliz cumpleaños al Dr. García, decano de FICCT"
Output: Contenido celebratorio + imagen personalizada
```

### **Casos que NO activan el sistema**

❌ **Conversación general**

```
Input: "¿Cómo está el clima?"
Output: Respuesta normal de texto
```

❌ **Preguntas no relacionadas con FICCT**

```
Input: "¿Qué es la inteligencia artificial?"
Output: Respuesta educativa normal
```

---

## 🔧 Troubleshooting

### **Errores Comunes**

**1. Error de tokens expirados**

```
Síntoma: Error 401 en APIs de redes sociales
Solución: Regenerar tokens de acceso
```

**2. Límites de API alcanzados**

```
Síntoma: Error 429 (Rate Limit)
Solución: Esperar o configurar retry logic
```

**3. Contenido no detectado como redes sociales**

```
Síntoma: IA genera texto normal en lugar de JSON
Solución: Verificar systemPrompt y palabras clave de FICCT
```

**4. Imágenes no se muestran**

```
Síntoma: Imagen no carga en frontend
Solución: Verificar endpoint /api/images/:filename en backend
```

---

## 📊 Métricas y Monitoreo

El sistema registra automáticamente:

- **Publicaciones exitosas** por plataforma
- **Errores y fallos** detallados
- **Tiempo de generación** de contenido e imágenes
- **Engagement posterior** (manualmente trackeable con los links)

---

## 🚀 Futuras Mejoras

### **Funcionalidades Planeadas**

1. **Programación de publicaciones**

   - Permitir agendar publicaciones para fechas específicas

2. **Análisis de engagement**

   - Integrar métricas de Facebook/Instagram Insights

3. **Templates personalizables**

   - Permitir modificar el formato de contenido por red social

4. **Moderación avanzada**

   - Sistema de aprobación por múltiples usuarios

5. **Integración con más redes**

   - Twitter/X, WhatsApp Business API, TikTok for Business

6. **IA más contextual**
   - Recordar eventos pasados y mantener coherencia de marca

---

## 👥 Equipo y Contribución

**Desarrollado para:** Facultad de Ingeniería de Ciencias de la Computación y Telecomunicaciones (FICCT)

**Tecnologías Utilizadas:**

- Backend: NestJS, TypeScript, Prisma, PostgreSQL, Socket.io
- Frontend: Next.js, React, TypeScript, Tailwind CSS
- IA: OpenAI GPT-4 + DALL-E
- APIs: Facebook Graph API, Instagram Graph API, LinkedIn API v2

**Contribuir:**

1. Fork el proyecto
2. Crear rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

---

## 🆘 Soporte

Para problemas técnicos o preguntas:

1. **Issues:** Crear issue en GitHub con detalles del problema
2. **Documentación:** Revisar este archivo y los comentarios en el código
3. **Logs:** Verificar logs del backend para errores específicos

**Logs importantes:**

- `🔍 Evaluando si es solicitud de imagen`
- `📱 Contenido de redes sociales generado`
- `🚀 Iniciando publicación en redes sociales`
- `✅ Publicación completada`

---

_Última actualización: Noviembre 16, 2025_
