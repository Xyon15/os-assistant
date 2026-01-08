from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
def get_ping():
    return {"status": "pong"}

class Message(BaseModel):
    texte: str
    nom_utilisateur: str = None

@app.post("/message")
def recevoir_message(msg: Message):
    return {
        "recu": True,
        "texte": msg.texte,
        "utilisateur": msg.nom_utilisateur or "Anonyme"
    }
