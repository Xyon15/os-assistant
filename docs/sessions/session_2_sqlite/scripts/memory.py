"""
memory.py : Module qui gère la mémoire de l'assistant IA grâce à une db SQLite

Ce module permet de sauvegarder et récupérer les messages dans une base de données.
La base de données est un fichier "memory.db" qui ne s'efface jamais (même si on redémarre).

Fonctions disponibles : 
- initialiser_db() : Créer la table "messages" dans la base de données
- sauvegarder_message(texte, nom_utilisateur) : Ajouter un message dans la db
- recuperer_messages() : Récupérer tous les messages sauvegardés

Exemple d'utilisation :
    from backend.memory import initialiser_db, sauvegarder_message
    
    initialiser_db()  # Créer la base (une seule fois au démarrage)
    sauvegarder_message("Bonjour !", "Alice")  # Sauvegarder un message

"""

# Imports
import sqlite3
from datetime import datetime


def initialiser_db(): # Fonction qui permet de créer et préparer la db
    # Ouvre/crée le fichier memory.db (comme un classeur Excel qui ne s'efface jamais)
    connexion = sqlite3.connect("memory.db")
    
    # Crée la table "messages" si elle n'existe pas encore (IF NOT EXISTS = sécurité)
    # Colonnes : id (auto), texte (message), nom_utilisateur (qui), date_creation (quand)
    connexion.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texte TEXT,
            nom_utilisateur TEXT,
            date_creation TEXT
        )                                
    """)
    connexion.commit() # Enregistrer les modifications
    connexion.close() # Fermer la connexion

def sauvegarder_message(texte, nom_utilisateur):  # Fonction pour ajouter un message dans la db
    # Ouvrir la connexion à la base de données
    connexion = sqlite3.connect("memory.db")
    
    # Récupérer la date et l'heure actuelles (format ISO : 2026-01-08T14:30:00)
    date_maintenant = datetime.now().isoformat()
    
    # Insérer une nouvelle ligne dans la table messages (les ? sont remplacés par les valeurs du tuple)
    connexion.execute("""
        INSERT INTO messages (texte, nom_utilisateur, date_creation) 
        VALUES (?, ?, ?)
    """, (texte, nom_utilisateur, date_maintenant))
    
    connexion.commit()  # Enregistrer les modifications
    connexion.close()   # Fermer la connexion
    return True  # Retourner True pour dire "c'est bon !"

def recuperer_messages(): # Fonction pour récupérer tous les messages de la db
    # Ouvrir la connexion à la base de données
    connexion = sqlite3.connect("memory.db")
    
    # Exécuter la requête SELECT et stocker le cursor (pour pouvoir faire fetchall)
    cursor = connexion.execute("SELECT * FROM messages")
    
    # Récupérer TOUTES les lignes (c'est une liste de tuples)
    lignes = cursor.fetchall()
    
    # Créer une liste vide pour stocker les résultats
    resultats = []
    
    # Boucler sur chaque ligne et la transformer en dictionnaire
    for ligne in lignes:
        message = {
            "id": ligne[0],
            "texte": ligne[1],
            "nom_utilisateur": ligne[2],
            "date_creation": ligne[3]
        }
        resultats.append(message)  # Ajouter le message à la liste
    
    connexion.close()  # Fermer la connexion
    return resultats  # Retourner la liste de tous les messages
