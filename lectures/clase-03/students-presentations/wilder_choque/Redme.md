# Generador Multiplataforma de Contenido Académico para Redes Sociales

Autor: **Wilder Choque Quispe**  
Tecnología: **Node.js + OpenAI API**

---

## 📌 Descripción del sistema

Este proyecto implementa un **adaptador LLM** capaz de generar contenido publicitario académico optimizado para múltiples redes sociales a partir de un único texto institucional.  

El sistema recibe:

```json
{
  "titulo": "Nueva funcionalidad en nuestra plataforma",
  "contenido": "Hoy lanzamos una nueva característica que permite...",
  "target_networks": ["facebook", "instagram", "linkedin"]
}


## controllador:
import { RedesInputDto } from './dto/content.dto';
import { 
  Controller, 
  Post, 
  Body, 
  ValidationPipe, 
  Get,
  HttpException,
  HttpStatus 
} from '@nestjs/common';
import { ChatbotService } from './chatbot.service';

@Controller('chatbot')
export class ChatbotController {
  constructor(private readonly chatbotService: ChatbotService) {}

  @Post('redes')
  async generarContenidoRedes(
    @Body(ValidationPipe) payload: RedesInputDto
  ) {
    return this.chatbotService.generateSocialContent(payload);
  }
  
}

## servicio
import { Injectable } from '@nestjs/common';
import OpenAI from 'openai';

import { RedesInputDto } from './dto/content.dto';

@Injectable()
export class ChatbotService {
  private openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
  });


  private redesSystemPrompt = `
  Eres un generador de contenido optimizado para redes sociales universitarias.
  
  Debes producir texto diferente por plataforma, manteniendo estilos:
  
  - Facebook: casual y cercano.
  - Instagram: visual y aspiracional; incluye suggested_image_prompt.
  - LinkedIn: profesional y corporativo.
  - TikTok: energético y juvenil.
  - WhatsApp: directo, corto y conversacional.
  
  REGLAS:
  - Responde exclusivamente sobre el contenido dado por el usuario.
  - No inventes datos adicionales.
  - Usa hashtags relevantes.
  - Incluye siempre "character_count".
  - Entrega SIEMPRE un JSON válido.
  `;
  async generateSocialContent(data: RedesInputDto) {
    const { titulo, contenido, target_networks } = data;
  
    const completion = await this.openai.chat.completions.create({
      model: "gpt-4.1-mini", 
      messages: [
        { role: "system", content: this.redesSystemPrompt },
        {
          role: "user",
          content: JSON.stringify({ titulo, contenido, target_networks })
        }
      ],
      response_format: { type: "json_object" }
    });
  
    return JSON.parse(completion.choices[0].message.content);
  }
}



El sistema se divide en:

- **Adaptador LLM (llm_adapter.ts)**  
  Contiene toda la lógica para comunicarse con OpenAI y generar contenido estructurado.

- **Prompts documentados**  
  En `docs/prompts.md` se explica la ingeniería de prompts utilizada.

- **Estructura JSON estricta**  
  Utilizamos `response_format: json_object` para evitar errores en la salida del modelo.



## Flujo del Sistema

1. Recibimos un JSON con título, contenido y redes objetivo.
2. Se envía el prompt al modelo.
3. El modelo devuelve JSON con contenido adaptado por red.
4. El resultado puede integrarse en sistemas como NestJS, CRMs o bots.


## Decisiones de Diseño

- **Uso de GPT-4.1-mini** por economía y eficiencia.
- Uso obligatorio de **JSON estructurado** en las respuestas.
- Adaptador independiente del framework para fácil reutilización.
- Prompt diseñado con reglas estrictas para cada red social.

## Repositorio
https://github.com/Willxd123/multi-red-back.git

.env.example
OPENAI_API_KEY=

##diagrama
https://s.icepanel.io/nrwdjRa66Ftbib/Y4Ba