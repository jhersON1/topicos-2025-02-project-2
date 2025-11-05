from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .services.llm import generate_response, LLMConfigurationError


class ChatPayload(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000)


app = FastAPI(
    title="LLM Commerce · Backend Python",
    description="Endpoint mínimo /chat para interactuar con OpenAI u Ollama",
    version="0.1.0",
)


@app.get("/health", tags=["status"])
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", tags=["chat"])
async def chat(payload: ChatPayload) -> dict[str, str]:
    try:
        reply = await generate_response(payload.message)
    except LLMConfigurationError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return {"reply": reply}
