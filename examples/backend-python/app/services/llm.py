import json
import os
from pathlib import Path
from typing import Any

import httpx


class LLMConfigurationError(RuntimeError):
    """Señala que falta configuración para el proveedor seleccionado."""


async def generate_response(user_message: str) -> str:
    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    if provider == "openai":
        return await _call_openai(user_message)
    if provider == "ollama":
        return await _call_ollama(user_message)
    raise LLMConfigurationError(f"LLM_PROVIDER '{provider}' no está soportado. Usa 'openai' u 'ollama'.")


async def _call_openai(user_message: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise LLMConfigurationError("OPENAI_API_KEY is required when LLM_PROVIDER=openai.")

    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    temperature = float(os.getenv("OPENAI_TEMPERATURE", "0.4"))

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": _load_system_prompt()},
            {"role": "user", "content": user_message},
        ],
        "temperature": temperature,
    }

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(f"{base_url}/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

    return _extract_message(data)


async def _call_ollama(user_message: str) -> str:
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/")
    model = os.getenv("OLLAMA_MODEL", "llama3.1")

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": _load_system_prompt()},
            {"role": "user", "content": user_message},
        ],
        "stream": False,
    }

    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.post(f"{base_url}/api/chat", json=payload)
        response.raise_for_status()
        data = response.json()

    message = data.get("message") or {}
    content = message.get("content")
    if not content:
        raise RuntimeError("Ollama no devolvió contenido en la respuesta.")
    return content


def _load_system_prompt() -> str:
    env_path = os.getenv("SYSTEM_PROMPT_PATH")
    if env_path:
        candidate = Path(env_path).expanduser()
        if not candidate.is_absolute():
            candidate = Path.cwd() / candidate
    else:
        candidate = Path(__file__).resolve().parents[1] / "prompts" / "system.txt"

    try:
        return candidate.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise LLMConfigurationError(
            f"No se encontró el prompt base en {candidate}. Ajusta SYSTEM_PROMPT_PATH."
        ) from exc


def _extract_message(data: dict[str, Any]) -> str:
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"No se pudo procesar la respuesta del modelo: {json.dumps(data)}") from exc
