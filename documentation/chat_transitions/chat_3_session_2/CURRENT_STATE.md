# État actuel — Fin de Session 2

> **Date :** 2026-01-08  
> **Chat :** 3  
> **Session :** 2 — Persistance avec SQLite

---

## 🎯 Ce qui a été accompli

### ✅ Concepts appris

- **SQLite** : Base de données relationnelle dans un fichier
- **Persistance** : Les données restent après redémarrage
- **SQL** : CREATE TABLE, INSERT INTO, SELECT \* FROM
- **Placeholders `?`** : Sécurité contre injections SQL
- **Lifespan FastAPI** : Remplace `@app.on_event("startup")` (méthode moderne)
- **`@asynccontextmanager`** : Gérer cycle de vie (démarrage/arrêt)
- **`cursor.fetchall()`** : Récupérer toutes les lignes SQL
- **Transformation tuples → dictionnaires** : Pour JSON lisible
- **`datetime.now().isoformat()`** : Format ISO pour dates

### ✅ Code écrit

#### **Module `backend/memory.py`** (nouveau fichier)

3 fonctions principales :

```python
def initialiser_db():
    # Créer la table "messages" avec 4 colonnes
    # id, texte, nom_utilisateur, date_creation

def sauvegarder_message(texte, nom_utilisateur):
    # Insérer un message dans la table
    # Utilise datetime.now().isoformat() pour la date

def recuperer_messages():
    # SELECT * FROM messages
    # Transformer chaque tuple en dictionnaire
    # Retourner liste de dictionnaires
```

#### **Modifications `backend/main.py`**

**Ajout du lifespan** :

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    initialiser_db()  # Au démarrage
    yield             # Serveur tourne
    # Code arrêt ici (si besoin)

app = FastAPI(lifespan=lifespan)
```

**Endpoint POST `/message` modifié** :

```python
@app.post("/message")
def recevoir_message(msg: Message):
    sauvegarder_message(msg.texte, msg.nom_utilisateur or "Anonyme")
    return {"recu": True}
```

**Nouveau endpoint GET `/messages`** :

```python
@app.get("/messages")
def lire_messages():
    messages = recuperer_messages()
    return {"messages": messages, "total": len(messages)}
```

### ✅ Documentation créée

- `docs/sessions/session_2_sqlite/README.md` : Vue d'ensemble ✅
- `docs/sessions/session_2_sqlite/GUIDE_TECHNIQUE.md` : Explications détaillées ligne par ligne ✅
- `docs/sessions/session_2_sqlite/scripts/main.py` : Code final FastAPI ✅
- `docs/sessions/session_2_sqlite/scripts/memory.py` : Code final module SQLite ✅
- `docs/chat_transitions/chat_3_session_2/CURRENT_STATE.md` : Ce fichier ✅
- Mise à jour de `docs/INDEX.md`, `docs/README.md`, `README.md` racine ✅

### ✅ Tests réussis

#### Test 1 : POST `/message` (sauvegarder) ✅

**Swagger** : http://127.0.0.1:8000/docs

```json
Envoi : {"texte": "Mon premier message persistant", "nom_utilisateur": "Alice"}
Résultat : {"recu": true}
```

#### Test 2 : GET `/messages` (récupérer) ✅

```json
Résultat : {
  "messages": [
    {
      "id": 1,
      "texte": "Mon premier message persistant",
      "nom_utilisateur": "Alice",
      "date_creation": "2026-01-08T14:30:00.123456"
    }
  ],
  "total": 1
}
```

#### Test 3 : Persistance après redémarrage ✅

- Redémarrer le serveur
- GET `/messages` retourne toujours les anciens messages
- ✅ **Les données sont bien persistantes !**

---

## 📂 Structure actuelle du projet

```
os-assistant/
├── backend/
│   ├── main.py                     ✅ FastAPI + Pydantic + SQLite + Lifespan
│   └── memory.py                   ✅ NOUVEAU : Module SQLite (3 fonctions)
├── frontend/
│   └── index.html                  (non modifié)
├── docs/                           ✅ Mis à jour
│   ├── INDEX.md                    ✅ Session 2 ajoutée
│   ├── README.md                   ✅ Session 2 ajoutée
│   ├── sessions/
│   │   ├── session_0_setup/        ✅ Session 0
│   │   ├── session_1_pydantic/     ✅ Session 1
│   │   └── session_2_sqlite/       ✅ NOUVEAU : Session 2
│   │       ├── README.md
│   │       ├── GUIDE_TECHNIQUE.md
│   │       └── scripts/
│   │           ├── main.py
│   │           └── memory.py
│   └── chat_transitions/
│       ├── chat_1_session_0/       ✅ Session 0
│       ├── chat_2_session_1/       ✅ Session 1
│       └── chat_3_session_2/       ✅ NOUVEAU : Session 2
│           └── CURRENT_STATE.md    (ce fichier)
├── memory.db                       ✅ NOUVEAU : Base de données SQLite
├── venv/                           ✅ Activé
├── README.md                       ✅ Mis à jour (4 sections)
└── requirements.txt                ✅ (fastapi, uvicorn, pydantic)
```

---

## 🎓 Apprentissages clés de cette session

### 1. **SQLite = Excel qui ne s'efface jamais**

- Fichier `memory.db` sur le disque
- Tables = onglets Excel
- Lignes = entrées
- Colonnes = champs (id, texte, nom_utilisateur, date_creation)

### 2. **SQL = Langage pour parler à la base**

- `CREATE TABLE` : Créer une table
- `INSERT INTO` : Ajouter des données
- `SELECT * FROM` : Récupérer des données
- `?` : Sécurité (évite injections SQL)

### 3. **Lifespan FastAPI (moderne)**

- Remplace `@app.on_event("startup")` déprécié
- `@asynccontextmanager` + `yield` pour gérer démarrage/arrêt
- Code avant `yield` = au démarrage
- Code après `yield` = à l'arrêt

### 4. **Transformation SQL → JSON**

- `fetchall()` retourne liste de tuples
- Boucle `for` pour transformer chaque tuple en dictionnaire
- Dictionnaires = format JSON lisible

---

## 🔧 Commandes pour tester

### Démarrer le serveur

```powershell
uvicorn backend.main:app --reload
```

### Tester avec Swagger

http://127.0.0.1:8000/docs

### Tester avec PowerShell

```powershell
# Ping
curl.exe http://127.0.0.1:8000/ping

