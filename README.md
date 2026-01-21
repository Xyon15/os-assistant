# OS Assistant

> Assistant personnel IA offline-first orienté productivité

---

![Tests](https://github.com/Xyon15/os-assistant/actions/workflows/tests.yml/badge.svg)

[![Backend](https://img.shields.io/badge/backend-live-brightgreen?logo=fastapi)](https://os-assistant-backend.onrender.com)
[![Frontend](https://img.shields.io/badge/frontend-GitHub%20Pages-blue?logo=github)](https://xyon15.github.io/os-assistant/)

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
- [Session 6 — Améliorations UX](docs/sessions/session_6_ux/README.md) ✅
- [Session 7 — Dark Mode](docs/sessions/session_7_darkmode/README.md) ✅
- [Session 8 — Tests automatisés & CI/CD](docs/sessions/session_8_tests/README.md) ✅
- [Session 9 — Déploiement production](documentation/sessions/session_9_deployment/README.md) ✅

### Guides spécifiques

- [Guide Git Workflow](docs/GIT_WORKFLOW.md) 🌿
- [Guide technique Session 0](docs/sessions/session_0_setup/GUIDE_TECHNIQUE.md)
- [Guide technique Session 1](docs/sessions/session_1_pydantic/GUIDE_TECHNIQUE.md)
- [Guide technique Session 2](docs/sessions/session_2_sqlite/GUIDE_TECHNIQUE.md)
- [Guide technique Session 3](docs/sessions/session_3_llm/GUIDE_TECHNIQUE.md)
- [Guide technique Session 4](docs/sessions/session_4_frontend/GUIDE_TECHNIQUE.md)
- [Guide technique Session 5](docs/sessions/session_5_css/GUIDE_TECHNIQUE.md)
- [Guide technique Session 6](docs/sessions/session_6_ux/GUIDE_TECHNIQUE.md)
- [Guide technique Session 7](docs/sessions/session_7_darkmode/GUIDE_TECHNIQUE.md)
- [Guide technique Session 8](docs/sessions/session_8_tests/GUIDE_TECHNIQUE.md)

---

## 📝 Changelog

### [Session 8] - 2026-01-17

**Ajouté**

- Tests pytest backend (4 tests : ping, message, get_messages, validation)
- Tests Selenium frontend (3 tests : open_page, send_message, dark_mode_toggle)
- GitHub Actions workflow CI/CD (.github/workflows/tests.yml)
- Badge status tests dans README.md
- Initialisation DB automatique dans tests (`initialiser_db()`)
- Mode headless Chrome pour CI (détection variable CI)
- Job backend séparé (Python + pytest)
- Job frontend séparé (Chrome + Selenium + pytest)
- Documentation complète Session 8

**Modifié**

- `tests/test_backend.py` : 4 tests avec TestClient FastAPI (~70 lignes)
- `tests/test_frontend.py` : 3 tests avec Selenium WebDriver (~110 lignes)
- `.github/workflows/tests.yml` : Workflow avec 2 jobs (~55 lignes)
- Installation dépendances spécifiques (pas pywin32 pour Linux)
- Sélecteurs CSS corrigés (#messageInput, #envoyerBtn, #dark-mode-switch)
- Timeout WebDriverWait 30s pour réponses LLM

**Concepts appris**

- pytest (framework tests Python)
- TestClient FastAPI (simulation requêtes HTTP sans serveur)
- Assertions et pattern AAA (Arrange-Act-Assert)
- Selenium WebDriver (automatisation navigateur)
- ChromeDriver et mode headless
- Sélecteurs CSS (#id, .class, tag)
- WebDriverWait (attentes explicites)
- GitHub Actions (CI/CD automatique)
- Workflows YAML (jobs, steps, runners Ubuntu)
- Badge status tests

### [Session 7] - 2026-01-16

**Ajouté**

- Variables CSS pour mode clair et mode sombre (`:root`, `.dark-mode`)
- Switch dark mode animé dans header (icônes ☀️/🌙)
- Persistance préférence utilisateur avec localStorage
- 17 variables CSS pour couleurs réutilisables
- Fonction `toggleDarkMode()` en JavaScript
- Détection et application automatique du thème au chargement
- Documentation complète Session 7

**Modifié**

- `frontend/style.css` : Ajout variables CSS (~50 lignes) + switch (~40 lignes)
- `frontend/index.html` : Ajout switch dans header (~4 lignes)
- `frontend/app.js` : Ajout gestion dark mode (~20 lignes)
- Toutes les couleurs fixes remplacées par variables CSS
- Couleurs adaptées pour excellent contraste en mode sombre

**Concepts appris**

- Variables CSS (`:root`, `var()`, redéfinition)
- Classes conditionnelles (`.dark-mode` sur body)
- localStorage (`setItem()`, `getItem()`)
- Toggle classes JavaScript (`classList.toggle()`, `classList.contains()`)
- Event listeners (`change` sur checkbox)
- Switch CSS personnalisé (styling checkbox)
- Persistance préférences navigateur

### [Session 6] - 2026-01-14

**Ajouté**

- Auto-scroll automatique vers nouveaux messages (`scrollTop = scrollHeight`)
- Gestion erreurs avec `.catch()` et message poli
- Bouton Clear "🗑️ Effacer conversation" dans header
- Désactivation bouton pendant traitement (`disabled`)
- Style CSS pour message d'erreur (`.message-error`, `.bulle-error`)
- Style CSS pour bouton désactivé (`#envoyerBtn:disabled`)
- Style CSS header Flexbox (`#headerBar`)
- Fonction `effacerConversation()` dans JavaScript
- Documentation complète Session 6

**Modifié**

- `frontend/index.html` : Header Flexbox avec titre + bouton Clear
- `frontend/app.js` : Ajout 3x auto-scroll, bloc `.catch()`, désactivation/réactivation bouton
- `frontend/style.css` : Styles pour header, bouton Clear, message erreur, bouton désactivé

**Concepts appris**

- Auto-scroll JavaScript (`scrollTop`, `scrollHeight`)
- Gestion erreurs Promesses (`.catch()`)
- Manipulation DOM (`innerHTML = ""`, `disabled`)
- Pseudo-classe CSS (`:disabled`)
- Flexbox avancé (`justify-content: space-between`, `flex: 1`)
- Pattern UX : Désactiver → Traiter → Réactiver

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
- ✅ Auto-scroll automatique vers nouveaux messages
- ✅ Gestion des erreurs avec messages polis
- ✅ Bouton Clear pour vider conversation
- ✅ Désactivation bouton pendant traitement
- ✅ Dark mode avec switch et localStorage
- ✅ Variables CSS pour thèmes clair/sombre
- ✅ Tests pytest backend (4 tests endpoints)
- ✅ Tests Selenium frontend (3 tests UI)
- ✅ GitHub Actions CI/CD opérationnel
- ✅ Badge status tests dans README
- ✅ Documentation structurée (Sessions 0 à 8)
- 🎉 **Application complète, testée et professionnelle !**
- 🔜 Prochaine étape : Déploiement (Render + GitHub Pages)
