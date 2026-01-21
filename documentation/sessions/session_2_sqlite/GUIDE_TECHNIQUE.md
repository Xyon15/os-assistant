# Guide Technique — Session 2 : SQLite

> Documentation détaillée du code créé lors de la Session 2

---

## 📋 Table des matières

1. [Module memory.py](#module-memorypy)
2. [Intégration dans main.py](#intégration-dans-mainpy)
3. [Explications SQL](#explications-sql)
4. [Analogies et concepts](#analogies-et-concepts)

---

## Module memory.py

### Vue d'ensemble

Fichier : `backend/memory.py`  
Rôle : Gérer la persistance des messages dans SQLite

### Structure

```python
# Imports
import sqlite3
from datetime import datetime

# 3 fonctions publiques
def initialiser_db()          # Créer la table
def sauvegarder_message()     # Ajouter un message
def recuperer_messages()       # Lire tous les messages
```

---

### Fonction 1 : `initialiser_db()`

#### Code complet

```python
def initialiser_db():
    # Ouvre/crée le fichier memory.db
    connexion = sqlite3.connect("memory.db")

    # Crée la table "messages" si elle n'existe pas
    connexion.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texte TEXT,
            nom_utilisateur TEXT,
            date_creation TEXT
        )
    """)
    connexion.commit()
    connexion.close()
```

#### Explications ligne par ligne

| Ligne                                  | Explication                                             |
| -------------------------------------- | ------------------------------------------------------- |
| `sqlite3.connect("memory.db")`         | Ouvre le fichier memory.db (le crée s'il n'existe pas)  |
| `CREATE TABLE IF NOT EXISTS`           | Crée la table seulement si elle n'existe pas déjà       |
| `id INTEGER PRIMARY KEY AUTOINCREMENT` | Colonne id : nombre unique auto-incrémenté (1, 2, 3...) |
| `texte TEXT`                           | Colonne texte : contient le message (type texte)        |
| `nom_utilisateur TEXT`                 | Colonne nom_utilisateur : qui a envoyé (type texte)     |
| `date_creation TEXT`                   | Colonne date : quand le message a été envoyé            |
| `connexion.commit()`                   | Sauvegarde les changements dans le fichier              |
| `connexion.close()`                    | Ferme la connexion (libère les ressources)              |

#### Pourquoi cette fonction ?

- **Idempotente** : Peut être appelée plusieurs fois sans erreur (IF NOT EXISTS)
- **Appelée au démarrage** : FastAPI l'appelle une fois au lancement
- **Garantit la structure** : Si memory.db n'existe pas, il est créé

---

### Fonction 2 : `sauvegarder_message(texte, nom_utilisateur)`

#### Code complet

```python
def sauvegarder_message(texte, nom_utilisateur):
    connexion = sqlite3.connect("memory.db")

    date_maintenant = datetime.now().isoformat()

    connexion.execute("""
        INSERT INTO messages (texte, nom_utilisateur, date_creation)
        VALUES (?, ?, ?)
    """, (texte, nom_utilisateur, date_maintenant))

    connexion.commit()
    connexion.close()
    return True
```

#### Explications ligne par ligne

| Ligne                                       | Explication                                       |
| ------------------------------------------- | ------------------------------------------------- |
| `datetime.now().isoformat()`                | Date actuelle au format ISO (2026-01-08T14:30:00) |
| `INSERT INTO messages (...)`                | Ajouter une nouvelle ligne dans la table messages |
| `VALUES (?, ?, ?)`                          | Placeholders (?) pour les valeurs (sécurité)      |
| `(texte, nom_utilisateur, date_maintenant)` | Tuple avec les valeurs qui remplacent les ?       |
| `return True`                               | Retourne True pour confirmer succès               |

#### Sécurité : Pourquoi les `?` ?

**Mauvaise méthode (dangereuse) :**

```python
# ❌ NE JAMAIS FAIRE ÇA
connexion.execute(f"INSERT INTO messages VALUES ('{texte}')")
```

**Problème :** Injection SQL ! Si `texte = "'; DROP TABLE messages; --"`, la table est supprimée !

**Bonne méthode (sécurisée) :**

```python
# ✅ SQLite échappe automatiquement les valeurs
connexion.execute("INSERT ... VALUES (?, ?)", (texte, nom))
```

---

### Fonction 3 : `recuperer_messages()`

#### Code complet

```python
def recuperer_messages():
    connexion = sqlite3.connect("memory.db")

    cursor = connexion.execute("SELECT * FROM messages")
    lignes = cursor.fetchall()

    resultats = []
    for ligne in lignes:
        message = {
            "id": ligne[0],
            "texte": ligne[1],
            "nom_utilisateur": ligne[2],
            "date_creation": ligne[3]
        }
        resultats.append(message)

    connexion.close()
    return resultats
```

#### Explications détaillées

**1. Exécuter la requête SELECT**

```python
cursor = connexion.execute("SELECT * FROM messages")
```

- `SELECT *` = "Donne-moi toutes les colonnes"
- `FROM messages` = "De la table messages"
- Retourne un **cursor** (pointeur sur les résultats)

**2. Récupérer toutes les lignes**

```python
lignes = cursor.fetchall()
```

- `fetchall()` = Récupère TOUTES les lignes
- Retourne une **liste de tuples** :
  ```python
  [
      (1, "Salut", "Alice", "2026-01-08T14:30:00"),
      (2, "Bonjour", "Bob", "2026-01-08T14:31:00")
  ]
  ```

**3. Transformer en dictionnaires**

```python
for ligne in lignes:
    message = {
        "id": ligne[0],        # Premier élément du tuple
        "texte": ligne[1],     # Deuxième élément
        ...
    }
    resultats.append(message)
```

- **Pourquoi ?** Les dictionnaires sont plus lisibles en JSON
- **Résultat final :**
  ```python
  [
      {"id": 1, "texte": "Salut", "nom_utilisateur": "Alice", ...},
      {"id": 2, "texte": "Bonjour", "nom_utilisateur": "Bob", ...}
  ]
  ```

---

## Intégration dans main.py

### Lifespan : Cycle de vie de FastAPI

#### Code complet

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code exécuté AU DÉMARRAGE
    initialiser_db()
    yield
    # Code exécuté À L'ARRÊT (actuellement rien)

app = FastAPI(lifespan=lifespan)
```

#### Explications

| Élément                      | Explication                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| `@asynccontextmanager`       | Décorateur pour créer un gestionnaire de contexte asynchrone |
| `async def lifespan()`       | Fonction asynchrone qui gère le cycle de vie                 |
| `initialiser_db()`           | Appelé UNE SEULE FOIS au démarrage                           |
| `yield`                      | "Pause" → le serveur traite les requêtes                     |
| Code après `yield`           | Exécuté à l'arrêt (nettoyage, fermeture connexions)          |
| `FastAPI(lifespan=lifespan)` | Passe le gestionnaire à FastAPI                              |

#### Analogie : Restaurant

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 🌅 MATIN : Ouvrir le restaurant
    initialiser_db()      # Préparer les tables, allumer les cuisines

    yield                 # 🍽️ JOURNÉE : Servir les clients

    # 🌙 SOIR : Fermer le restaurant
    # nettoyer(), eteindre_tout()
```

---

### Endpoint POST `/message` modifié

#### Code complet

```python
@app.post("/message")
def recevoir_message(msg: Message):
    sauvegarder_message(msg.texte, msg.nom_utilisateur or "Anonyme")
    return {"recu": True}
```

#### Changements par rapport à Session 1

| Session 1 (ancien)                | Session 2 (nouveau)                             |
| --------------------------------- | ----------------------------------------------- |
| Valide et retourne le message     | Valide, **sauvegarde dans SQLite**, et confirme |
| Données perdues après redémarrage | **Données persistantes**                        |

---

### Endpoint GET `/messages` (nouveau)

#### Code complet

```python
@app.get("/messages")
def lire_messages():
    messages = recuperer_messages()
    return {"messages": messages, "total": len(messages)}
```

#### Explication

- Appelle `recuperer_messages()` qui retourne une liste
- `len(messages)` = nombre total de messages (pratique pour le frontend)
- Retourne un dictionnaire avec 2 clés : `messages` et `total`

#### Exemple de réponse

```json
{
  "messages": [
    {
      "id": 1,
      "texte": "Premier message",
      "nom_utilisateur": "Alice",
      "date_creation": "2026-01-08T14:30:00.123456"
    },
    {
      "id": 2,
      "texte": "Deuxième message",
      "nom_utilisateur": "Bob",
      "date_creation": "2026-01-08T14:31:00.789012"
    }
  ],
  "total": 2
}
```

---

## Explications SQL

### Commandes SQL utilisées

#### 1. CREATE TABLE

```sql
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texte TEXT,
    nom_utilisateur TEXT,
    date_creation TEXT
)
```

| Élément               | Explication                                             |
| --------------------- | ------------------------------------------------------- |
| `CREATE TABLE`        | Créer une nouvelle table                                |
| `IF NOT EXISTS`       | Seulement si elle n'existe pas déjà (évite les erreurs) |
| `messages`            | Nom de la table                                         |
| `INTEGER PRIMARY KEY` | Colonne id : nombre entier, clé primaire (unique)       |
| `AUTOINCREMENT`       | SQLite incrémente automatiquement (1, 2, 3...)          |
| `TEXT`                | Type de données : texte (chaîne de caractères)          |

#### 2. INSERT INTO

```sql
INSERT INTO messages (texte, nom_utilisateur, date_creation)
VALUES (?, ?, ?)
```

| Élément                                   | Explication                          |
| ----------------------------------------- | ------------------------------------ |
| `INSERT INTO messages`                    | Ajouter dans la table messages       |
| `(texte, nom_utilisateur, date_creation)` | Colonnes à remplir                   |
| `VALUES (?, ?, ?)`                        | Valeurs à insérer (? = placeholders) |

#### 3. SELECT

```sql
SELECT * FROM messages
```

| Élément         | Explication           |
| --------------- | --------------------- |
| `SELECT`        | Récupérer des données |
| `*`             | Toutes les colonnes   |
| `FROM messages` | De la table messages  |

---

## Analogies et concepts

### Analogie : SQLite = Classeur Excel

| Concept SQL                     | Analogie Excel             |
| ------------------------------- | -------------------------- |
| **Base de données** (memory.db) | Fichier Excel (.xlsx)      |
| **Table** (messages)            | Onglet dans le classeur    |
| **Colonnes** (id, texte, ...)   | Colonnes A, B, C, D        |
| **Lignes**                      | Lignes 1, 2, 3...          |
| **INSERT**                      | Ajouter une nouvelle ligne |
| **SELECT**                      | Lire des lignes            |

### Différences clés

| Caractéristique | Excel                               | SQLite                   |
| --------------- | ----------------------------------- | ------------------------ |
| **Format**      | Binaire propriétaire                | Standard ouvert          |
| **Performance** | Lent avec beaucoup de lignes        | Rapide (indexé)          |
| **Requêtes**    | Filtres manuels                     | Langage SQL puissant     |
| **Concurrence** | Problèmes si plusieurs utilisateurs | Gère bien la concurrence |
| **Sécurité**    | Pas de protection injections        | Protections intégrées    |

---

## Résumé : Flux complet

### 1. Au démarrage du serveur

```
FastAPI démarre
    ↓
lifespan() s'exécute
    ↓
initialiser_db() est appelé
    ↓
Table "messages" créée (si n'existe pas)
    ↓
yield → Serveur prêt à recevoir des requêtes
```

### 2. Recevoir un message (POST /message)

```
Client envoie JSON → {"texte": "Salut", "nom_utilisateur": "Alice"}
    ↓
Pydantic valide les données
    ↓
recevoir_message(msg) appelé
    ↓
sauvegarder_message("Salut", "Alice")
    ↓
INSERT INTO messages ... (SQL)
    ↓
Message sauvegardé dans memory.db
    ↓
return {"recu": True}
```

### 3. Récupérer les messages (GET /messages)

```
Client demande GET /messages
    ↓
lire_messages() appelé
    ↓
recuperer_messages() appelé
    ↓
SELECT * FROM messages (SQL)
    ↓
Transformation tuples → dictionnaires
    ↓
return {"messages": [...], "total": 5}
```

---

_Dernière mise à jour : 2026-01-08_
