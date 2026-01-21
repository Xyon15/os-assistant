"""
backend.main : Backend API de l'assistant IA

Ce fichier crée le serveur web avec FastAPI.
FastAPI reçoit les requêtes HTTP et retourne des réponses JSON.

Endpoints disponibles :
- GET /ping : Test de connexion (retourne "pong")
- POST /message : Recevoir et valider un message utilisateur

"""
# Imports
from contextlib import asynccontextmanager  # Pour gérer le cycle de vie de l'app
from typing import Optional  # Pour déclarer des types optionnels (peut être None)
from fastapi import FastAPI  # Framework web pour créer l'API
from pydantic import BaseModel  # Pour valider les données reçues
from backend.memory import initialiser_db, sauvegarder_message, recuperer_messages
from backend.ai import demander_llm

# Gestionnaire du cycle de vie : actions au démarrage et à l'arrêt
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code exécuté AU DÉMARRAGE du serveur
    initialiser_db()  # Créer la table "messages" si elle n'existe pas
    yield  # Le serveur tourne (traite les requêtes)
    # Code exécuté À L'ARRÊT du serveur (si besoin, actuellement rien)

# Créer l'application FastAPI avec le gestionnaire de cycle de vie
app = FastAPI(lifespan=lifespan)

# Endpoint GET /ping : vérifier que le serveur fonctionne
@app.get("/ping")
def get_ping():
    return {"status": "pong"}

# Modèle Pydantic : définir la structure d'un message valide
# texte = obligatoire (str), nom_utilisateur = facultatif (str ou None)
class Message(BaseModel):
    texte: str
    nom_utilisateur: Optional[str] = None

# Modèle Pydantic pour le chat avec le LLM
class ChatMessage(BaseModel):
    message: str

# Endpoint POST /message : recevoir un message et le valider
@app.post("/message")
def recevoir_message(msg: Message):
    # Pydantic vérifie automatiquement que "texte" est présent
    # Si nom_utilisateur est None, on utilise "Anonyme"
    sauvegarder_message(msg.texte, msg.nom_utilisateur or "Anonyme")
    return {"recu": True}

# Endpoint GET /messages : récupérer tous les messages sauvegardés
@app.get("/messages")
def lire_messages():
    # Appeler la fonction pour récupérer tous les messages de la DB
    messages = recuperer_messages()
    return {"messages": messages, "total": len(messages)}

# Endpoint POST /chat : conversation avec le LLM
@app.post("/chat")
def chat(msg: ChatMessage):
    # Sauvegarder le message utilisateur avec role="user"
    sauvegarder_message(msg.message, "Utilisateur", role="user")
    
    # Appeler le LLM pour obtenir une réponse
    reponse_llm = demander_llm(msg.message)
    
    # Sauvegarder la réponse du LLM avec role="assistant"
    sauvegarder_message(reponse_llm, "Assistant", role="assistant")
    
    # Retourner la réponse au frontend
    return {"reponse": reponse_llm}