# Principios SOLID en el Backend LLM

## Índice

- [Introducción](#introducción)
- [1. Single Responsibility Principle (SRP)](#1-single-responsibility-principle-srp)
- [2. Open/Closed Principle (OCP)](#2-openclosed-principle-ocp)
- [3. Liskov Substitution Principle (LSP)](#3-liskov-substitution-principle-lsp)
- [4. Interface Segregation Principle (ISP)](#4-interface-segregation-principle-isp)
- [5. Dependency Inversion Principle (DIP)](#5-dependency-inversion-principle-dip)
- [Arquitectura del Proyecto](#arquitectura-del-proyecto)
- [Beneficios Obtenidos](#beneficios-obtenidos)
- [Ejemplos Prácticos](#ejemplos-prácticos)

## Introducción

Este documento explica cómo el backend LLM implementa los **principios SOLID** de programación orientada a objetos. Estos principios garantizan que el código sea mantenible, escalable, testeable y fácil de extender.

Los principios SOLID son:

- **S** - Single Responsibility Principle
- **O** - Open/Closed Principle
- **L** - Liskov Substitution Principle
- **I** - Interface Segregation Principle
- **D** - Dependency Inversion Principle

## 1. Single Responsibility Principle (SRP)

> "Una clase debe tener una sola razón para cambiar"

### Implementación en el Proyecto

Cada servicio y clase tiene una **única responsabilidad**:

#### `SocketChatService`

```typescript
@Injectable()
export class SocketChatService {
  // SOLO se encarga de gestionar clientes WebSocket conectados
  addClient(client: Socket) { ... }
  getClients() { ... }
  getClientCount() { ... }
}
```

**Responsabilidad única**: Gestión de conexiones WebSocket.

#### `ChatsService`

```typescript
@Injectable()
export class ChatsService {
  // SOLO operaciones CRUD para chats
  create(createChatDto: CreateChatDto) { ... }
  findAll() { ... }
  findOne(id: string) { ... }
  update(id: string, updateChatDto: UpdateChatDto) { ... }
  remove(id: string) { ... }
}
```

**Responsabilidad única**: Operaciones CRUD de chats.

#### `RedesSocialesService`

```typescript
@Injectable()
export class RedesSocialesService {
  // SOLO maneja publicaciones en redes sociales
  async publicarEnTodasLasRedes() { ... }
  private async guardarResultadosPublicacion() { ... }
  async obtenerHistorialPublicaciones() { ... }
}
```

**Responsabilidad única**: Gestión de publicaciones en redes sociales.

#### `PrismaService`

```typescript
@Injectable()
export class PrismaService extends PrismaClient {
  // SOLO maneja la conexión a la base de datos
  async onModuleInit() { ... }
  async onModuleDestroy() { ... }
}
```

**Responsabilidad única**: Conexión y configuración de base de datos.

### Ventajas del SRP en el Proyecto

- Fácil mantenimiento: cambios en una funcionalidad no afectan otras
- Testing simplificado: cada clase se puede probar independientemente
- Código más legible y comprensible
- Menor acoplamiento entre componentes

## 2. Open/Closed Principle (OCP)

> "Las entidades de software deben estar abiertas para extensión, pero cerradas para modificación"

### Implementación en el Proyecto

#### Extensibilidad de DTOs

```typescript
// Fácil de extender sin modificar código existente
export type CreateChatDto = Omit<
  Chat,
  'id' | 'isActive' | 'createdAt' | 'updatedAt'
>;
```

#### Sistema de Redes Sociales Extensible

```typescript
export interface ContenidoRedesSociales {
  facebook: { caption: string };
  instagram: { caption: string };
  linkedin: { caption: string };
  whatsapp: { titulo: string };
  tiktok: { titulo: string; hashtags: string[] };
  // Se pueden agregar nuevas redes sin modificar código existente
}
```

#### Arquitectura Modular

```
src/api/
├── facebook/     # Módulo independiente
├── instagram/    # Módulo independiente
├── linkedIn/     # Módulo independiente
└── [nueva-red]/  # Nueva red social sin modificar existentes
```

### Ejemplos de Extensión

Para agregar una nueva red social (ej: Twitter):

1. **Crear módulo independiente**:

   ```typescript
   // src/api/twitter/twitter.api.ts
   export const sendTweet = async (tweetDto: SendTweetDto) => { ... }
   ```

2. **Extender interface**:

   ```typescript
   export interface ContenidoRedesSociales {
     // ... redes existentes
     twitter: { text: string; hashtags: string[] }; // Solo agregar
   }
   ```

3. **Agregar al servicio**:
   ```typescript
   // En RedesSocialesService, solo agregar nuevo caso
   // Publicar en Twitter
   try {
     const twitterResult = await sendTweet(contenido.twitter);
     // ...
   } catch (error) { ... }
   ```

## 3. Liskov Substitution Principle (LSP)

> "Los objetos de las clases derivadas deben poder reemplazar a los objetos de la clase base sin alterar el funcionamiento del programa"

### Implementación en el Proyecto

#### `PrismaService` extiende `PrismaClient`

```typescript
export class PrismaService
  extends PrismaClient
  implements OnModuleInit, OnModuleDestroy
{
  // Puede usarse como PrismaClient en cualquier lugar
  // Mantiene el contrato de la clase base
  // Agrega funcionalidad sin romper comportamiento existente

  async onModuleInit() {
    await this.$connect(); // Funcionalidad adicional
  }

  async onModuleDestroy() {
    await this.$disconnect(); // Funcionalidad adicional
  }
}
```

#### Uso Polimórfico

```typescript
// Se puede usar PrismaService donde se espere PrismaClient
constructor(private readonly prismaService: PrismaService) {}

// Todos los métodos de PrismaClient funcionan correctamente
await this.prismaService.chat.create({ data: createChatDto });
await this.prismaService.mensaje.findMany();
```

### Beneficios del LSP

- Polimorfismo seguro
- Intercambiabilidad de implementaciones
- Extensión sin ruptura de contratos

## 4. Interface Segregation Principle (ISP)

> "Los clientes no deben depender de interfaces que no usan"

### Implementación en el Proyecto

#### DTOs Específicos y Cohesivos

```typescript
// Interface pequeña y específica para mensajes
export interface SendMessageDto {
  message: string;
}

// Interface específica para imágenes
export interface SendImageDto {
  imageUrl: string;
  caption: string;
}

// Interface específica para resultados de publicación
export interface ResultadoPublicacion {
  plataforma: string;
  exito: boolean;
  postId?: string; // Opcional según contexto
  error?: string; // Opcional según resultado
  link?: string; // Opcional según plataforma
}
```

#### No hay "Interfaces Gordas"

**Anti-patrón evitado**:

```typescript
// Esto sería una violación del ISP (no implementado)
interface MegaInterface {
  // Demasiadas responsabilidades en una sola interface
  sendMessage(message: string): void;
  uploadImage(image: File): void;
  publishToFacebook(): void;
  publishToInstagram(): void;
  generateAIResponse(): void;
  manageDatabase(): void;
}
```

**Patrón implementado**:

```typescript
// Interfaces segregadas y específicas
interface MessageSender {
  sendMessage(dto: SendMessageDto): Promise<any>;
}

interface ImageUploader {
  uploadImage(dto: SendImageDto): Promise<any>;
}

interface SocialPublisher {
  publish(content: ContenidoRedesSociales): Promise<ResultadoPublicacion[]>;
}
```

### Ventajas del ISP

- Interfaces focalizadas y comprensibles
- Menor acoplamiento
- Implementaciones más simples
- Facilita testing y mocking

## 5. Dependency Inversion Principle (DIP)

> "Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones"

### Implementación en el Proyecto

#### Inyección de Dependencias con NestJS

```typescript
@WebSocketGateway()
export class SocketChatGateway {
  constructor(
    // Depende de abstracciones (interfaces), no implementaciones concretas
    private readonly socketChatService: SocketChatService,
    private readonly mensajesService: MensajesService,
    private readonly redesSocialesService: RedesSocialesService,
  ) {}
}
```

#### Servicios Desacoplados

```typescript
@Injectable()
export class ChatsService {
  constructor(
    // Depende de la abstracción PrismaService, no de implementación concreta
    private readonly prismaService: PrismaService,
  ) {}

  // Usa la abstracción, no sabe de detalles de implementación
  create(createChatDto: CreateChatDto) {
    return this.prismaService.chat.create({ data: createChatDto });
  }
}
```

#### Abstracción de Base de Datos

```typescript
// PrismaService actúa como abstracción
@Injectable()
export class PrismaService extends PrismaClient {
  // Abstrae los detalles de conexión y configuración
}

// Los servicios usan la abstracción, no Prisma directamente
@Injectable()
export class MensajesService {
  constructor(private readonly prisma: PrismaService) {} // Abstracción
}
```

### Beneficios del DIP

- **Testing**: Fácil de mockear dependencias
- **Flexibilidad**: Cambiar implementaciones sin afectar dependientes
- **Desacoplamiento**: Módulos independientes
- **Reutilización**: Servicios reutilizables

## Arquitectura del Proyecto

### Estructura Modular

```
src/
├── app.module.ts           # Módulo principal
├── main.ts                 # Punto de entrada
├── api/                    # APIs externas (Facebook, Instagram, LinkedIn)
│   ├── facebook/
│   ├── instagram/
│   └── linkedIn/
├── chats/                  # Módulo de chats
├── mensajes/               # Módulo de mensajes
├── publicacion/            # Módulo de publicaciones
├── redes-sociales/         # Servicio orquestador de redes sociales
├── socket-chat/            # Gateway WebSocket
├── prisma/                 # Servicio de base de datos
└── utils/                  # Utilidades compartidas
```

### Separación por Capas

#### 1. **Capa de Presentación**

- **Controllers**: Manejan requests HTTP
- **Gateways**: Manejan conexiones WebSocket
- **DTOs**: Validación de datos de entrada

#### 2. **Capa de Lógica de Negocio**

- **Services**: Lógica de aplicación
- **Interfaces**: Contratos entre capas

#### 3. **Capa de Acceso a Datos**

- **PrismaService**: Abstracción de base de datos
- **APIs Externas**: Integración con servicios terceros

#### 4. **Capa de Utilidades**

- **Logger**: Registro de eventos
- **Helpers**: Funciones auxiliares

## Beneficios Obtenidos

### **Mantenibilidad**

- Cambios localizados: modificar una funcionalidad no afecta otras
- Código legible y bien estructurado
- Fácil identificación de responsabilidades

### **Testabilidad**

- Cada servicio es testeable independientemente
- Fácil mocking de dependencias
- Tests unitarios focalizados

### **Escalabilidad**

- Agregar nuevas redes sociales sin modificar código existente
- Extensión de funcionalidades sin romper lo existente
- Arquitectura preparada para crecimiento

### **Reutilización**

- Servicios reutilizables en diferentes contextos
- DTOs compartibles entre módulos
- Abstracciones reutilizables

### **Manejo de Errores**

- Errores localizados y específicos
- Logging estructurado y trazable
- Recuperación elegante de fallos

## Ejemplos Prácticos

### Ejemplo 1: Agregar Nueva Red Social (YouTube)

#### Paso 1: Crear API específica

```typescript
// src/api/youtube/youtube.api.ts
export const uploadYouTubeVideo = async (dto: UploadVideoDto) => {
  // Implementación específica de YouTube
};
```

#### Paso 2: Extender interface (OCP)

```typescript
export interface ContenidoRedesSociales {
  // ... redes existentes
  youtube: {
    title: string;
    description: string;
    tags: string[];
  }; // Solo agregar, no modificar
}
```

#### Paso 3: Extender servicio

```typescript
// En RedesSocialesService
// Publicar en YouTube
try {
  const youtubeResult = await uploadYouTubeVideo({
    title: contenido.youtube.title,
    description: contenido.youtube.description,
    tags: contenido.youtube.tags,
    videoFile: videoFile
  });
  // ... manejo del resultado
} catch (error) { ... }
```

### Ejemplo 2: Testing con DIP

```typescript
// test/chats.service.spec.ts
describe('ChatsService', () => {
  let service: ChatsService;
  let prismaService: jest.Mocked<PrismaService>;

  beforeEach(async () => {
    const mockPrismaService = {
      chat: {
        create: jest.fn(),
        findMany: jest.fn(),
        findUnique: jest.fn(),
        update: jest.fn(),
      },
    };

    const module: TestingModule = await Test.createTestingModule({
      providers: [
        ChatsService,
        { provide: PrismaService, useValue: mockPrismaService }, // Mock fácil
      ],
    }).compile();

    service = module.get<ChatsService>(ChatsService);
    prismaService = module.get(PrismaService);
  });

  it('should create a chat', async () => {
    const createChatDto = { titulo: 'Test Chat' };
    prismaService.chat.create.mockResolvedValue({ id: '1', ...createChatDto });

    const result = await service.create(createChatDto);

    expect(prismaService.chat.create).toHaveBeenCalledWith({
      data: createChatDto,
    });
    expect(result).toEqual({ id: '1', ...createChatDto });
  });
});
```

### Ejemplo 3: Extensión de DTOs (OCP + ISP)

```typescript
// Extensión sin modificar DTOs existentes
export interface CreateChatWithMetadataDto extends CreateChatDto {
  metadata?: {
    tags: string[];
    priority: 'low' | 'medium' | 'high';
    assignedTo?: string;
  };
}

// Uso polimórfico (LSP)
const createChat = (dto: CreateChatDto | CreateChatWithMetadataDto) => {
  // Funciona con ambos tipos sin modificar código existente
  return prismaService.chat.create({ data: dto });
};
```

## Conclusión

El backend LLM es un **excelente ejemplo** de aplicación de principios SOLID en un proyecto real con NestJS. La arquitectura resultante es:

- **Mantenible**: Fácil de modificar y extender
- **Testeable**: Cada componente es testeable independientemente
- **Escalable**: Preparado para crecimiento futuro
- **Legible**: Código claro y bien organizado
- **Robusto**: Manejo elegante de errores y casos edge

Los principios SOLID no son solo teoría académica, sino herramientas prácticas que mejoran significativamente la calidad del código y la experiencia de desarrollo.

---

_Documentación generada para el proyecto Backend LLM - Noviembre 2025_
