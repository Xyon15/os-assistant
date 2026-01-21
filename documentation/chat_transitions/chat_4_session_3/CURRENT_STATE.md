# État actuel — Fin de Session 3

> **Date :** 2026-01-09  
> **Chat :** 4  
> **Session :** 3 — Intégration LLM API

---

## 🎯 Ce qui a été accompli

### ✅ Concepts appris

- **API LLM** : Service distant qui génère du texte intelligent
- **Analogie "appeler un ami expert"** : LLM = expert au téléphone vs SQLite = bibliothèque
- **GitHub Models** : API LLM gratuite pour étudiants (GPT-4o, Claude, Llama)
- **Fichier `.env`** : Stocker secrets (clés API) sans les committer
- **`python-dotenv`** : Bibliothèque pour charger variables depuis `.env`
- **`requests.post()`** : Envoyer requêtes HTTP (comme `fetch()` en JavaScript)
- **`try/except`** : Gérer les erreurs qui peuvent survenir (réseau, timeout)
- **Pattern de réessai** : Boucle + `time.sleep(2)` entre tentatives
- **Rôles conversationnels** : `role="user"` vs `role="assistant"`
- **Headers HTTP** : `Authorization: Bearer token`, `Content-Type: application/json`

### ✅ Code écrit

#### **Nouveau fichier : `.env`**

```bash
GITHUB_TOKEN=ghp_...
MODEL_NAME=gpt-4o
```

- Configuration secrets (JAMAIS committer)
- Déjà dans `.gitignore` ✅

#### **Nouveau module : `backend/ai.py`**

Fonction principale : `demander_llm(prompt: str) -> str`

**Fonctionnalités :**

```python
def demander_llm(prompt: str) -> str:
    # 1. Charger token depuis .env
    token = os.getenv("GITHUB_TOKEN")

    # 2. Vérifier token existe
    if not token:
        return "Erreur : token manquant"

    # 3. Préparer requête HTTP (URL, headers, JSON)
    url = "https://models.inference.ai.azure.com/chat/completions"
    headers = {"Authorization": f"Bearer {token}", ...}
    donnees = {"model": "gpt-4o", "messages": [...]}

    # 4. Boucle réessai (3 tentatives)
    for tentative in range(1, 4):
        try:
            reponse = requests.post(url, headers=headers, json=donnees)
            if reponse.status_code == 200:
                return resultat["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Erreur : {e}")
        time.sleep(2)  # Attendre avant réessai

    # 5. Message poli si échec total
    return "Désolé, service indisponible..."
```

#### **Modifications : `backend/memory.py`**

**1. Table SQLite modifiée (colonne `role` ajoutée)**

```sql
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texte TEXT,
    nom_utilisateur TEXT,
    role TEXT,              -- NOUVEAU
    date_creation TEXT
)
```

**2. Fonction `sauvegarder_message()` modifiée**

```python
def sauvegarder_message(texte, nom_utilisateur, role="user"):
    # ...
    connexion.execute("""
        INSERT INTO messages (texte, nom_utilisateur, role, date_creation)
        VALUES (?, ?, ?, ?)
    """, (texte, nom_utilisateur, role, date_maintenant))
```

**3. Fonction `recuperer_messages()` modifiée**

```python
for ligne in lignes:
    message = {
        "id": ligne[0],
        "texte": ligne[1],
        "nom_utilisateur": ligne[2],
        "role": ligne[3],              # NOUVEAU
        "date_creation": ligne[4]
    }
```

#### **Modifications : `backend/main.py`**

**1. Import ajouté**

```python
from backend.ai import demander_llm
```

**2. Nouveau modèle Pydantic**

```python
class ChatMessage(BaseModel):
    message: str
```

**3. Nouveau endpoint POST `/chat`**

```python
@app.post("/chat")
def chat(msg: ChatMessage):
    # 1. Sauvegarder message user
    sauvegarder_message(msg.message, "Utilisateur", role="user")

    # 2. Appeler LLM
    reponse_llm = demander_llm(msg.message)

    # 3. Sauvegarder réponse LLM
    sauvegarder_message(reponse_llm, "Assistant", role="assistant")

    # 4. Retourner JSON
    return {"reponse": reponse_llm}
```

### ✅ Documentation créée

- `docs/sessions/session_3_llm/README.md` : Vue d'ensemble ✅
- `docs/sessions/session_3_llm/GUIDE_TECHNIQUE.md` : Explications ligne par ligne ✅
- `docs/sessions/session_3_llm/scripts/` : Copies finales (main.py, memory.py, ai.py) ✅
- `docs/chat_transitions/chat_4_session_3/CURRENT_STATE.md` : Ce fichier ✅

### ✅ Tests réussis

#### Test 1 : Module `ai.py` seul ✅

**Commande :**

```powershell
python backend/ai.py
```

**Résultat :**

```
Bonjour ! Comment puis-je vous aider aujourd'hui ?
```

#### Test 2 : Endpoint POST `/chat` ✅

**Swagger** : http://127.0.0.1:8000/docs

**Envoi :**

