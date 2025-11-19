from fastapi import FastAPI
from pydantic import BaseModel, Field
from .content_engine import generate_content

app = FastAPI(
    title="Social Content LLM API",
    description="API para generar contenido para Facebook, Instagram y LinkedIn usando LLM.",
    version="1.0.0"
)

class ContentRequest(BaseModel):
    title: str = Field(..., example="Lanzamiento de nuevo producto")
    body: str = Field(..., example="Hoy presentamos nuestra nueva línea de productos...")
    network: str = Field(..., example="facebook")

@app.post("/generate", summary="Genera contenido para la red social especificada.")
async def generate(req: ContentRequest):
    return generate_content(req.title, req.body, req.network)
