"""
backend.main : Backend API de l'assistant IA

Ce fichier crée le serveur web avec FastAPI.
FastAPI reçoit les requêtes HTTP et retourne des réponses JSON.

Documentation FastAPI automatique disponible à :
- /docs (Swagger UI)

"""
## Imports

# Bibliothèque standard Python
import os
import time
import logging
from contextlib import asynccontextmanager  # Pour gérer le cycle de vie de l'app
from typing import Optional  # Pour déclarer des types optionnels (peut être None)

# FastAPI & Pydantic
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware  # Pour autoriser les requêtes depuis le navigateur
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr  # Pour valider les données reçues

# Librairies tierces
import psycopg2 # Pour interagir avec la base de données PostgreSQL

# Modules locaux
from backend.memory import initialiser_db, charger_metriques_historiques, incrementer_metriques, logger_requete, recuperer_stats  # Mémoire des messages et des métriques
from backend.ai import demander_llm
from backend.auth import hash_password, verify_password, create_access_token, get_current_user

##

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
    title= "Backend API - Workly",
    description= "API backend pour l'assistant IA Workly. Fournit des endpoints pour envoyer des messages et interagir avec le modèle de langage.",
    version="1.2.0",
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

## Modèle Pydantic : définir la structure d'un message valide ##
# texte = obligatoire (str), nom_utilisateur = facultatif (str ou None)
class Message(BaseModel):
    texte: str
    nom_utilisateur: Optional[str] = None

# Modèle Pydantic pour le chat avec le LLM
class ChatMessage(BaseModel):
    message: str

class UserRegister(BaseModel):
    username : str
    email : EmailStr  # Validation format email (ex: testnimp@a sera rejeté)
    password : str

class UserLogin(BaseModel):
    username : str
    password : str


########################## Endpoints de monitoring et de health check ##########################

# Endpoint GET /ping : vérifier que le serveur fonctionne
@app.get("/ping")
def get_ping():
    return {"status": "pong"}

# Endpoint GET /me : vérifier que le token JWT est encore valide
@app.get("/me")
def get_me(username: str = Depends(get_current_user)):
    # get_current_user lève automatiquement 401 si le token est expiré ou invalide
    return {"username": username}

# Endpoint GET /health : vérifier que le serveur est opérationnel
@app.get("/health")
def health_check():
    """
    Endpoint de health check pour vérifier que le serveur est opérationnel.
    Retourne un statut 200 si tout va bien.
    """
    return {"status": "healthy", "uptime": round(time.time() - METRIQUES["demarrage"], 2)}

# Endpoint GET /metrics : récupérer les métriques d'utilisation
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


########################## Endpoints d'échange de messages ##########################

# Endpoint POST /chat : conversation avec le LLM
@app.post("/chat")
def chat(msg: ChatMessage, current_user: str = Depends(get_current_user)):
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

########################## Endpoints d'authentification ##########################

# Endpoint POST /register : créer un nouveau compte utilisateur
@app.post("/register")
def register(user: UserRegister):
    logger.info(f"Tentative de création de compte : {user.username}")

    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = conn.cursor()

    hashed = hash_password(user.password)

    try:
        cursor.execute("INSERT INTO users (username, email, hashed_password) VALUES (%s, %s, %s)", (user.username, user.email, hashed))
        conn.commit()
        logger.info(f"Compte cree pour : {user.username}")
    except Exception as e:
        conn.rollback()  # Annuler la transaction en cas d'erreur
        erreur = str(e)
        logger.warning(f"Erreur lors de l'insertion : {erreur}")
        # Erreur de contrainte UNIQUE PostgreSQL : e.pgcode == "23505"
        pgcode = getattr(e, "pgcode", "")  # Récupérer le code d'erreur PostgreSQL (ou "" si absent)
        if pgcode == "23505":
            if "username" in erreur:
                raise HTTPException(status_code=400, detail="Ce nom d'utilisateur est déjà pris.")
            elif "email" in erreur:
                raise HTTPException(status_code=400, detail="Cette adresse email est déjà utilisée.")
        raise HTTPException(status_code=400, detail="Erreur lors de la création du compte.")
    finally:
        cursor.close()
        conn.close()
    return {"message": "Compte créé avec succès"}


# Endpoint POST /login : authentifier un utilisateur et retourner un token JWT
@app.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    logger.info(f"Tentative de connexion : {form.username}")

    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = conn.cursor()

    try:
        # Login par username
        cursor.execute("SELECT hashed_password FROM users WHERE username = %s", (form.username,))
        result = cursor.fetchone() # result = (hashed_password,) ou None
        
        if not result:
            logger.warning(f"Utilisateur introuvable : {form.username}")
            raise HTTPException(status_code=401, detail="Identifiants incorrects")
        
        if not verify_password(form.password, result[0]):
            logger.warning(f"Mot de passe incorrect pour : {form.username}")
            raise HTTPException(status_code=401, detail="Identifiants incorrects")
        
        token = create_access_token({"sub": form.username}) # JWT avec le username
        logger.info(f"Login reussi pour : {form.username}")
        
        return {"access_token": token, "token_type": "bearer", "username": form.username}
    
    finally:
        cursor.close()
        conn.close()