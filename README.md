# OS Assistant

> Productivity-oriented personal AI assistant

**[🇫🇷 Version française](README.md)**

## Live Service Status

![Tests](https://github.com/Xyon15/os-assistant/actions/workflows/tests.yml/badge.svg)

[![Backend uptime](https://img.shields.io/uptimerobot/status/m802190707-d0e3a39848760de34f826234?label=Backend%20status&style=flat-square&logo=render)](https://stats.uptimerobot.com/a4Q7kpTig9)

[![Frontend uptime](https://img.shields.io/uptimerobot/status/m802190746-183f3a09139cdc8eebe0ab5a?label=Frontend%20status&style=flat-square&logo=github)](https://stats.uptimerobot.com/a4Q7kpTig9)

## 🎯 Project Goals

Build a personal assistant with:

- Python backend (FastAPI)
- Lightweight web client (HTML/CSS/JS)
- AI integration (LLM API)

## 🧠 Vision

OS Assistant aims to become an intelligent office companion,
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
  Sends a message to the LLM.  
  **Expected payload**: `{"message": "..."}` (validated by Pydantic)  
  **Response**: `{"reponse": "<text returned by the LLM>"}`  
  **Implementation**: calls `backend.ai.demander_llm()` (uses environment variables `GITHUB_TOKEN` and `MODEL_NAME`)

### 🚀 Deployed Services

- **Backend**: deployed on Render — https://os-assistant-backend.onrender.com
- **Swagger Documentation**: https://os-assistant-backend.onrender.com/docs
- **Frontend**: deployed on GitHub Pages — https://xyon15.github.io/os-assistant

### 🧪 Tests, CI and Monitoring

- **CI (GitHub Actions)**: `Tests (tests.yml)` workflow
  - Backend job: installs dependencies and runs `pytest tests/test_backend.py`
  - Frontend job: installs selenium/webdriver and runs `pytest tests/test_frontend.py` after the backend
- **Automated tests**:
  - Backend: `test_backend.py` (FastAPI TestClient — checks `/ping`, `/chat` validation)
  - Frontend: `test_frontend.py` (Selenium, UI tests in headless CI)
- **Monitoring / uptime**: UptimeRobot badges displayed in the README (backend + frontend)

## 🛠️ Tech Stack

- **Backend:** [![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python)](https://www.python.org/downloads/) [![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1+-green.svg?logo=fastapi)](https://fastapi.tiangolo.com/) [![Uvicorn](https://img.shields.io/badge/Uvicorn-0.24.0+-cyan.svg)](https://www.uvicorn.org/)
- **Frontend:** [![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML) [![CSS3](https://img.shields.io/badge/CSS-8A05FF?logo=css&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS) [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- **AI API:** Github models (Temporary)

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
- API documentation: http://127.0.0.1:8000/docs

<br>

## This project is published on Flavortown

<img src="https://www.genroam.io/flavourtown/sticker.webp" align="right" width="120" />

Flavortown is a platform for sharing and discovering open source projects. It allows young developers to publish, document, and share their projects with the community.

**Feel free to visit the project page!**

[See the Flavortown project page](https://flavortown.hackclub.com/)
