
# Plataforma Automatizada de Gestión de Publicaciones
Generación y distribución de contenido para múltiples redes sociales  
Facultad de Ciencias de la Computación

---

## Arquitectura General del Sistema

El sistema está diseñado con **tres módulos esenciales**, cada uno cumpliendo funciones específicas dentro del flujo de automatización:

1. **Motor de Generación de Contenido (IA)**  
2. **Módulos de Integración con Redes Sociales**  
3. **Servidor Central de Control (API Flask)**

---

## 1. Motor de Generación de Contenido (IA)

La aplicación utiliza un modelo de lenguaje encargado de:

- Interpretar la solicitud del usuario.  
- Determinar si se trata de una interacción conversacional o una petición de contenido.  
- Elaborar textos adecuados para diversas plataformas digitales.  

El módulo trabaja con un **prompt base** que define reglas de estilo, tono y estructura del resultado.  
La respuesta del modelo siempre se devuelve en formato JSON estructurado.

---

## Ejemplo del Comportamiento del Generador

Dependiendo del tipo de solicitud, el módulo entrega dos formatos:

### Conversación general
```
{
  "status": "conversacion",
  "mensaje": "Respuesta amigable del asistente",
  "haypublicacion": false,
  "publicaciones": {}
}
```

### Solicitud de contenido
```
{
  "status": "publicacion",
  "mensaje": "Se generaron textos personalizados.",
  "haypublicacion": true,
  "publicaciones": {
      "facebook": {"response": "Texto adaptado a formato extendido"},
      "instagram": {"response": "Publicación con estilo visual y hashtags"},
      "linkedin": {"response": "Contenido formal y profesional"},
      "tiktok": {"response": "Mensaje breve y dinámico"},
      "whatsapp": {"response": "Mensaje directo y claro"}
  }
}
```

---

## 2. Comunicación con OpenAI

El servidor construye un prompt con las instrucciones del usuario y lo envía al modelo.  
El resultado se procesa y se transforma en un objeto JSON validado que las otras partes del sistema puedan entender.

---

## 3. Integraciones con Redes Sociales

El sistema contiene módulos independientes para manejar cada plataforma.

---

## Módulo de Facebook

### Características:
- Requiere PAGE_ID y ACCESS_TOKEN.  
- Utiliza **Graph API** para manejar publicaciones.

### Funcionalidades:
- Recuperar información de la página.  
- Publicar mensajes de texto.
- Subir imágenes con descripción.

Cada solicitud se valida y genera una respuesta estructurada que incluye el ID de la publicación creada.

---

## Módulo de Instagram

La publicación en Instagram se realiza en dos pasos:

1. **Creación del contenedor de media**  
2. **Publicación del contenido procesado**

El sistema implementa intentos automáticos para asegurar que las imágenes sean procesadas correctamente antes de publicarse.

---

## Módulo de WhatsApp

Usa **Twilio** como pasarela para el envío de mensajes.  
Las funciones principales incluyen:

- Validación del número destino.  
- Construcción del mensaje.  
- Envío y registro mediante la API de Twilio.

---

## Flujo Completo del Sistema

1. El usuario envía una instrucción a través del sistema.  
2. El motor IA analiza el mensaje y genera contenido.  
3. La API central coordina la publicación en cada plataforma.  
4. Cada módulo retorna resultados individuales indicando éxito o error.  

---

## Manejo de Errores

Cada componente implementa:

- Comprobación de credenciales.  
- Validación de parámetros mínimos.  
- Registro detallado de errores.  
- Respuestas consistentes en formato JSON.  

---

## Tecnologías Utilizadas

| Componente | Tecnología |
|-----------|------------|
| Servidor | Python + Flask |
| IA | Modelo de Lenguaje |
| Facebook | Graph API |
| Instagram | Instagram Graph API |
| WhatsApp | Twilio |
| Gestión HTTP | requests |
| Configuración | dotenv |

---

## Ejemplo de Uso

**Solicitud:**  
"Necesito un texto para anunciar un nuevo taller académico."

**Resultado:**  
El sistema genera y distribuye publicaciones adaptadas a cada red social según su estilo y formato.

---

## Próximas Mejoras

- Incorporación de TikTok y LinkedIn (módulos completos).  
- Programación automática de publicaciones.  
- Panel administrativo con métricas de desempeño.  
- Generación automática de contenido visual.  
