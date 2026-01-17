"""
Tests automatisés pour le backend FastAPI

Ce fichier teste les 4 endpoints de l'API :
- GET /ping : Vérifier que le serveur répond
- POST /message : Sauvegarder un message
- GET /messages : Récupérer tous les messages
- POST /chat : Valider les données envoyées au LLM
"""
# Imports pour tester FastAPI avec TestClient
from fastapi.testclient import TestClient
import sys
import os

# Ajouter backend/ au chemin Python pour importer main.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

# Importer l'application FastAPI depuis backend/main.py
from main import app  # type: ignore

# Créer un client de test (simule des requêtes HTTP sans lancer uvicorn)
client = TestClient(app)

# Test 1 : Vérifier que l'endpoint /ping répond correctement
def test_ping():
    # Envoyer requête GET à /ping
    response = client.get("/ping")
    # Vérifier status code 200 (OK)
    assert response.status_code == 200
    # Vérifier réponse JSON {"status": "pong"}
    assert response.json() == {"status": "pong"}

# Test 2 : Vérifier que l'endpoint /message sauvegarde un message
def test_message():
    # Créer un message de test
    payload = {"texte": "Test message"}

    # Envoyer requête POST à /message avec le payload
    response = client.post("/message", json=payload)

    # Vérifier status code 200 (OK)
    assert response.status_code == 200
    # Stocker la réponse JSON
    data = response.json()
    # Vérifier que le backend confirme réception
    assert data["recu"] == True

# Test 3 : Vérifier que l'endpoint /messages retourne une liste
def test_get_messages():
    # Envoyer requête GET à /messages
    response = client.get ("/messages")
    # Vérifier status code 200 (OK)
    assert response.status_code == 200
    # Vérifier que response.json()["messages"] est une liste Python
    assert isinstance(response.json()["messages"], list)

# Test 4 : Vérifier que Pydantic rejette les messages vides
def test_chat_validation():
    # Créer un payload avec contenu vide (invalide)
    payload = {"contenu": ""}
    # Envoyer requête POST à /chat
    response = client.post("/chat", json=payload)
    # Vérifier status code 422 (erreur validation Pydantic)
    assert response.status_code == 422

