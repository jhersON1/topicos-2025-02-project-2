from .adapters import facebook, instagram, linkedin
from .llm_client import LLMClient

ADAPTERS = {
    "facebook": facebook.FacebookAdapter(),
    "instagram": instagram.InstagramAdapter(),
    "linkedin": linkedin.LinkedInAdapter()
}

def generate_content(title: str, body: str, network: str):
    adapter = ADAPTERS.get(network)
    if not adapter:
        return {"error": f"Red social '{network}' no soportada."}
    prompt = adapter.build_prompt(title, body)
    llm = LLMClient()
    result = llm.generate(prompt)
    return {"network": network, "content": result}
