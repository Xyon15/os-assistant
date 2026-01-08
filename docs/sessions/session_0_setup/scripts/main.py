# backend/main.py - Session 0
# Premier serveur FastAPI avec endpoint /ping

from fastapi import FastAPI

# Créer une instance de FastAPI
app = FastAPI()

# Définir une route GET sur /ping
@app.get("/ping")
def get_ping():
    """Endpoint de test qui retourne un statut pong"""
    return {"status": "pong"}
