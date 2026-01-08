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
- **API IA :** (à venir)

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

### Guides spécifiques

- [Guide technique Session 0](docs/sessions/session_0_setup/GUIDE_TECHNIQUE.md)
- [Guide technique Session 1](docs/sessions/session_1_pydantic/GUIDE_TECHNIQUE.md)
- [Guide technique Session 2](docs/sessions/session_2_sqlite/GUIDE_TECHNIQUE.md)

---

## 📝 Changelog

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
- Documentation complète Session 1 (sauvegarde dans SQLite)
- ✅ Endpoint GET `/messages` fonctionnel (récupère depuis SQLite)
- ✅ Base de données SQLite avec persistance
- ✅ Documentation structurée (Sessions 0, 1 et 2)
- 🔜 Prochaine étape : Intégration LLM API

**Ajouté**

- Structure du projet
- Premier serveur FastAPI
- Endpoint GET `/ping`
- Documentation automatique `/docs`
- Structure complète `docs/`

---

## ✅ Status final

- ✅ Serveur FastAPI opérationnel
- ✅ Endpoint `/ping` fonctionnel
- ✅ Modèle Pydantic `Message` avec validation
- ✅ Endpoint POST `/message` fonctionnel
- ✅ Documentation structurée (Session 0 & 1)
- 🔜 Prochaine étape : Persistance SQLite
