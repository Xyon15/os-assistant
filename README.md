# OS Assistant

> Assistant personnel IA offline-first orienté productivité

---

## 🎯 Vision

Construire un assistant personnel avec :

- Backend Python (FastAPI)
- Mémoire locale (SQLite)
- Client web minimal
- Intégration LLM API

---

## 🛠️ Tech Stack

- **Backend :** Python 3.10+ / FastAPI / Uvicorn
- **Base de données :** SQLite
- **Frontend :** HTML / CSS / JavaScript
- **API IA :** Github models (Temporaire)

---

## 🚀 Démarrage rapide

### Prérequis

- Python 3.10+
- Git

### Installation

```powershell
# Cloner le projet
git clone <repo-url>
cd os-assistant

# Créer et activer l'environnement virtuel
python -m venv venv
venv\Scripts\Activate.ps1

# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur
uvicorn backend.main:app --reload
```

### Tester

- API : http://127.0.0.1:8000/ping
- Documentation : http://127.0.0.1:8000/docs

---

## 📚 Documentation

Toute la documentation est dans [`docs/`](docs/README.md)

### Sessions documentées

- [Session 0 — Setup & Premier serveur FastAPI](docs/sessions/session_0_setup/README.md) ✅
- [Session 1 — Validation avec Pydantic](docs/sessions/session_1_pydantic/README.md) ✅
- [Session 2 — Persistance avec SQLite](docs/sessions/session_2_sqlite/README.md) ✅
- [Session 3 — Intégration LLM API](docs/sessions/session_3_llm/README.md) ✅
- [Session 4 — Frontend Interactif](docs/sessions/session_4_frontend/README.md) ✅
- [Session 5 — CSS & Design Moderne](docs/sessions/session_5_css/README.md) ✅

### Guides spécifiques

- [Guide Git Workflow](docs/GIT_WORKFLOW.md) 🌿
- [Guide technique Session 0](docs/sessions/session_0_setup/GUIDE_TECHNIQUE.md)
- [Guide technique Session 1](docs/sessions/session_1_pydantic/GUIDE_TECHNIQUE.md)
- [Guide technique Session 2](docs/sessions/session_2_sqlite/GUIDE_TECHNIQUE.md)
- [Guide technique Session 3](docs/sessions/session_3_llm/GUIDE_TECHNIQUE.md)
- [Guide technique Session 4](docs/sessions/session_4_frontend/GUIDE_TECHNIQUE.md)
- [Guide technique Session 5](docs/sessions/session_5_css/GUIDE_TECHNIQUE.md)

---

## 📝 Changelog

### [Session 5] - 2026-01-13

**Ajouté**

