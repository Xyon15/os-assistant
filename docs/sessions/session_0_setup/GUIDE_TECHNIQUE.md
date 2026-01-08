# Guide Technique — Session 0

> Explications détaillées du code et des concepts

---

## 📋 Table des matières

1. [Comprendre FastAPI](#1-comprendre-fastapi)
2. [Structure du code](#2-structure-du-code)
3. [Explications ligne par ligne](#3-explications-ligne-par-ligne)
4. [Commandes importantes](#4-commandes-importantes)
5. [Troubleshooting](#5-troubleshooting)

---

## 1. Comprendre FastAPI

### C'est quoi FastAPI ?

FastAPI est un **framework web Python** qui te permet de créer des APIs facilement.

**Les 3 avantages principaux :**

1. **Rapide à écrire** : Quelques lignes suffisent pour créer une route
2. **Documentation automatique** : Génère `/docs` automatiquement
3. **Validation automatique** : Vérifie les données envoyées

### Alternative : Flask

Flask est plus ancien et un peu plus simple, mais FastAPI est plus moderne et plus performant.

---

## 2. Structure du code

### Architecture de base

```
Client (Navigateur)
    ↓
    GET http://localhost:8000/ping
    ↓
FastAPI (backend/main.py)
    ↓
    Fonction get_ping()
    ↓
    Return {"status": "pong"}
    ↓
Client reçoit le JSON
```

---

## 3. Explications ligne par ligne

### Code complet (à écrire dans cette session)

```python
# 1. Importer FastAPI
from fastapi import FastAPI

# 2. Créer une instance de FastAPI
app = FastAPI()

# 3. Définir une route
@app.get("/ping")
def get_ping():
    return {"status": "pong"}
```

### Explication détaillée

**Ligne 1-2 : Import**

```python
from fastapi import FastAPI
```

- On importe la classe `FastAPI` depuis le package `fastapi`
- C'est comme importer `random` ou `os` : on charge un module externe

**Ligne 4-5 : Création de l'application**

```python
app = FastAPI()
```

- On crée une **instance** de FastAPI
- `app` est l'objet principal qui va gérer toutes les routes
- C'est comme créer une liste vide : `ma_liste = []`

**Ligne 7-8 : Décorateur de route**

```python
@app.get("/ping")
```

- `@` = **décorateur** (syntaxe Python pour modifier une fonction)
- `.get()` = méthode HTTP GET (lecture de données)
- `"/ping"` = chemin de la route (l'URL sera `/ping`)
- **Résultat** : cette fonction sera appelée quand on accède à `/ping`

**Ligne 9-10 : Fonction handler**

```python
def get_ping():
    return {"status": "pong"}
```

- Fonction Python normale qui retourne un dictionnaire
- FastAPI convertit automatiquement ce dictionnaire en JSON
- Le client reçoit : `{"status": "pong"}`

---

## 4. Commandes importantes

### Activer l'environnement virtuel (Windows PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

**Pourquoi ?** Pour utiliser les packages Python installés localement dans ce projet.

### Installer les dépendances

```powershell
pip install -r requirements.txt
```

**Pourquoi ?** Pour installer `fastapi` et `uvicorn` nécessaires au projet.

### Lancer le serveur

```powershell
uvicorn backend.main:app --reload
```

**Détails :**

- `uvicorn` = serveur ASGI qui fait tourner FastAPI
- `backend.main` = chemin vers le fichier (`backend/main.py`)
- `:app` = nom de la variable dans le fichier
- `--reload` = redémarre automatiquement si tu modifies le code

### Tester la route

**Option 1 : Navigateur**

```
http://127.0.0.1:8000/ping
```

**Option 2 : Documentation auto**

```
http://127.0.0.1:8000/docs
```

**Option 3 : PowerShell (curl)**

```powershell
curl http://127.0.0.1:8000/ping
```

---

## 5. Troubleshooting

### Problème : "uvicorn: command not found"

**Cause :** Le venv n'est pas activé ou uvicorn n'est pas installé.

**Solution :**

```powershell
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Problème : "Address already in use"

**Cause :** Le port 8000 est déjà utilisé par un autre programme.

**Solution :** Change le port :

```powershell
uvicorn backend.main:app --reload --port 8001
```

### Problème : "No module named 'fastapi'"

**Cause :** fastapi n'est pas installé.

**Solution :**

```powershell
pip install fastapi uvicorn
```

---

## 📚 Pour aller plus loin

### Questions à te poser

1. Que se passe-t-il si je change `"/ping"` en `"/test"` ?
2. Comment ajouter une deuxième route `/hello` ?
3. Que retourne FastAPI si ma fonction ne retourne rien ?

### Mini-exercice

Essaie d'ajouter une route `/status` qui retourne `{"alive": true}`.

---

_Document créé le : 2026-01-08_
