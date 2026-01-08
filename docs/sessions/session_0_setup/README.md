# Session 0 — Setup & Premier serveur FastAPI

> **Date :** 2026-01-08  
> **Durée estimée :** 30-40 minutes  
> **Niveau :** Débutant

---

## 🎯 Objectifs de cette session

- ✅ Comprendre ce qu'est une API REST
- ✅ Comprendre le modèle client/serveur
- ✅ Structurer proprement le projet
- ✅ Écrire un premier endpoint `/ping` avec FastAPI
- ✅ Lancer et tester le serveur localement

---

## 📚 Concepts appris

### 1. API (Application Programming Interface)

Une API est l'intermédiaire entre un client (navigateur) et un serveur (backend Python). Elle permet de faire des requêtes et recevoir des réponses.

### 2. FastAPI

Framework Python moderne pour créer des APIs rapidement avec documentation automatique.

### 3. Routes (endpoints)

Chemins comme `/ping` qui correspondent à des actions spécifiques.

### 4. JSON

Format de données qui ressemble aux dictionnaires Python : `{"clé": "valeur"}`

---

## 🛠️ Ce qu'on a construit

Un serveur FastAPI minimal avec :

- Un endpoint `GET /ping` qui retourne `{"status": "pong"}`
- Documentation automatique sur `/docs`

---

## 📂 Fichiers modifiés

- `backend/main.py` : Serveur FastAPI avec route /ping
- `requirements.txt` : Ajout de fastapi et uvicorn

---

## 🧪 Comment tester

```powershell
# 1. Activer l'environnement virtuel
venv\Scripts\Activate.ps1

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer le serveur
uvicorn backend.main:app --reload

# 4. Tester dans le navigateur
# Ouvrir : http://127.0.0.1:8000/ping
# Ouvrir : http://127.0.0.1:8000/docs
```

---

## 📖 Documentation détaillée

Consulte [GUIDE_TECHNIQUE.md](GUIDE_TECHNIQUE.md) pour les explications ligne par ligne.

---

## ✅ Checklist de fin de session

- [ ] Structure `docs/` créée
- [ ] `backend/main.py` complété
- [ ] Serveur lancé avec succès
- [ ] Endpoint `/ping` testé et fonctionnel
- [ ] Documentation automatique `/docs` consultée

---

## 🔜 Prochaine session

**Session 1 — Validation de données avec Pydantic**

- Apprendre à valider les entrées utilisateur
- Créer des modèles de données
- Gérer les erreurs proprement

---

_Session complétée le : ****\_\_\_****_