- Fichier CSS `frontend/style.css` (~120 lignes) avec design moderne
- Layout Flexbox vertical (body) et horizontal (#inputZone)
- Bulles de messages stylisées (user bleue droite, assistant grise gauche)
- Animations CSS (fadeIn apparition + hover scale)
- Commentaires détaillés sur tous les fichiers frontend
- `id="inputZone"` dans HTML pour sélecteur CSS
- Documentation complète Session 5

**Modifié**

- `frontend/app.js` : Remplacement `innerHTML +=` par `createElement()` + `appendChild()`
- `frontend/app.js` : Ajout `setTimeout(400ms)` pour délai naturel avant "est en train d'écrire..."
- `frontend/index.html` : Suppression `<p>Interface prête</p>`, ajout commentaires HTML
- Performance améliorée : animations uniquement sur nouveaux messages

**Concepts appris**

- Flexbox CSS (`display: flex`, `flex-direction`, `justify-content`, `align-items`)
- Animations CSS (`@keyframes`, `animation`, `transition`)
- Pseudo-classes (`:hover`)
- `createElement()` et `appendChild()` (DOM moderne)
- `setTimeout()` pour délais naturels
- Bulles de chat (border-radius, box-shadow, max-width)

### [Session 4] - 2026-01-09

**Ajouté**

- Frontend HTML/JavaScript (`frontend/index.html`, `frontend/app.js`)
- Middleware CORS dans `backend/main.py`
- Interface chat interactive (input + bouton)
- Envoi messages avec bouton ou touche Entrée
- Message de chargement pendant réflexion LLM
- Documentation complète Session 4

**Concepts appris**

- `fetch()` JavaScript pour requêtes HTTP
- `addEventListener()` pour événements (clic, touche)
- `innerHTML` pour modifier le DOM
- Promesses JavaScript et `.then()`
- CORS (Cross-Origin Resource Sharing)
- Middleware FastAPI
- Séparation HTML / JavaScript

### [Session 3] - 2026-01-09

**Ajouté**

- Module `backend/ai.py` pour appeler GitHub Models (GPT-4o)
- Fichier `.env` pour stocker secrets (GITHUB_TOKEN)
- Endpoint POST `/chat` pour conversation avec LLM
- Support des rôles (user/assistant) dans `memory.py`
- Colonne `role` ajoutée à la table SQLite
- Bibliothèques : `python-dotenv`, `requests`
- Documentation complète Session 3

**Concepts appris**

- API LLM et appels HTTP avec `requests`
- Gestion secrets avec `.env` et `python-dotenv`
- `try/except` et pattern de réessai (3 tentatives)
- Rôles conversationnels (user/assistant)
- Headers HTTP (Authorization, Content-Type)
- Extraction JSON : `resultat["choices"][0]["message"]["content"]`

### [Session 2] - 2026-01-08

**Ajouté**

- Module `backend/memory.py` avec 3 fonctions (initialiser_db, sauvegarder_message, recuperer_messages)
- Base de données SQLite (`memory.db`) pour persistance
- Lifespan FastAPI avec `@asynccontextmanager` (remplace @app.on_event déprécié)
- Endpoint GET `/messages` pour récupérer tous les messages sauvegardés
- Modification endpoint POST `/message` pour sauvegarder dans SQLite
- Gestion dates avec `datetime.now().isoformat()`
- Documentation complète Session 2

**Concepts appris**

- SQLite, tables, colonnes, SQL (CREATE, INSERT, SELECT)
- Sécurité avec placeholders `?`
- Transformation tuples → dictionnaires
- Lifespan et cycle de vie FastAPI

### [Session 1] - 2026-01-08

**Ajouté**

- Modèle Pydantic `Message` avec validation automatique
- Endpoint POST `/message` avec validation des entrées
- Champs obligatoires et facultatifs
- Tests de validation (champs manquants, types incorrects)
- Documentation complète Session 1

**Concepts appris**

- Pydantic et BaseModel
- Validation automatique des données
- Champs Optional[str]

### [Session 0] - 2026-01-08

**Ajouté**

- Structure du projet
- Premier serveur FastAPI
- Endpoint GET `/ping`
- Documentation automatique `/docs`
- Structure complète `docs/`

**Concepts appris**

- API REST et modèle client/serveur
- FastAPI et décorateurs Python
- Dictionnaires Python et JSON

---

## ✅ Status final

- ✅ Serveur FastAPI opérationnel
- ✅ Endpoint `/ping` fonctionnel
- ✅ Modèle Pydantic `Message` avec validation
- ✅ Endpoint POST `/message` fonctionnel
- ✅ Endpoint GET `/messages` fonctionnel (récupère depuis SQLite)
- ✅ Base de données SQLite avec persistance
- ✅ Module `ai.py` pour appeler GitHub Models (GPT-4o)
- ✅ Endpoint POST `/chat` pour conversation avec LLM
- ✅ Frontend HTML/JavaScript interactif
- ✅ Communication frontend ↔ backend ↔ LLM opérationnelle
- ✅ Design CSS moderne avec Flexbox et animations
- ✅ Bulles de chat stylisées (user/assistant)
- ✅ Code entièrement commenté (frontend)
- ✅ Documentation structurée (Sessions 0 à 5)
- 🎉 **Application complète et professionnelle !**
- 🔜 Prochaines étapes optionnelles : Auto-scroll, Dark mode, Tests, Déploiement
