"""
backend.main : Backend API de l'assistant IA (VERSION SESSION 4)

Modifications Session 4 :
- Ajout middleware CORS pour autoriser requêtes frontend
"""
# Imports
from contextlib import asynccontextmanager
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ← AJOUTÉ Session 4
from pydantic import BaseModel
from backend.memory import initialiser_db, sauvegarder_message, recuperer_messages
from backend.ai import demander_llm

# Gestionnaire du cycle de vie
@asynccontextmanager
async def lifespan(app: FastAPI):
    initialiser_db()
    yield

# Créer l'application FastAPI
app = FastAPI(lifespan=lifespan)

# ← AJOUTÉ Session 4 : Configurer CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # "*" = autoriser TOUTES les origines (OK pour dev local)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint GET /ping
@app.get("/ping")
def get_ping():
    return {"status": "pong"}

# Modèle Pydantic pour validation
class Message(BaseModel):
    texte: str
    nom_utilisateur: Optional[str] = None

# Endpoint POST /message
@app.post("/message")
def post_message(message: Message):
    sauvegarder_message(message.texte, message.nom_utilisateur or "Anonyme")
    return {"status": "ok", "message_recu": message.texte}

# Endpoint GET /messages
@app.get("/messages")
def get_messages():
    messages = recuperer_messages()
    return {"messages": messages}

# Modèle Pydantic pour chat
class ChatMessage(BaseModel):
    message: str

# Endpoint POST /chat
@app.post("/chat")
def chat(msg: ChatMessage):
    sauvegarder_message(msg.message, "Utilisateur", role="user")
    reponse_llm = demander_llm(msg.message)
    sauvegarder_message(reponse_llm, "Assistant", role="assistant")
    return {"reponse": reponse_llm}