# Envoyer message (PowerShell natif)
$body = @{texte="Test PowerShell"; nom_utilisateur="Alice"} | ConvertTo-Json
Invoke-WebRequest -Method POST -Uri http://127.0.0.1:8000/message -ContentType "application/json" -Body $body -UseBasicParsing

# Récupérer messages
curl.exe http://127.0.0.1:8000/messages
```

---

## 🚀 Prochaine session suggérée

**Session 3 — Intégration LLM (API externe)**

### Objectifs

- Créer un module `backend/ai.py`
- Fonction `ask_llm(prompt: str) -> str`
- Appeler une API LLM (OpenAI, Anthropic, Ollama local)
- Nouveau endpoint POST `/chat` qui :
  1. Reçoit un message utilisateur
  2. Appelle le LLM avec le contexte
  3. Sauvegarde question + réponse dans SQLite
  4. Retourne la réponse du LLM

### Concepts à apprendre

- Requêtes HTTP avec `requests` ou `httpx`
- Variables d'environnement (`.env`)
- Gestion d'erreurs (try/except)
- Streaming de réponses (si temps)

---

## 📝 Notes personnelles (observations Copilot)

### Points forts identifiés

- ✅ **Excellent progrès** : écrit 90% du code lui-même
- ✅ **Bonne compréhension** des boucles `for` pour transformer les tuples
- ✅ **Réflexe documentation** : veut commenter avant de continuer
- ✅ **Teste systématiquement** : vérifie que ça marche avant d'avancer

### Difficultés rencontrées

- ⚠️ Confusion tuple vs liste (normale pour un débutant)
- ⚠️ Oublié `.close()` et `()` pour `commit()` (corrigé rapidement)
- ⚠️ PowerShell et guillemets JSON (résolu avec Swagger)

### Évolution depuis Session 1

- **Plus autonome** : écrit le code avant de demander validation
- **Pose les bonnes questions** : "je veux commenter le code d'abord"
- **Comprend les erreurs** : identifie Pylance warning et demande explication

### Recommandations pour Session 3

- Continuer le pattern : concept → pseudo-code → coder → corriger
- Introduire `try/except` (gestion d'erreurs)
- Montrer `.env` et `os.getenv()` pour secrets
- Garder les snippets ≤60 lignes

---

_Dernière mise à jour : 2026-01-08_
