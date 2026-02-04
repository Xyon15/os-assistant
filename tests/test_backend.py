"""
Tests automatisés pour le backend FastAPI

Ce fichier teste les endpoints de l'API :
- GET /ping : Vérifier que le serveur répond
- GET /health : Vérifier health check avec uptime
- GET /metrics : Vérifier métriques (requêtes, uptime)
- GET /stats : Vérifier statistiques DB
- POST /chat : Valider les données envoyées au LLM
"""
# Imports pour tester FastAPI avec TestClient
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
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

# Test 2 : Vérifier que l'endpoint /health retourne status et uptime
def test_health():
    # Envoyer requête GET à /health
    response = client.get("/health")
    # Vérifier status code 200 (OK)
    assert response.status_code == 200
    data = response.json()
    # Vérifier présence des clés obligatoires
    assert "status" in data
    assert "uptime" in data
    assert data["status"] == "healthy"
    # Vérifier que uptime est un nombre positif
    assert isinstance(data["uptime"], (int, float))
    assert data["uptime"] >= 0

# Test 3 : Vérifier que l'endpoint /metrics retourne les métriques
def test_metrics():
    # Envoyer requête GET à /metrics
    response = client.get("/metrics")
    # Vérifier status code 200 (OK)
    assert response.status_code == 200
    data = response.json()
    # Vérifier présence des clés obligatoires
    assert "total_requetes" in data
    assert "total_historique" in data
    assert "uptime_seconds" in data
    assert "uptime_lisible" in data
    # Vérifier types
    assert isinstance(data["total_requetes"], int)
    assert isinstance(data["uptime_lisible"], str)

# Test 4 : Vérifier que l'endpoint /stats retourne les statistiques (avec mock)
@patch('main.recuperer_stats')
def test_stats(mock_recuperer_stats):
    # Mock : retourner des statistiques factices
    mock_recuperer_stats.return_value = {
        "temps_moyen_total": 2.5,
        "temps_moyen_llm": 2.0,
        "total_requetes_logees": 10,
        "total_erreurs": 0
    }
    
    # Envoyer requête GET à /stats
    response = client.get("/stats")
    # Vérifier status code 200 (OK)
    assert response.status_code == 200
    data = response.json()
    # Vérifier que les données mockées sont retournées
    assert data["temps_moyen_total"] == 2.5
    assert data["temps_moyen_llm"] == 2.0
    assert data["total_requetes_logees"] == 10
    assert data["total_erreurs"] == 0

# Test 5 : Vérifier que Pydantic rejette les messages vides
def test_chat_validation():
    # Créer un payload avec contenu vide (invalide)
    payload = {"contenu": ""}
    # Envoyer requête POST à /chat
    response = client.post("/chat", json=payload)
    # Vérifier status code 422 (erreur validation Pydantic)
    assert response.status_code == 422


