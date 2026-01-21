# Guide Technique — Session 3 : Intégration LLM API

> **Documentation détaillée ligne par ligne**  
> **Date :** 2026-01-09  
> **Niveau :** Débutant Python

---

## 📋 Table des matières

1. [Configuration `.env`](#1-configuration-env)
2. [Module `backend/ai.py`](#2-module-backendaipy)
3. [Modifications `backend/memory.py`](#3-modifications-backendmemorypy)
4. [Modifications `backend/main.py`](#4-modifications-backendmainpy)
5. [Tests et vérifications](#5-tests-et-vérifications)

---

## 1. Configuration `.env`

### 📄 Fichier `.env`

```bash
# Configuration API LLM
GITHUB_TOKEN=ghp_...
MODEL_NAME=gpt-4o
```

### 📖 Explications

**Ligne 1-2 : Commentaire**

- Les `#` en début de ligne = commentaires (ignorés par Python)

**Ligne 3 : `GITHUB_TOKEN=ghp_...`**

- Format : `NOM_VARIABLE=valeur`
- **Pas d'espaces** autour du `=`
- **Pas de guillemets** autour de la valeur
- Le token commence par `ghp_` ou `github_pat_`

**Ligne 4 : `MODEL_NAME=gpt-4o`**

- Nom du modèle LLM à utiliser
- Options : `gpt-4o`, `claude-3-5-sonnet`, `llama-3.1`, etc.

### 🔒 Sécurité

**Pourquoi `.env` dans `.gitignore` ?**

- Le token = mot de passe pour accéder à l'API
- Si on commit `.env` → tout le monde peut utiliser ton token
- Si quelqu'un vole ton token → peut consommer ta limite gratuite

**Comment lire `.env` depuis Python ?**

```python
from dotenv import load_dotenv  # Importer la bibliothèque
load_dotenv()  # Charger le fichier .env

token = os.getenv("GITHUB_TOKEN")  # Lire la variable
```

---

## 2. Module `backend/ai.py`

### 📄 Code complet commenté

```python
# Imports : bibliothèques nécessaires
import os          # Pour lire variables d'environnement (os.getenv)
import requests    # Pour faire des requêtes HTTP (comme fetch en JS)
import time        # Pour time.sleep() (attendre entre réessais)
from dotenv import load_dotenv  # Pour charger le fichier .env

# Charger les variables du fichier .env dans l'environnement
load_dotenv()


def demander_llm(prompt: str) -> str:
    """
    Appelle l'API GitHub Models (GPT-4o) pour obtenir une réponse.
    Réessaie 3 fois en cas d'erreur.

    Args:
        prompt: La question de l'utilisateur

    Returns:
        La réponse du LLM ou un message d'erreur poli
    """

    # 1. Récupérer le token depuis .env
    token = os.getenv("GITHUB_TOKEN")

    # 2. Vérifier que le token existe (sécurité)
    if not token:
        return "Erreur : token GitHub manquant dans .env"

    # 3. Préparer l'URL de l'API
    url = "https://models.inference.ai.azure.com/chat/completions"

    # 4. Préparer les headers (informations HTTP)
    headers = {
        "Content-Type": "application/json",  # On envoie du JSON
        "Authorization": f"Bearer {token}"   # Authentification avec token
    }

    # 5. Préparer les données à envoyer (body de la requête)
    donnees = {
        "model": os.getenv("MODEL_NAME", "gpt-4o"),  # Quel modèle utiliser
        "messages": [
            {"role": "user", "content": prompt}  # Format requis par l'API
        ]
    }

    # 6. Boucle pour réessayer 3 fois
    for tentative in range(1, 4):  # 1, 2, 3
        try:
            # 7. Envoyer la requête POST
            reponse = requests.post(url, headers=headers, json=donnees)

            # 8. Vérifier que la requête a réussi
            if reponse.status_code == 200:
                # 9. Extraire le texte de la réponse
                resultat = reponse.json()
                texte_llm = resultat["choices"][0]["message"]["content"]
                return texte_llm
            else:
                # Afficher l'erreur dans la console
                print(f"Tentative {tentative} échouée : status {reponse.status_code}")

        except Exception as e:
            # Capturer toute erreur (timeout, connexion, etc.)
            print(f"Tentative {tentative} erreur : {e}")

        # 10. Attendre 2 secondes avant de réessayer
        if tentative < 3:
            time.sleep(2)

    # 11. Si les 3 tentatives échouent, message d'erreur poli
    return "Désolé, le service est temporairement indisponible. Veuillez réessayer plus tard."
```

### 📖 Explications détaillées

#### **Bloc 1 : Imports**

```python
import os
import requests
import time
from dotenv import load_dotenv
```

- `os` : module standard Python pour système (fichiers, variables env)
- `requests` : bibliothèque tierce pour HTTP (installée avec `pip install requests`)
- `time` : module standard pour `sleep()` (pause)
- `dotenv` : bibliothèque pour lire `.env` (installée avec `pip install python-dotenv`)

#### **Bloc 2 : Charger `.env`**

```python
load_dotenv()
```

- Lit le fichier `.env` à la racine du projet
- Charge les variables dans l'environnement (accessibles via `os.getenv()`)
- Si `.env` n'existe pas : aucune erreur, mais `os.getenv()` retournera `None`

#### **Bloc 3 : Récupérer le token**

```python
token = os.getenv("GITHUB_TOKEN")
if not token:
    return "Erreur : token GitHub manquant dans .env"
```

- `os.getenv("NOM")` : lire variable d'environnement
- Si `token = None` (pas trouvé) → `if not token:` est `True`
- `return` arrête la fonction immédiatement avec message d'erreur

#### **Bloc 4 : URL et headers**

```python
url = "https://models.inference.ai.azure.com/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}
```

- `url` : adresse de l'API GitHub Models (Azure backend)
- `headers` : dictionnaire avec 2 clés
  - `Content-Type` : dit au serveur "on envoie du JSON"
  - `Authorization` : prouve qu'on a le droit d'utiliser l'API
  - `f"Bearer {token}"` : f-string qui insère la valeur de `token`

#### **Bloc 5 : Données à envoyer**

```python
donnees = {
    "model": os.getenv("MODEL_NAME", "gpt-4o"),
    "messages": [
        {"role": "user", "content": prompt}
    ]
}
```

- `donnees` : dictionnaire Python (sera converti en JSON)
- `os.getenv("MODEL_NAME", "gpt-4o")` : valeur par défaut si variable absente
- `messages` : liste de dictionnaires (format requis par API OpenAI)
  - `"role": "user"` : ce message vient de l'utilisateur
  - `"content": prompt` : le texte de la question

#### **Bloc 6 : Boucle de réessais**

```python
for tentative in range(1, 4):  # 1, 2, 3
    try:
        # Code qui peut échouer
    except Exception as e:
        # Code exécuté si erreur
```

- `range(1, 4)` : génère [1, 2, 3] (4 est exclu)
- `try:` : "essaie d'exécuter ce code"
- `except Exception as e:` : "si erreur, exécute ce bloc"
- `e` : variable qui contient l'objet erreur

#### **Bloc 7 : Requête POST**

```python
reponse = requests.post(url, headers=headers, json=donnees)
```

- `requests.post()` : envoie requête HTTP POST
- `url` : vers où envoyer
- `headers=headers` : ajouter headers HTTP
- `json=donnees` : convertit automatiquement dictionnaire en JSON et l'envoie

#### **Bloc 8 : Vérifier succès**

```python
if reponse.status_code == 200:
    resultat = reponse.json()
    texte_llm = resultat["choices"][0]["message"]["content"]
    return texte_llm
```

- `status_code == 200` : code HTTP pour "succès"
- `reponse.json()` : convertit réponse JSON en dictionnaire Python
- Navigation dictionnaire :
  - `resultat["choices"]` → liste
  - `[0]` → premier élément
  - `["message"]` → dictionnaire
  - `["content"]` → texte final
- `return` sort de la fonction ET de la boucle

#### **Bloc 9 : Attendre avant réessai**

```python
if tentative < 3:
    time.sleep(2)
```

- Si on n'est pas à la dernière tentative (3)
- Attendre 2 secondes avant de recommencer
- `time.sleep(2)` : pause de 2 secondes

#### **Bloc 10 : Message final**

```python
return "Désolé, le service est temporairement indisponible..."
```

- Si on arrive ici : les 3 tentatives ont échoué
- Retourne message poli au lieu de crasher

---

## 3. Modifications `backend/memory.py`

### 🔄 Changements apportés

#### **1. Ajout colonne `role` dans la table**

**Avant :**

```sql
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texte TEXT,
    nom_utilisateur TEXT,
    date_creation TEXT
)
```

**Après :**

```sql
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texte TEXT,
    nom_utilisateur TEXT,
    role TEXT,                    -- NOUVELLE COLONNE
    date_creation TEXT
)
```

**Pourquoi ?**

- Besoin de distinguer messages utilisateur vs réponses LLM
- `role="user"` → question de l'utilisateur
- `role="assistant"` → réponse du LLM

#### **2. Modification `sauvegarder_message()`**

**Avant :**

```python
def sauvegarder_message(texte, nom_utilisateur):
    # ...
    connexion.execute("""
        INSERT INTO messages (texte, nom_utilisateur, date_creation)
        VALUES (?, ?, ?)
    """, (texte, nom_utilisateur, date_maintenant))
```

**Après :**

```python
def sauvegarder_message(texte, nom_utilisateur, role="user"):  # Nouveau paramètre
    # ...
    connexion.execute("""
        INSERT INTO messages (texte, nom_utilisateur, role, date_creation)
        VALUES (?, ?, ?, ?)                                      -- 4 placeholders
    """, (texte, nom_utilisateur, role, date_maintenant))       # 4 valeurs
```

**Explications :**

- `role="user"` : valeur par défaut si non fourni
- Ajout de `role` dans la liste des colonnes
- Ajout d'un `?` supplémentaire (placeholder SQL)
- Ajout de `role` dans le tuple de valeurs

#### **3. Modification `recuperer_messages()`**

**Avant :**

```python
for ligne in lignes:
    message = {
        "id": ligne[0],
        "texte": ligne[1],
        "nom_utilisateur": ligne[2],
        "date_creation": ligne[3]      # Index 3
    }
```

**Après :**

```python
for ligne in lignes:
    message = {
        "id": ligne[0],
        "texte": ligne[1],
        "nom_utilisateur": ligne[2],
        "role": ligne[3],              # NOUVEAU : index 3
        "date_creation": ligne[4]      # Index décalé à 4
    }
```

**Pourquoi les indices changent ?**

- SQLite retourne tuples : `(id, texte, nom_utilisateur, role, date_creation)`
- `ligne[0]` = 1er élément (id)
- `ligne[3]` = 4ème élément (role)
- `ligne[4]` = 5ème élément (date_creation)

---

## 4. Modifications `backend/main.py`

### 🆕 Nouveautés ajoutées

#### **1. Import de `demander_llm`**

```python
from backend.ai import demander_llm
```

- Importe la fonction depuis le module `ai.py`
- Maintenant accessible dans `main.py` avec `demander_llm()`

#### **2. Nouveau modèle Pydantic `ChatMessage`**

```python
class ChatMessage(BaseModel):
    message: str
```

**Pourquoi créer un nouveau modèle ?**

- Endpoint `/chat` a besoin d'un format différent de `/message`
- `/message` : `{"texte": "...", "nom_utilisateur": "..."}`
- `/chat` : `{"message": "..."}`
- Séparation des responsabilités (principe SOLID)

#### **3. Endpoint POST `/chat`**

```python
@app.post("/chat")
def chat(msg: ChatMessage):
    # 1. Sauvegarder message utilisateur
    sauvegarder_message(msg.message, "Utilisateur", role="user")

    # 2. Appeler le LLM
    reponse_llm = demander_llm(msg.message)

    # 3. Sauvegarder réponse LLM
    sauvegarder_message(reponse_llm, "Assistant", role="assistant")

    # 4. Retourner réponse
    return {"reponse": reponse_llm}
```

### 📖 Explications ligne par ligne

**Ligne 1 : Décorateur**

```python
@app.post("/chat")
```

- Déclare un endpoint qui répond aux requêtes POST
- URL : `http://127.0.0.1:8000/chat`

**Ligne 2 : Définition fonction**

```python
def chat(msg: ChatMessage):
```

- Nom fonction : `chat`
- Paramètre `msg` : type `ChatMessage` (validé par Pydantic)
- Pydantic vérifie automatiquement que JSON contient `message`

**Ligne 3-4 : Sauvegarder question utilisateur**

```python
sauvegarder_message(msg.message, "Utilisateur", role="user")
```

- `msg.message` : accède au champ `message` du JSON reçu
- `"Utilisateur"` : nom générique pour tous les utilisateurs
- `role="user"` : marque comme message utilisateur

**Ligne 5-6 : Appeler le LLM**

```python
reponse_llm = demander_llm(msg.message)
```

- Appelle la fonction de `backend/ai.py`
- Passe la question de l'utilisateur
- Stocke la réponse dans `reponse_llm`

**Ligne 7-8 : Sauvegarder réponse LLM**

```python
sauvegarder_message(reponse_llm, "Assistant", role="assistant")
```

- `reponse_llm` : texte généré par GPT-4o
- `"Assistant"` : nom pour le LLM
- `role="assistant"` : marque comme réponse LLM

**Ligne 9-10 : Retourner JSON**

```python
return {"reponse": reponse_llm}
```

- FastAPI convertit automatiquement dictionnaire en JSON
- Frontend recevra : `{"reponse": "Pour lister les fichiers..."}`

---

## 5. Tests et vérifications

### 🧪 Test 1 : Module `ai.py` seul

**Commande :**

```powershell
python backend/ai.py
```

**Attendu :**

```
Bonjour ! Comment puis-je vous aider aujourd'hui ?
```

**Que se passe-t-il ?**

1. `load_dotenv()` charge `.env`
2. `demander_llm("Dis bonjour en une phrase")` est appelé
3. Requête HTTP envoyée à GitHub Models
4. GPT-4o génère une réponse
5. Réponse affichée dans console

### 🧪 Test 2 : Endpoint `/chat` via Swagger

**URL :** http://127.0.0.1:8000/docs

**JSON envoyé :**

```json
{
  "message": "Comment lister les fichiers dans PowerShell ?"
}
```

**JSON reçu :**

```json
{
  "reponse": "Pour lister les fichiers dans PowerShell, vous pouvez utiliser la commande **`Get-ChildItem`**..."
}
```

**Flux d'exécution :**

1. Swagger envoie POST à `/chat`
2. FastAPI valide JSON avec Pydantic
3. `chat()` appelle `sauvegarder_message()` (role="user")
4. `chat()` appelle `demander_llm()`
5. API GitHub Models traite la requête (~2-3 secondes)
6. GPT-4o génère réponse complète
7. `chat()` appelle `sauvegarder_message()` (role="assistant")
8. FastAPI retourne JSON au frontend

### 🧪 Test 3 : Vérifier persistance

**Endpoint :** GET `/messages`

**Résultat attendu :**

```json
{
  "messages": [
    {
      "id": 1,
      "texte": "Comment lister les fichiers dans PowerShell ?",
      "nom_utilisateur": "Utilisateur",
      "role": "user",
      "date_creation": "2026-01-09T10:41:09.043304"
    },
    {
      "id": 2,
      "texte": "Pour lister les fichiers dans PowerShell...",
      "nom_utilisateur": "Assistant",
      "role": "assistant",
      "date_creation": "2026-01-09T10:41:13.371480"
    }
  ],
  "total": 2
}
```

**Vérifications :**

- ✅ 2 messages sauvegardés
- ✅ `role` présent et correct (user/assistant)
- ✅ Dates différentes (quelques secondes d'écart)
- ✅ Ordre préservé (user puis assistant)

---

## 🎓 Concepts clés à retenir

### 1. **API REST = communication client-serveur**

- Client (frontend) envoie JSON
- Serveur (backend) traite et répond JSON
- Notre backend appelle aussi une autre API (GitHub Models)

### 2. **Gestion d'erreurs robuste**

- Toujours vérifier que les ressources existent (token, fichiers)
- `try/except` pour code qui peut échouer
- Réessayer en cas d'erreur temporaire (réseau)
- Messages d'erreur polis pour l'utilisateur

### 3. **Séparation des responsabilités**

- `ai.py` : communication avec LLM
- `memory.py` : persistance SQLite
- `main.py` : orchestration des endpoints
- Chaque module a un rôle précis

### 4. **Sécurité des secrets**

- Jamais de clés API en dur dans le code
- `.env` pour stocker secrets localement
- `.gitignore` pour ne pas committer `.env`
- `python-dotenv` pour charger variables

### 5. **Rôles conversationnels**

- Distinction user/assistant essentielle
- Permet de reconstruire historique
- Prépare contexte multi-tours (sessions futures)

---

## 📚 Ressources complémentaires

### Documentation officielle

- **GitHub Models :** https://github.com/marketplace/models
- **Requests :** https://docs.python-requests.org
- **Python-dotenv :** https://pypi.org/project/python-dotenv/
- **FastAPI :** https://fastapi.tiangolo.com

### Commandes utiles

```powershell
# Lister packages installés
pip list

# Voir détails d'un package
pip show requests

# Mettre à jour requirements.txt
pip freeze > requirements.txt

# Installer depuis requirements.txt
pip install -r requirements.txt
```

---

**📌 Fin du guide technique**  
**Prochaine étape :** Frontend interactif (Session 4)
