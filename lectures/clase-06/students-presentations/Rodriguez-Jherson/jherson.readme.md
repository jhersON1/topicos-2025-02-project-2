# PublIA - Backend

<p align="center">
  <a href="http://nestjs.com/" target="blank"><img src="https://nestjs.com/img/logo-small.svg" width="200" alt="Nest Logo" /></a>
</p>

## 📋 Descripción

**PublIA** es una plataforma avanzada de gestión de redes sociales impulsada por Inteligencia Artificial. Este repositorio contiene el **Backend**, construido con **NestJS**, que orquesta la generación de contenido, la gestión de chats y la publicación automatizada en múltiples plataformas sociales.

El sistema permite a los usuarios interactuar con un asistente de IA para generar textos, imágenes y videos, y publicarlos directamente en sus redes sociales favoritas.

## 🚀 Características Principales

-   **🤖 Inteligencia Artificial Generativa**:
    -   Integración con **Google Gemini** y **OpenAI** para generación de texto avanzado.
    -   Generación de imágenes y videos optimizados para redes sociales.
-   **📱 Publicación Multi-Plataforma**:
    -   Conexión y publicación automática en **Facebook**, **Instagram**, **LinkedIn** y **TikTok**.
-   **💬 Sistema de Chat Inteligente**:
    -   Interfaz de chat para interactuar con la IA, refinar contenido y gestionar publicaciones.
    -   Historial de conversaciones y contexto persistente.
-   **🟢 Bot de WhatsApp**:
    -   Integración para gestión y actualizaciones de estado vía WhatsApp.
-   **☁️ Gestión de Medios**:
    -   Almacenamiento y optimización de activos multimedia mediante **Cloudinary**.
-   **🔒 Seguridad**:
    -   Autenticación robusta con **JWT** y **Passport**.

## 🛠️ Stack Tecnológico

-   **Framework**: [NestJS](https://nestjs.com/) (Node.js)
-   **Base de Datos**: [MongoDB](https://www.mongodb.com/) (con Mongoose)
-   **Lenguaje**: TypeScript
-   **IA & ML**: Google Vertex AI, OpenAI API
-   **Almacenamiento**: Cloudinary
-   **Validación**: Class Validator, Class Transformer

## 📦 Instalación

1.  **Clonar el repositorio**
    ```bash
    git clone <url-del-repositorio>
    cd publ-ia-back
    ```

2.  **Instalar dependencias**
    ```bash
    npm install
    ```

3.  **Configuración de Entorno**
    Copia el archivo de ejemplo y configura tus variables de entorno:
    ```bash
    cp .env.template .env
    ```
    *Asegúrate de rellenar las credenciales para Mongo, JWT, Cloudinary y las APIs de redes sociales.*

## ▶️ Ejecución

### Desarrollo
```bash
npm run start:dev
```

### Producción
```bash
npm run build
npm run start:prod
```

## 📂 Estructura del Proyecto

El código fuente se encuentra en el directorio `src` y está organizado modularmente:

-   `auth/`: Módulo de autenticación y autorización.
-   `bot/`: Lógica del bot de WhatsApp.
-   `chat/`: Gestión de conversaciones y mensajes.
-   `gpt/`: Servicios de integración con modelos de IA.
-   `social-media/`: (Meta, LinkedIn, TikTok) Adaptadores para cada red social.
-   `database/`: Configuración de conexión a MongoDB.

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para mejoras.

## 📄 Licencia

Este proyecto es propiedad privada.
