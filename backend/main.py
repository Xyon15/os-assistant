"""
backend.main : Backend API de l'assistant IA

Ce fichier crée le serveur web avec FastAPI.
FastAPI reçoit les requêtes HTTP et retourne des réponses JSON.

Documentation FastAPI automatique disponible à :
- /docs (Swagger UI)

"""
# Imports
from contextlib import asynccontextmanager  # Pour gérer le cycle de vie de l'app
from typing import Optional  # Pour déclarer des types optionnels (peut être None)
from fastapi import FastAPI  # Framework web pour créer l'API
from fastapi.middleware.cors import CORSMiddleware  # Pour autoriser les requêtes depuis le navigateur
from pydantic import BaseModel  # Pour valider les données reçues
from backend.memory import initialiser_db, charger_metriques_historiques, incrementer_metriques, logger_requete, recuperer_stats # Mémoire des messages et des métriques
from backend.ai import demander_llm
import logging
import time
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

# Configuration du logger 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),  # Écrit dans fichier
        logging.StreamHandler()  # Affiche dans terminal
    ]
)
logger = logging.getLogger(__name__)

METRIQUES = {
    "total_requetes": 0,
    "total_historique": 0, # Valeur temporaire, sera chargée au démarrage
    "demarrage": time.time()
}
# Gestionnaire du cycle de vie : actions au démarrage et à l'arrêt
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code exécuté AU DÉMARRAGE du serveur
    initialiser_db()  # Démarre la db sqlite
    METRIQUES["total_historique"] = charger_metriques_historiques()  # Charge les métriques historiques
    logger.info("Serveur demarre et pret a recevoir des requetes.")
    yield  # Le serveur tourne (traite les requêtes)
    # Code exécuté À L'ARRÊT du serveur (si besoin, actuellement rien)

# Liste des origines autorisées (frontend)
ALLOWED_ORIGINS = [
    "http://localhost:8000",  # Local dev
    "http://127.0.0.1:8000",  # Local dev
    "http://localhost:5500",  # Live Server VS Code
    "http://127.0.0.1:5500",  # Live Server VS Code
    "null",  # file:// protocol (ouverture directe HTML)
    "https://xyon15.github.io",  # GitHub Pages production
]

# Créer l'application FastAPI avec le gestionnaire de cycle de vie et description sur FastAPI
app = FastAPI(
    lifespan=lifespan,
    title= "Backend API - OS Assistant",
    description= "API backend pour l'assistant IA OS Assistant. Fournit des endpoints pour envoyer des messages et interagir avec le modèle de langage.",
    version="1.1.0",
)

# Configurer CORS : autoriser origines
# Permet au navigateur d'envoyer des requêtes depuis file:// ou localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,  # Autoriser l'envoi de cookies/authentification
    allow_methods=["*"],  # Autoriser toutes les méthodes (GET, POST, OPTIONS...)
    allow_headers=["*"],  # Autoriser tous les headers HTTP
)

@app.exception_handler(Exception)
def gestionnaire_erreurs_global(request: Request, exc: Exception):
    """
    Gestionnaire d'erreurs global pour capturer toutes les exceptions non gérées.
    Log l'erreur et retourne une réponse JSON standardisée.
    """
    logger.error(f"Erreur inattendue: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"erreur": True, "message": "Une erreur interne est survenue. Veuillez réessayer plus tard."},
    )

## Endpoints de monitoring et de health check ##

# Endpoint GET /ping : vérifier que le serveur fonctionne
@app.get("/ping")
def get_ping():
    return {"status": "pong"}

@app.get("/health")
def health_check():
    """
    Endpoint de health check pour vérifier que le serveur est opérationnel.
    Retourne un statut 200 si tout va bien.
    """
    return {"status": "healthy", "uptime": round(time.time() - METRIQUES["demarrage"], 2)}

@app.get("/metrics")
def get_metrics():
    """
    Endpoint pour récupérer les métriques de l'application.
    """
    uptime = int(time.time() - METRIQUES["demarrage"])
    heures = uptime // 3600
    minutes = (uptime % 3600) // 60
    secondes = uptime % 60
    uptime_lisible = f"{heures}h {minutes}m {secondes}s"
    return {
        "total_requetes": METRIQUES["total_requetes"],
        "total_historique": METRIQUES["total_historique"],
        "uptime_seconds": round(time.time() - METRIQUES["demarrage"], 2),
        "uptime_lisible": uptime_lisible
    }

# Endpoint GET /stats : récupérer les statistiques détaillées
@app.get("/stats")
def get_stats():
    """
    Endpoint pour récupérer les statistiques détaillées.
    """
    stats = recuperer_stats()
    return stats

## Modèle Pydantic : définir la structure d'un message valide ##
# texte = obligatoire (str), nom_utilisateur = facultatif (str ou None)
class Message(BaseModel):
    texte: str
    nom_utilisateur: Optional[str] = None

# Modèle Pydantic pour le chat avec le LLM
class ChatMessage(BaseModel):
    message: str


## Endpoints d'échange de messages ##
# Endpoint POST /chat : conversation avec le LLM
@app.post("/chat")
def chat(msg: ChatMessage):
    # Log de la requête reçue
    debut = time.time()
    logger.info(f"Requete recuee pour /chat")

    METRIQUES["total_requetes"] += 1
    METRIQUES["total_historique"] += 1
    incrementer_metriques()  # Incrémente le compteur dans la db

    try:
        reponse_llm, duree_llm = demander_llm(msg.message) # Appeler le LLM pour obtenir une réponse
        
        # Log de la réponse générée
        duree = time.time() - debut
        logger.info(f"Reponse generee en {duree:.2f}s") 

        logger_requete("/chat", duree, duree_llm, "success")  # Logger la requête dans la db (duree = total, duree_llm = temps API LLM)
        return {"reponse": reponse_llm} # Retourner la réponse au frontend
    
    except Exception as e:
        # Log de l'erreur
        duree = time.time() - debut
        logger.error(f"Erreur apres {duree:.2f}s : {str(e)}")

        logger_requete("/chat", duree, None, "error", str(e))  # Logger l'erreur dans la db
        return {"reponse": "Désolé, une erreur est survenue.", "erreur": True,}  # Retourner un message d'erreur au frontend