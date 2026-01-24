<div style= "font-family: Arial, sans-serif; text-align: center; font-size: 30px">OS Assistant</div>

> Assistant personnel IA orienté productivité

<div style="text-align: center;">
    <a href="README_EN.md">🇬🇧 English Version</a>
</div>

## Status live des services :

![Tests](https://github.com/Xyon15/os-assistant/actions/workflows/tests.yml/badge.svg)

[![Backend uptime](https://img.shields.io/uptimerobot/status/m802190707-d0e3a39848760de34f826234?label=Backend%20status&style=flat-square&logo=render)](https://stats.uptimerobot.com/a4Q7kpTig9)

[![Frontend uptime](https://img.shields.io/uptimerobot/status/m802190746-183f3a09139cdc8eebe0ab5a?label=Frontend%20status&style=flat-square&logo=github)](https://stats.uptimerobot.com/a4Q7kpTig9)

## 🎯 Objectifs du projet

Construire un assistant personnel avec :

- Backend Python (FastAPI)
- Client web léger (HTML/CSS/JS)
- Intégration IA (LLM API)

## 🛠️ Tech Stack

- **Backend :** [![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python)](https://www.python.org/downloads/) [![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1+-green.svg?logo=fastapi)](https://fastapi.tiangolo.com/) [![Uvicorn](https://img.shields.io/badge/Uvicorn-0.24.0+-cyan.svg)](https://www.uvicorn.org/)
- **Frontend :** [![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/fr/docs/Web/HTML) [![CSS3](https://img.shields.io/badge/CSS-8A05FF?logo=css&logoColor=white)](https://developer.mozilla.org/fr/docs/Web/CSS) [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/fr/docs/Web/JavaScript)
- **API IA :** Github models (Temporaire)

---

### Documentation de l'api via le serveur render : https://os-assistant-backend.onrender.com/docs

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
- Documentation de l'API : http://127.0.0.1:8000/docs

<br>

<div>
<h1>Ce projet est publié sur Flavortown :</h1>
Flavortown est une plateforme de partage et de découverte de projets open source. Elle permet aux jeunes développeurs de publier leurs projets, de les documenter et de les partager avec la communauté.

<div style="display:flex; align-items:center; justify-content:space-between; max-width:700px; margin:0 auto;">
    <p style="margin:0; text-align:left; flex:1;">N'hésitez pas à aller visiter la page du projet!</p>
    <a href="https://flavortown.hackclub.com"><img src="https://www.genroam.io/flavourtown/sticker.webp" alt="Flavortown Sticker" style="margin-left:20px; width:150px; height:auto; display:block;" /></a>
</div>

</div>