```json
{ "message": "Comment lister les fichiers dans PowerShell ?" }
```

**Réponse :**

```json
{
  "reponse": "Pour lister les fichiers dans PowerShell, vous pouvez utiliser la commande **`Get-ChildItem`** ou son alias **`ls`**..."
}
```

#### Test 3 : Persistance SQLite ✅

**Endpoint GET `/messages`** :

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

---

## 📁 Structure actuelle du projet

```
os-assistant/
├── backend/
│   ├── main.py           ✅ Modifié : endpoint /chat + import demander_llm
│   ├── memory.py         ✅ Modifié : support role (user/assistant)
│   ├── ai.py             ✅ NOUVEAU : appel API GitHub Models
│   └── __pycache__/
├── frontend/
│   └── index.html        (pas encore modifié)
├── docs/
│   ├── INDEX.md
│   ├── README.md
│   ├── sessions/
│   │   ├── session_0_setup/
│   │   ├── session_1_pydantic/
│   │   ├── session_2_sqlite/
│   │   └── session_3_llm/       ✅ NOUVEAU
│   │       ├── README.md
│   │       ├── GUIDE_TECHNIQUE.md
│   │       └── scripts/
│   │           ├── main.py
│   │           ├── memory.py
│   │           └── ai.py
│   └── chat_transitions/
│       ├── chat_1_session_0/
│       ├── chat_2_session_1/
│       ├── chat_3_session_2/
│       └── chat_4_session_3/    ✅ NOUVEAU
│           └── CURRENT_STATE.md (ce fichier)
├── .env                  ✅ NOUVEAU (secrets)
├── .gitignore            ✅ Contient .env
├── memory.db             ✅ Recréé avec colonne role
├── requirements.txt      (à mettre à jour)
└── README.md
```

---

## 🔧 Commandes exécutées

### Installation bibliothèques

```powershell
pip install python-dotenv requests
```

### Recréer DB avec colonne role

```powershell
rm memory.db
python -c "from backend.memory import initialiser_db; initialiser_db()"
```

### Tester module ai.py

```powershell
python backend/ai.py
```

### Lancer serveur

```powershell
uvicorn backend.main:app --reload
```

---

## 📊 Statistiques

- **Fichiers créés** : 2 (ai.py, .env)
- **Fichiers modifiés** : 2 (memory.py, main.py)
- **Lignes de code ajoutées** : ~120
- **Endpoints totaux** : 4 (ping, message, messages, **chat**)
- **Nouveaux concepts** : 10+ (API, try/except, .env, roles, etc.)
- **Tests réussis** : 3/3 ✅

---

## 🎓 Apprentissages clés de la session

### Réussites majeures

1. ✅ **Compréhension API LLM** : analogie "ami expert" très efficace
2. ✅ **Code écrit 100% par l'utilisateur** : guidage pseudo-code → code réel
3. ✅ **Gestion erreurs robuste** : pattern réessai + messages polis
4. ✅ **Sécurité secrets** : `.env` + `.gitignore` bien compris
5. ✅ **Tests méthodiques** : module seul → endpoint → persistance

### Évolution depuis Session 2

- **Plus autonome** : écrit fonctions complètes (50+ lignes) sans aide
- **Meilleure compréhension HTTP** : POST, headers, JSON, status codes
- **Réflexes sécurité** : pourquoi ne pas committer secrets
- **Débogage efficace** : teste étape par étape (isolation problèmes)

### Points d'attention

- ⚠️ Première tentative : ajout `message` dans classe `Message` au lieu de créer `ChatMessage`
- ✅ Correction immédiate : séparation modèles Pydantic

---

## 🚀 Prochaines étapes possibles

### Session 4 : Frontend interactif

**Objectifs :**

- Créer interface chat dans `frontend/index.html`
- JavaScript pour appeler `/chat` avec `fetch()`
- Afficher conversation en temps réel
- Design simple avec CSS

### Améliorations futures

1. **Contexte conversationnel** : envoyer historique au LLM (mémoire multi-tours)
2. **Streaming** : afficher réponse mot par mot (SSE ou WebSocket)
3. **Gestion d'erreurs avancée** : retry exponentiel, timeout configurable
4. **Support multi-modèles** : switcher entre GPT-4o, Claude, Llama
5. **Interface admin** : gérer conversations, effacer historique
6. **Déploiement** : Render, Heroku, ou GitHub Pages (frontend)

---

## 📝 TODO avant Session 4

- [ ] Mettre à jour `requirements.txt` (ajouter `python-dotenv` et `requests`)
- [ ] Commenter code si besoin
- [ ] Tester endpoint `/chat` avec plusieurs questions
- [ ] Vérifier que persistance fonctionne après redémarrage serveur

---

## 🔗 Liens utiles

- **GitHub Models** : https://github.com/marketplace/models
- **Documentation Requests** : https://docs.python-requests.org
- **Documentation Python-dotenv** : https://pypi.org/project/python-dotenv/
- **FastAPI Docs** : https://fastapi.tiangolo.com

---

**📌 Session 3 terminée avec succès !**  
**Prochain chat : Session 4 — Frontend interactif**
