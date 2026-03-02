<div align="center">
  <img src="docs/images/logo.png" alt="Workly Logo" width="100" />
  <h1>Workly</h1>
  <p><em>Productivity-oriented personal AI assistant</em></p>
  <img src="docs/images/demo.gif" alt="Workly Demo" width="680" />
</div>
<br/>
<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-4051B5?style=for-the-badge&logo=gunicorn&logoColor=white)](https://www.uvicorn.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-8A05FF?style=for-the-badge&logo=css&logoColor=white)](https://developer.mozilla.org/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/docs/Web/JavaScript)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)
[![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io/)
[![GitHub Models](https://img.shields.io/badge/GitHub%20Models-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/marketplace/models)

</div>

**[🇫🇷 Version française](README.md)**

## Live Service Status

![Tests](https://github.com/Xyon15/os-assistant/actions/workflows/tests.yml/badge.svg)

[![Backend uptime](https://img.shields.io/uptimerobot/status/m802190707-d0e3a39848760de34f826234?label=Backend%20status&style=flat-square&logo=render)](https://stats.uptimerobot.com/a4Q7kpTig9)

[![Frontend uptime](https://img.shields.io/uptimerobot/status/m802190746-183f3a09139cdc8eebe0ab5a?label=Frontend%20status&style=flat-square&logo=github)](https://stats.uptimerobot.com/a4Q7kpTig9)

[![DB uptime](https://img.shields.io/uptimerobot/status/m802287025-46bedf5420248ab2dbb6e18f?label=Database%20status&style=flat-square&logo=supabase)](https://stats.uptimerobot.com/a4Q7kpTig9)

## 🎯 Project Goals

Build a personal assistant with:

- Python backend (FastAPI)
- Lightweight web client (HTML/CSS/JS)
- AI integration (LLM API)

## 🧠 Vision

Workly aims to become an intelligent office companion,
capable of assisting users in their daily tasks while remaining
simple, lightweight, and scalable.

In the long term, the project targets:

- a productivity-oriented interface
- an evolution towards a desktop application

## ✨ Current Features

### 🔌 Endpoints (Backend API)

- **GET /ping** ✅  
  Checks if the server is responding.  
  **Response**: `{"status": "pong"}`

- **POST /chat** 💬  
  Sends a message to the LLM. **Requires authentication (Bearer token).**  
  **Expected payload**: `{"message": "..."}` (validated by Pydantic)  
  **Response**: `{"reponse": "<text returned by the LLM>"}`  
  **Implementation**: calls `backend.ai.demander_llm()` (uses environment variables `GITHUB_TOKEN` and `MODEL_NAME`)

- **POST /register** 📝  
  Creates a new user account.  
  **Expected payload**: `{"username": "...", "email": "...", "password": "..."}` (unique username & email)  
  **Response**: `{"message": "Compte créé avec succès"}`

- **POST /login** 🔑  
  Authenticates a user and returns a JWT token.  
  **Expected payload**: OAuth2 form (`username` + `password`)  
  **Response**: `{"access_token": "...", "token_type": "bearer", "username": "..."}`

- **GET /me** 👤  
  Verifies the JWT token is still valid.  
  **Requires**: `Authorization: Bearer <token>` header  
  **Response**: `{"username": "..."}` or `401` if expired

- **GET /health** 💚  
  Health check with uptime.  
  **Response**: `{"status": "healthy", "uptime": 123.45}`

- **GET /metrics** 📊  
  Application metrics (total requests, uptime readable).  
  **Response**: `{"total_requetes": 5, "total_historique": 42, "uptime_seconds": 3665.12, "uptime_lisible": "1h 1m 5s"}`

- **GET /stats** 📈  
  Database statistics (avg response time, error count).  
  **Response**: `{"temps_moyen_total": 2.12, "temps_moyen_llm": 1.71, "total_requetes_logees": 42, "total_erreurs": 0}`

### 🚀 Deployed Services

- **Backend**: deployed on Render — https://os-assistant-backend.onrender.com
- **Swagger Documentation**: https://os-assistant-backend.onrender.com/docs
- **Frontend**: deployed on GitHub Pages — https://xyon15.github.io/os-assistant
- **Database**: Supabase (PostgreSQL) — https://supabase.com/

### 🧪 Tests, CI and Monitoring

- **CI (GitHub Actions)**: `Tests (tests.yml)` workflow
  - Backend job: installs dependencies and runs `pytest tests/test_backend.py`
  - Frontend job: installs selenium/webdriver and runs `pytest tests/test_frontend.py` after the backend
- **Automated tests**:
  - Backend: `test_backend.py` (FastAPI TestClient — checks `/ping`, `/chat` validation)
  - Frontend: `test_frontend.py` (Selenium, UI tests in headless CI)
- **UptimeRobot Monitoring**:
  - Keeps backend (Render) + database (Supabase) active 24/7
  - Status badges displayed in README (backend + frontend + database)

### 🔐 Authentication

- **JWT authentication**: Register/login flow with bcrypt password hashing
- **Protected routes**: `/chat` requires a valid Bearer token
- **Token verification**: `/me` endpoint validates token on page load, auto-redirect to login if expired
- **Duplicate detection**: Username and email uniqueness enforced (PostgreSQL constraints)

### Database & Persistence

- **PostgreSQL (Supabase)**: Cloud database
- **Persistent logging**: Metrics and request logs stored permanently in cloud
- **Statistics tracking**: Average response times (total vs LLM), error rates, request counts

## 📸 Screenshots

<table align="center">
  <tr>
    <td align="center"><strong>Login</strong></td>
    <td align="center"><strong>Chat</strong></td>
  </tr>
  <tr>
    <td><img src="docs/images/screenshot-login.png" alt="Login page" width="480"/></td>
    <td><img src="docs/images/screenshot-chat.png" alt="Chat interface" width="480"/></td>
  </tr>
</table>

<br/>

## 🔐 Environment Variables

Required variables in `.env`:

- `GITHUB_TOKEN` : GitHub Models API token
- `MODEL_NAME` : LLM model (e.g., gpt-4o)
- `DATABASE_URL` : PostgreSQL connection string (Supabase Session Pooler)
- `SECRET_KEY` : JWT signing secret key
- `ACCESS_TOKEN_EXPIRE_MINUTES` : Token expiration in minutes (default: 30)

## 🚀 API Quickstart

### Prerequisites

- Python 3.10+
- Git

### Installation

```powershell
# Clone the project
git clone <repo-url>
cd os-assistant

# Create and activate the virtual environment
python -m venv venv
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn backend.main:app --reload
```

### Test locally

- API ping test: http://127.0.0.1:8000/ping
- Metrics: http://127.0.0.1:8000/metrics
- Statistics: http://127.0.0.1:8000/stats
- API documentation: http://127.0.0.1:8000/docs

## 🚀 Deployment

### Backend (Render)

1. Connect your GitHub repository to Render
2. Add environment variables:
   - `GITHUB_TOKEN`: Your GitHub Models API token
   - `MODEL_NAME`: LLM model name (e.g., `gpt-4o`)
   - `DATABASE_URL`: Supabase PostgreSQL connection string
3. Deploy from `main` branch

### Database (Supabase)

1. Create a new project with PostgreSQL 17
2. Go to **Settings → Database**
3. Copy **Connection string** in **Session mode** (IPv4 compatible)
4. Format: `postgresql://postgres.PROJECT_ID:PASSWORD@aws-1-eu-central-1.pooler.supabase.com:5432/postgres`

<br>

## This project is published on Flavortown

<img src="https://www.genroam.io/flavourtown/sticker.webp" align="right" width="120" />

Flavortown is a platform for sharing and discovering open source projects. It allows young developers to publish, document, and share their projects with the community.

**Feel free to visit the project page!**

[See the Flavortown project page](https://flavortown.hackclub.com/projects/11493)
