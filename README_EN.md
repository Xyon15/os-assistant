<div style="font-family: Arial, sans-serif; text-align: center; font-size: 30px">OS Assistant</div>

> Productivity-oriented personal AI assistant

<div style="text-align: center;">
    <a href="README_FR.md">🇫🇷 Version française</a>
</div>

## Live Service Status

![Tests](https://github.com/Xyon15/os-assistant/actions/workflows/tests.yml/badge.svg)

[![Backend uptime](https://img.shields.io/uptimerobot/status/m802190707-d0e3a39848760de34f826234?label=Backend%20status&style=flat-square&logo=render)](https://stats.uptimerobot.com/a4Q7kpTig9)

[![Frontend uptime](https://img.shields.io/uptimerobot/status/m802190746-183f3a09139cdc8eebe0ab5a?label=Frontend%20status&style=flat-square&logo=github)](https://stats.uptimerobot.com/a4Q7kpTig9)

## 🎯 Project Goals

Build a personal assistant with:

- Python backend (FastAPI)
- Lightweight web client (HTML/CSS/JS)
- AI integration (LLM API)

## 🛠️ Tech Stack

- **Backend:** [![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python)](https://www.python.org/downloads/) [![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1+-green.svg?logo=fastapi)](https://fastapi.tiangolo.com/) [![Uvicorn](https://img.shields.io/badge/Uvicorn-0.24.0+-cyan.svg)](https://www.uvicorn.org/)
- **Frontend:** [![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML) [![CSS3](https://img.shields.io/badge/CSS-8A05FF?logo=css&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS) [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- **AI API:** Github models (Temporary)

---

### API documentation via Render server: https://os-assistant-backend.onrender.com/docs

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

<div>
<h1>This project is published on Flavortown:</h1>
Flavortown is a platform for sharing and discovering open source projects. It allows young developers to publish, document, and share their projects with the community.

<div style="display:flex; align-items:center; justify-content:space-between; max-width:700px; margin:0 auto;">
    <p style="margin:0; text-align:left; flex:1;">Feel free to visit the project page!</p>
    <a href="https://flavortown.hackclub.com"><img src="https://www.genroam.io/flavourtown/sticker.webp" alt="Flavortown Sticker" style="margin-left:20px; width:150px; height:auto; display:block;" /></a>
</div>

</div>
