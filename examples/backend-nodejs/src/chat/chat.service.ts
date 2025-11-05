import { Injectable, InternalServerErrorException, Logger } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import axios from 'axios';
import * as fs from 'fs';
import * as path from 'path';

@Injectable()
export class ChatService {
  private readonly logger = new Logger(ChatService.name);
  private readonly config = {
    provider: this.configService.get<string>('LLM_PROVIDER', 'openai'),
    openai: {
      apiKey: this.configService.get<string>('OPENAI_API_KEY'),
      baseUrl: this.configService.get<string>('OPENAI_BASE_URL', 'https://api.openai.com/v1'),
      model: this.configService.get<string>('OPENAI_MODEL', 'gpt-4o-mini'),
      temperature: Number(this.configService.get<string>('OPENAI_TEMPERATURE', '0.4')),
    },
    ollama: {
      baseUrl: this.configService.get<string>('OLLAMA_BASE_URL', 'http://localhost:11434'),
      model: this.configService.get<string>('OLLAMA_MODEL', 'llama3.1'),
    },
    promptPath: this.configService.get<string>(
      'SYSTEM_PROMPT_PATH',
      path.join(process.cwd(), 'prompts', 'system.txt'),
    ),
  };

  constructor(private readonly configService: ConfigService) {}

  async generate(message: string): Promise<string> {
    const provider = this.config.provider?.toLowerCase();
    if (provider === 'openai') {
      return this.callOpenAI(message);
    }
    if (provider === 'ollama') {
      return this.callOllama(message);
    }
    throw new InternalServerErrorException(`LLM_PROVIDER '${provider}' no está soportado (usa 'openai' u 'ollama').`);
  }

  private async callOpenAI(message: string): Promise<string> {
    const { apiKey, baseUrl, model, temperature } = this.config.openai;
    if (!apiKey) {
      throw new InternalServerErrorException('OPENAI_API_KEY es requerido cuando LLM_PROVIDER=openai');
    }

    const payload = {
      model,
      messages: [
        { role: 'system', content: this.loadSystemPrompt() },
        { role: 'user', content: message },
      ],
      temperature,
    };

    try {
      const response = await axios.post(
        `${baseUrl.replace(/\/$/, '')}/chat/completions`,
        payload,
        {
          headers: {
            Authorization: `Bearer ${apiKey}`,
            'Content-Type': 'application/json',
          },
          timeout: 60000,
        },
      );

      return response.data.choices?.[0]?.message?.content ?? '';
    } catch (error) {
      this.logger.error('Error calling OpenAI', error instanceof Error ? error.stack : `${error}`);
      throw new InternalServerErrorException('No se pudo obtener una respuesta del modelo OpenAI.');
    }
  }

  private async callOllama(message: string): Promise<string> {
    const { baseUrl, model } = this.config.ollama;
    try {
      const response = await axios.post(
        `${baseUrl.replace(/\/$/, '')}/api/chat`,
        {
          model,
          messages: [
            { role: 'system', content: this.loadSystemPrompt() },
            { role: 'user', content: message },
          ],
          stream: false,
        },
        { timeout: 120000 },
      );

      return response.data?.message?.content ?? '';
    } catch (error) {
      this.logger.error('Error calling Ollama', error instanceof Error ? error.stack : `${error}`);
      throw new InternalServerErrorException('No se pudo obtener una respuesta de Ollama.');
    }
  }

  private loadSystemPrompt(): string {
    try {
      const primaryPath = this.config.promptPath;
      if (fs.existsSync(primaryPath)) {
        return fs.readFileSync(primaryPath, { encoding: 'utf-8' });
      }

      const fallbackPath = path.join(process.cwd(), 'src', 'prompts', 'system.txt');
      if (fs.existsSync(fallbackPath)) {
        return fs.readFileSync(fallbackPath, { encoding: 'utf-8' });
      }

      throw new Error(`Prompt not found in ${primaryPath} ni ${fallbackPath}`);
    } catch (error) {
      this.logger.error(`No se pudo leer el prompt base en ${this.config.promptPath}`, error instanceof Error ? error.stack : `${error}`);
      throw new InternalServerErrorException('No se pudo cargar el prompt base del sistema.');
    }
  }
}
