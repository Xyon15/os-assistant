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

### Guides spécifiques

- [Guide technique Session 0](docs/sessions/session_0_setup/GUIDE_TECHNIQUE.md)
- [Guide technique Session 1](docs/sessions/session_1_pydantic/GUIDE_TECHNIQUE.md)

---

## 📝 Changelog

### [Session 1] - 2026-01-08

**Ajouté**

- Modèle Pydantic `Message` avec validation automatique
- Endpoint POST `/message` avec validation des entrées
- Champs obligatoires et facultatifs
- Tests de validation (champs manquants, types incorrects)
- Documentation complète Session 1

### [Session 0] - 2026-01-08

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
