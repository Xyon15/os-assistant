"""
backend.auth - Module de gestion de l'authentification et de la sécurité

Ce module fournit des fonctions pour le hachage des mots de passe, la vérification des mots de passe, et la création de tokens JWT pour l'authentification.

Fonctions :
- hash_password(password): Hache un mot de passe en utilisant bcrypt.
- verify_password(plain, hashed): Vérifie/Compare si le mot de passe en clair correspond au hash.
- create_access_token(data): Crée un token JWT avec les données fournies et une date

"""
# Imports
import os
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Charger variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "changeme")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# Hasher le password
def hash_password(password):
    return pwd_context.hash(password)

# Vérifier si le hash correspond au mdp
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# Créer le token jwt
def create_access_token(data: dict):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=int(EXPIRE_MINUTES))
    payload.update({"exp": expire})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# Récupérer l'utilisateur courant à partir du token JWT (fonction utilitaire pour les endpoints protégés)
def get_current_user(token: str = Depends(oauth2_scheme)):
    # token est injecté automatiquement par oauth2_scheme
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")  # Extraire le nom d'utilisateur du payload
        if username is None:
            raise HTTPException(status_code=401, detail="Token invalide")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalide ou expiré")