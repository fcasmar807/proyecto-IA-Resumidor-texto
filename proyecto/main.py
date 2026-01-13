from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Cliente OpenAI usando GitHub Models
client = OpenAI(
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com"
)

app = FastAPI(
    title="Resumidor de Textos con IA (GitHub Models)",
    description="API para resumir textos en español usando IA de GitHub",
    version="1.0.0"
)

# =========================
# MODELOS DE DATOS
# =========================

class TextoEntrada(BaseModel):
    texto: str
    max_palabras: int = 120

class TextoResumen(BaseModel):
    resumen: str

# =========================
# ENDPOINT
# =========================

@app.post("/resumir", response_model=TextoResumen)
def resumir_texto(data: TextoEntrada):
    if not data.texto.strip():
        raise HTTPException(status_code=400, detail="El texto no puede estar vacío")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un experto en resumir textos en español de forma clara y concisa."
                },
                {
                    "role": "user",
                    "content": f"Resume el siguiente texto en un máximo de {data.max_palabras} palabras:\n\n{data.texto}"
                }
            ],
            temperature=0.3
        )

        resumen = response.choices[0].message.content

        return {"resumen": resumen}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
