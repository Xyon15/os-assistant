"""
Module pour interagir avec le LLM via l'API GitHub Models.

Fonctions disponibles :
- demander_llm(prompt: str) -> str : Appelle GPT-4o et retourne la réponse

"""

# Imports
import os
import requests
import time
from dotenv import load_dotenv
import logging

# Charger les variables du fichier .env
load_dotenv()

# Configurer le logger
logger = logging.getLogger(__name__)

def demander_llm(prompt: str) -> tuple[str, float]:
    """
    Appelle l'API GitHub Models (GPT-4o) pour obtenir une réponse.
    Réessaie 3 fois en cas d'erreur.
    
    Args:
        prompt: La question de l'utilisateur
    
    Returns:
        La réponse du LLM ou un message d'erreur poli
    """
    
    # Récupérer le token depuis .env
    token = os.getenv("GITHUB_TOKEN")
    
    # Vérifier que le token existe
    if not token:
        return "Erreur : token GitHub manquant dans .env", 0.0
    
    # Préparer l'URL et les headers
    url = "https://models.inference.ai.azure.com/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    
    # Préparer les données JSON (body de la requête)
    # Récupérer le modèle depuis .env
    model_name = os.getenv("MODEL_NAME")
    
    # Vérifier que le modèle existe
    if not model_name:
        return "Erreur : MODEL_NAME manquant dans .env", 0.0
    
    # Préparer les données JSON (body de la requête)
    donnees = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    logger.info(f"Appel a l'API LLM")
    debut = time.time()
    # Boucle pour réessayer 3 fois
    for tentative in range(1, 4):
        try:
            # Envoyer la requête POST
            reponse = requests.post(url, headers=headers, json=donnees)
            
            # Vérifier que la requête a réussi (status 200)
            if reponse.status_code == 200:
                # Extraire le texte de la réponse
                resultat = reponse.json()
                texte_llm = resultat["choices"][0]["message"]["content"]
                duree = time.time() - debut
                logger.info(f"Reponse recue de l'API LLM en {duree:.2f}s")
                return texte_llm, duree
            else:
                logger.warning(f"Tentative {tentative} échouée : status {reponse.status_code}")
        
        except Exception as e:
            logger.error(f"Tentative {tentative} erreur : {e}")
        
        # Attendre 2 secondes avant de réessayer (sauf dernière tentative)
        if tentative < 3:
            time.sleep(2)

    duree = time.time() - debut
    # Si les 3 tentatives échouent, retourner message poli
    return "Désolé, le service est temporairement indisponible. Veuillez réessayer plus tard.", duree