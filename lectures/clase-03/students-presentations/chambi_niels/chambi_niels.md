# Tarea 2. Prototipo de Adaptación con LLM

## Enlace al repositorio de codigo

[https://github.com/NielsRoy/proyecto-2-topicos](https://github.com/NielsRoy/proyecto-2-topicos)

## Prompt plantilla para enviar al LLM

```md
### ROL
Eres un "Social Media Manager" y "Copywriter" experto, con especialización en comunicación digital para instituciones de educación superior (universidades). Tu objetivo es maximizar la interacción y comunicar eficazmente las noticias de la facultad.

### CONTEXTO DE ENTRADA (Noticia Base)
Aquí están los datos de la noticia proporcionados por el personal administrativo:
* **Título:** [AQUÍ VA EL TÍTULO DE LA NOTICIA]
* **Descripción Detallada:** [AQUÍ VA LA DESCRIPCIÓN LARGA DE LA NOTICIA]
* **Fechas Clave:** [AQUÍ VA LA FECHA/HORA DEL EVENTO]
* **Lugar:** [AQUÍ VA EL LUGAR O "Modalidad Virtual"]
* **Llamada a la Acción (CTA):** [AQUÍ VA EL ENLACE O INSTRUCCIÓN, EJ: "Regístrate en..."]
* **Audiencia Principal:** [AQUÍ VA LA AUDIENCIA, EJ: "Estudiantes de Ingeniería", "Empresas", "Docentes"]

### TAREA PRINCIPAL
Genera el texto de publicación (solo texto) para las 5 redes sociales listadas abajo. Debes adaptar el contenido de la "Noticia Base" a las "Directrices de Contenido" específicas para cada red.

### DIRECTRICES DE CONTENIDO POR RED SOCIAL (Editable)

1.  **Facebook:**
    * **Tono:** Informativo, amigable y que fomente la comunidad.
    * **Longitud:** 2-3 párrafos cortos (aprox. 400-600 caracteres).
    * **Emojis:** Uso moderado (ej. 🎓, 💡, 📅, 📍).
    * **Hashtags:** 3-5 hashtags relevantes al final.
    * **Especial:** Asegurarse de que la Llamada a la Acción (CTA) sea muy clara y el enlace (si existe) esté visible.

2.  **Instagram:**
    * **Tono:** Visual, inspirador y atractivo. El texto es un "caption".
    * **Longitud:** El primer renglón debe ser un "gancho" fuerte (máx. 125 caracteres antes del "ver más").
    * **Emojis:** Uso más liberal y visual (ej. ✨, 🚀, 📸, 🤩).
    * **Hashtags:** 5-10 hashtags (mezcla de populares y de nicho de la facultad).
    * **Especial:** Incluir una CTA que dirija a "link en la bio" o al enlace directo si la descripción lo permite.

3.  **Estado de WhatsApp:**
    * **Tono:** Urgente, directo, personal e hiper-conciso.
    * **Longitud:** 1-2 frases. Máximo 150 caracteres.
    * **Emojis:** Uso clave para llamar la atención (ej. ❗, 📣, ➡️, 🔥).
    * **Especial:** Debe ser un "teaser" (un adelanto) que genere curiosidad e incluya el enlace directo (CTA) si es corto.

4.  **LinkedIn:**
    * **Tono:** Profesional, formal y orientado al valor académico/profesional.
    * **Longitud:** 1-2 párrafos estructurados (aprox. 300-500 caracteres).
    * **Emojis:** Uso mínimo o nulo. Solo emojis profesionales si es estrictamente necesario (ej. 💼, 📈, 🏛️).
    * **Hashtags:** 3-5 hashtags profesionales y de industria (ej. #EducacionSuperior, #Ingenieria, #Networking).
    * **Especial:** Enfocar el valor para la carrera, el desarrollo profesional, la academia o la industria.

5.  **TikTok:**
    * **Tono:** Muy casual, entretenido, que genere curiosidad (FOMO) y use lenguaje de tendencia (si aplica).
    * **Longitud:** 1-3 frases muy cortas (máx. 150 caracteres).
    * **Emojis:** Uso creativo y de tendencia (ej. 🤯, 👀, 🔥, 💯).
    * **Hashtags:** 2-3 hashtags de tendencia + 1 hashtag de marca/facultad.
    * **Especial:** El texto es un "caption" para un video. Debe ser un gancho rápido, hacer una pregunta, o describir la acción.

### FORMATO DE SALIDA OBLIGATORIO
Responde *únicamente* con un objeto JSON válido. No incluyas ningún texto, explicación, saludo o despedida antes o después del objeto JSON. La estructura debe ser la siguiente clave-valor:

{
  "facebook": "...",
  "instagram": "...",
  "whatsapp": "...",
  "linkedin": "...",
  "tiktok": "..."
}
```

## Endpoint para obtener el contenido de texto para las publicaciones en redes sociales

```bash
curl -X POST http://localhost:3000/post \
  -H "Content-Type: application/json" \
  -d '{
    "title": "inicio de retiro de materias",
    "description": "habilitación del periodo de retiro de materias en las fechas indicadas",
    "dates": "08 de abril del 2025 hasta 10 de abril de 2025",
    "place": "",
    "links": "",
    "audience": "estudiantes de la facultad de ciencias de la computación, redes y telecomunicaciones"
  }'

```

## Respuesta del endpoint:

```json
{
  "facebook": "¡Atención, estudiantes de la Facultad de Ciencias de la Computación, Redes y Telecomunicaciones! 🎓\n\nQueremos recordarles que el periodo de retiro de materias ha sido oficialmente habilitado. Esta es una oportunidad importante para ajustar tu carga académica si lo consideras necesario. Asegúrate de revisar tus opciones con anticipación.\n\nLas fechas clave para realizar este proceso son del **08 de abril al 10 de abril de 2025**. No dejes pasar esta ventana. Para conocer todos los detalles y el procedimiento, visita el enlace oficial en nuestra página. ¡Tu planificación académica es clave para un semestre exitoso! 💡📅\n\nMás información y procedimiento aquí: [ENLACE_A_INFORMACION_OFICIAL]\n\n#RetiroDeMaterias #VidaUniversitaria #FacultadCRyT #EstudiantesCRyT",
  "instagram": "¡Ojo, futuros ingenieros! 👀 Es tu momento de optimizar tu semestre. 🚀\n\nEl periodo de retiro de materias ya está habilitado para todos los estudiantes de nuestra Facultad de Ciencias de la Computación, Redes y Telecomunicaciones. ✨\n\nAprovecha esta ventana del **08 al 10 de abril de 2025** para tomar decisiones académicas inteligentes. Revisa tu avance y ajusta tu horario si es necesario para asegurar tu éxito. 📚💡\n\nPara todos los detalles y cómo proceder, visita el #LinkEnBio o nuestra sección de noticias académicas. ¡No te quedes con dudas! 💻🎓\n\n#Universidad #VidaUniversitaria #EstudiantesCRyT #FacultadCRyT #RetiroDeMaterias #Ingenieria #Programacion #Redes #Telecomunicaciones #ExitoAcademico",
  "whatsapp": "¡Atención, estudiantes CRyT! 📣 Periodo de retiro de materias habilitado del 08 al 10 de abril 2025. ¡No lo olvides! ➡️ [ENLACE_A_INFORMACION_OFICIAL]",
  "linkedin": "Aviso Importante para la Comunidad Académica de la Facultad de Ciencias de la Computación, Redes y Telecomunicaciones.\n\nInformamos a nuestros estimados estudiantes que el periodo para el retiro de materias ha sido oficialmente habilitado. Este proceso permite una gestión estratégica de la trayectoria académica, asegurando que cada estudiante pueda optimizar su carga de estudio para un rendimiento óptimo y una progresión profesional efectiva.\n\nEl plazo para realizar este procedimiento es del **08 al 10 de abril de 2025**. Recomendamos a todos los interesados consultar la normativa y los procedimientos detallados a través de los canales oficiales de la facultad para garantizar el cumplimiento de los requisitos. La planificación académica es un pilar fundamental para el éxito profesional futuro. 🏛️\n\n#EducacionSuperior #GestionAcademica #FacultadCRyT #DesarrolloProfesional #IngenieriaInformatica",
  "tiktok": "🚨 ¿Cambios en tu horario? ¡Es ahora! Periodo de retiro de materias habilitado del 08 al 10 de abril 2025. ¡No te lo pierdas! 🤯\n\n#CRyT #universidad #estudiantes #hackacademico"
}
```