# OS Assistant

> Assistant personnel IA orienté productivité

**[🇬🇧 English Version](README_EN.md)**

## Status live des services :

![Tests](https://github.com/Xyon15/os-assistant/actions/workflows/tests.yml/badge.svg)

[![Backend uptime](https://img.shields.io/uptimerobot/status/m802190707-d0e3a39848760de34f826234?label=Backend%20status&style=flat-square&logo=render)](https://stats.uptimerobot.com/a4Q7kpTig9)

[![Frontend uptime](https://img.shields.io/uptimerobot/status/m802190746-183f3a09139cdc8eebe0ab5a?label=Frontend%20status&style=flat-square&logo=github)](https://stats.uptimerobot.com/a4Q7kpTig9)

[![DB uptime](https://img.shields.io/uptimerobot/status/m802287025-46bedf5420248ab2dbb6e18f?label=Database%20status&style=flat-square&logo=supabase)](https://stats.uptimerobot.com/a4Q7kpTig9)

## 🎯 Objectifs du projet

Construire un assistant personnel avec :

- Backend Python (FastAPI)
- Client web léger (HTML/CSS/JS)
- Intégration IA (LLM API)

## 🧠 Vision

OS Assistant a pour objectif de devenir un compagnon de bureau intelligent,
capable d'assister l'utilisateur dans ses tâches quotidiennes tout en restant
simple, léger et évolutif.

À terme, le projet vise :

- une interface orientée productivité
- une évolution vers une application desktop

## ✨ Fonctionnalités actuelles

### 🔌 Endpoints (API Backend)

- **GET /ping** ✅  
  Vérifie que le serveur répond.  
  **Réponse** : `{"status": "pong"}`

- **POST /chat** 💬  
  Envoie un message au LLM.  
  **Payload attendu** : `{"message": "..."}` (validé par Pydantic)  
  **Réponse** : `{"reponse": "<texte retourné par le LLM>"}`  
  **Implémentation** : appelle `backend.ai.demander_llm()` (utilise les variables d’environnement `GITHUB_TOKEN` et `MODEL_NAME`)
- **GET /health** 💚  
  Vérification de santé avec uptime.  
  **Réponse** : `{"status": "healthy", "uptime": 123.45}`

- **GET /metrics** 📊  
  Métriques de l'application (total requêtes, uptime lisible).  
  **Réponse** : `{"total_requetes": 5, "total_historique": 42, "uptime_seconds": 3665.12, "uptime_lisible": "1h 1m 5s"}`

- **GET /stats** 📈  
  Statistiques de la base de données (temps de réponse moyen, nombre d'erreurs).  
  **Réponse** : `{"temps_moyen_total": 2.12, "temps_moyen_llm": 1.71, "total_requetes_logees": 42, "total_erreurs": 0}`

### 🚀 Services déployés

- **Backend** : déployé sur Render — https://os-assistant-backend.onrender.com
- **Documentation Swagger** : https://os-assistant-backend.onrender.com/docs
- **Frontend** : déployé sur GitHub Pages — https://xyon15.github.io/os-assistant
- **Base de données** : Supabase (PostgreSQL) — https://supabase.com/

### 🧪 Tests, CI et Monitoring

- **CI (GitHub Actions)** : workflow `Tests (tests.yml)`
  - Job backend : installe dépendances et exécute `pytest tests/test_backend.py`
  - Job frontend : installe selenium/webdriver et exécute `pytest tests/test_frontend.py` après le backend
- **Tests automatisés** :
  - Backend : `test_backend.py` (TestClient FastAPI — vérifie `/ping`, validation `/chat`)
  - Frontend : `test_frontend.py` (Selenium, tests d’UI en headless CI)
- **Monitoring UptimeRobot** :
  - Maintient le backend (Render) + base de données (Supabase) actifs 24/7
  - Badges de statut affichés dans le README (backend + frontend + base de données)

### 📊 Base de données & Persistance

- **PostgreSQL (Supabase)** : Base de données cloud
- **Logs persistants** : Métriques et logs de requêtes stockés en permanence dans le cloud
- **Suivi des statistiques** : Temps de réponse moyens (total vs LLM), taux d'erreurs, nombre de requêtes

## 🛠️ Tech Stack

- **Backend :** [![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python)](https://www.python.org/downloads/) [![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1+-green.svg?logo=fastapi)](https://fastapi.tiangolo.com/) [![Uvicorn](https://img.shields.io/badge/Uvicorn-0.24.0+-cyan.svg)](https://www.uvicorn.org/)
- **Frontend :** [![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/fr/docs/Web/HTML) [![CSS3](https://img.shields.io/badge/CSS-8A05FF?logo=css&logoColor=white)](https://developer.mozilla.org/fr/docs/Web/CSS) [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/fr/docs/Web/JavaScript)
- **Base de données :** [![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?logo=supabase&logoColor=white)](https://supabase.com/)
- **API IA :** Github models (Temporaire)

## 🔐 Variables d'environnement

Variables requises dans `.env` :

- `GITHUB_TOKEN` : Token API GitHub Models
- `MODEL_NAME` : Modèle LLM (ex: gpt-4o)
- `DATABASE_URL` : Chaîne de connexion PostgreSQL (Supabase Session Pooler)

## 🚀 Démarrage de l'API

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

### Tester en local

- API ping test : http://127.0.0.1:8000/ping
- Métriques : http://127.0.0.1:8000/metrics
- Statistiques : http://127.0.0.1:8000/stats
- Documentation de l'API : http://127.0.0.1:8000/docs

## 🚀 Déploiement

### Backend (Render)

1. Connectez votre dépôt GitHub à Render
2. Ajoutez les variables d'environnement :
   - `GITHUB_TOKEN` : Votre token API GitHub Models
   - `MODEL_NAME` : Nom du modèle LLM (ex: `gpt-4o`)
   - `DATABASE_URL` : Chaîne de connexion PostgreSQL Supabase
3. Déployez depuis la branche `main`

### Base de données (Supabase)

1. Créez un nouveau projet avec PostgreSQL 17
2. Allez dans **Settings → Database**
3. Copiez la **Connection string** en mode **Session** (compatible IPv4)
4. Format : `postgresql://postgres.PROJECT_ID:PASSWORD@aws-1-eu-central-1.pooler.supabase.com:5432/postgres`

<br>

<div>

## Ce projet est publié sur Flavortown

<img src="https://www.genroam.io/flavourtown/sticker.webp" align="right" width="120" />

Flavortown est une plateforme de partage et de découverte de projets open source. Elle permet aux jeunes développeurs de publier leurs projets, de les documenter et de les partager avec la communauté.

**N'hésitez pas à aller visiter la page du projet !**

[Voir la page Flavortown du projet](https://flavortown.hackclub.com/projects/11493)
