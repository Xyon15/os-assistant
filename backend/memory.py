"""
memory.py : Module qui gère les métriques de l'assistant IA grâce à une db PostgreSQL

Ce module permet de sauvegarder et récupérer les métriques et logs dans une base de données cloud.

"""

# Imports
import psycopg2
from datetime import datetime, timezone
import os
from dotenv import load_dotenv


# Charger les variables d'environnement depuis .env
load_dotenv()


def get_connexion():
    """Créer une connexion PostgreSQL depuis la variable d'environnement DATABASE_URL"""
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL manquante dans .env")
    return psycopg2.connect(database_url)


def initialiser_db(): # Fonction qui permet de créer et préparer la db
    # Ouvre/crée une connexion à PostgreSQL (cloud database)
    connexion = get_connexion()

    curseur = connexion.cursor()
    
    # Créer la table "metriques" si elle n'existe pas (syntaxe PostgreSQL)
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS metriques (
            id INTEGER PRIMARY KEY,
            total_historique INTEGER
        )
    """)
    
    # Initialiser le compteur à 0 si la table est vide (PostgreSQL : ON CONFLICT)
    curseur.execute("""
        INSERT INTO metriques (id, total_historique) 
        VALUES (1, 0) 
        ON CONFLICT (id) DO NOTHING
    """)

    # Créer la table "logs" pour statistiques (PostgreSQL : SERIAL au lieu de AUTOINCREMENT)
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id SERIAL PRIMARY KEY,
            timestamp TEXT,
            endpoint TEXT,
            duree_totale REAL,
            duree_llm REAL,
            status TEXT,
            erreur_details TEXT
        )
    """)

    connexion.commit() # Enregistrer les modifications
    curseur.close()
    connexion.close() # Fermer la connexion

## Fonctions pour gérer les métriques ##
def charger_metriques_historiques():
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("SELECT total_historique FROM metriques WHERE id = 1")
    resultat = curseur.fetchone()
    curseur.close()
    connexion.close()
    return resultat[0] if resultat else 0

def incrementer_metriques():
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("UPDATE metriques SET total_historique = total_historique + 1 WHERE id = 1")
    connexion.commit()
    curseur.close()
    connexion.close()

def logger_requete(endpoint, duree_totale, duree_llm=None, status="success", erreur_details=None):
    connexion = get_connexion()
    curseur = connexion.cursor()
    # Timestamp en UTC
    timestamp = datetime.now(timezone.utc).isoformat()
    curseur.execute("""
        INSERT INTO logs (timestamp, endpoint, duree_totale, duree_llm, status, erreur_details)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (timestamp, endpoint, duree_totale, duree_llm, status, erreur_details))
    connexion.commit()
    curseur.close()
    connexion.close()

def recuperer_stats():
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("""
        SELECT 
            AVG(duree_totale) as duree_moy,
            AVG(duree_llm) as llm_moy,
            COUNT(*) as total,
            SUM(CASE WHEN status = 'error' THEN 1 ELSE 0 END) as erreurs
        FROM logs
    """)
    stats = curseur.fetchone()
    curseur.close()
    connexion.close()
    
    # Si aucun log, retourner des valeurs par défaut
    if not stats or stats[0] is None:
        return {
            "temps_moyen_total": 0,
            "temps_moyen_llm": 0,
            "total_requetes_logees": 0,
            "total_erreurs": 0
        }
    
    return {
        "temps_moyen_total": round(stats[0], 2),
        "temps_moyen_llm": round(stats[1], 2) if stats[1] else 0,
        "total_requetes_logees": stats[2],
        "total_erreurs": stats[3]
    }