# syntax=docker/dockerfile:1.6

FROM node:20-alpine AS base
WORKDIR /app

COPY package.json package-lock.json* ./
RUN npm install

COPY tsconfig*.json nest-cli.json jest.config.ts ./
COPY test ./test
COPY src ./src

RUN npm run build

FROM node:20-alpine AS runtime
WORKDIR /app

ENV NODE_ENV=production

COPY --from=base /app/node_modules ./node_modules
COPY --from=base /app/dist ./dist
COPY --from=base /app/src ./src
COPY --from=base /app/test ./test
COPY --from=base /app/jest.config.ts ./jest.config.ts
COPY --from=base /app/tsconfig.json ./tsconfig.json
COPY --from=base /app/tsconfig.build.json ./tsconfig.build.json
COPY --from=base /app/nest-cli.json ./nest-cli.json
COPY --from=base /app/package.json ./package.json
COPY --from=base /app/src/prompts ./src/prompts

EXPOSE 3000

CMD ["npm", "run", "start:prod"]
