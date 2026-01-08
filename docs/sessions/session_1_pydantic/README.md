# Session 1 — Validation avec Pydantic

> **Date :** 2026-01-08  
> **Durée :** ~45 minutes  
> **Prérequis :** Session 0 (FastAPI de base)

---

## 🎯 Objectifs de cette session

### Ce que tu vas apprendre

- ✅ Comprendre ce qu'est Pydantic et pourquoi c'est utile
- ✅ Créer un modèle de données (classe Pydantic)
- ✅ Valider automatiquement les entrées utilisateur
- ✅ Créer un endpoint POST pour recevoir des données
- ✅ Gérer les champs obligatoires et facultatifs

### Ce que tu vas créer

- Un modèle `Message` avec validation automatique
- Un endpoint `POST /message` qui accepte et valide des messages
- Des tests pour vérifier que la validation fonctionne

---

## 📚 Concepts appris

### 1. Pydantic = Agent de sécurité automatique

**Analogie :** Ton API est un aéroport, Pydantic est l'agent de sécurité qui vérifie chaque passager (donnée).

**Sans Pydantic :**

- Tu dois vérifier manuellement chaque donnée
- Risque d'oublier des vérifications
- Code compliqué avec plein de `if`

**Avec Pydantic :**

- Validation automatique
- Erreurs claires si données incorrectes
- Code simple et lisible

### 2. BaseModel = Classe spéciale

```python
from pydantic import BaseModel

class Message(BaseModel):
    texte: str              # Champ obligatoire (type texte)
    nom_utilisateur: str = None  # Champ facultatif (défaut = None)
```

**Points clés :**

- `BaseModel` : classe de base fournie par Pydantic
- `:` (deux-points) : déclare le type d'un champ
- `= None` : rend le champ facultatif avec une valeur par défaut

### 3. Validation automatique

Pydantic vérifie automatiquement :

- ✅ Les champs obligatoires sont présents
- ✅ Les types sont corrects (str, int, bool, etc.)
- ✅ Les formats sont valides

Si erreur → message clair renvoyé automatiquement.

---

## 💻 Code final

Voir [scripts/main.py](scripts/main.py) pour le code complet.

### Structure du code

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modèle Pydantic
class Message(BaseModel):
    texte: str
    nom_utilisateur: str = None

# Endpoint GET existant
@app.get("/ping")
def get_ping():
    return {"status": "pong"}

# Nouveau endpoint POST
@app.post("/message")
def recevoir_message(msg: Message):
    return {
        "recu": True,
        "texte": msg.texte,
        "utilisateur": msg.nom_utilisateur or "Anonyme"
    }
```

---

## 🧪 Tests réalisés

### Test 1 : Message sans nom d'utilisateur ✅

**Envoi :**

```json
{
  "texte": "Mon premier message !"
}
```

**Résultat :**

```json
{
  "recu": true,
  "texte": "Mon premier message !",
  "utilisateur": "Anonyme"
}
```

### Test 2 : Message avec nom d'utilisateur ✅

**Envoi :**

```json
{
  "texte": "Deuxième test",
  "nom_utilisateur": "Alice"
}
```

**Résultat :**

```json
{
  "recu": true,
  "texte": "Deuxième test",
  "utilisateur": "Alice"
}
```

### Test 3 : Validation (champ manquant) ✅

**Envoi :**

```json
{
  "nom_utilisateur": "Bob"
}
```

**Résultat (erreur attendue) :**

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "texte"],
      "msg": "Field required",
      "input": { "nom_utilisateur": "Bob" }
    }
  ]
}
```

---

## 📝 Commandes rapides

### Démarrer le serveur

```powershell
# Activer venv
venv\Scripts\Activate.ps1

# Lancer serveur
uvicorn backend.main:app --reload
```

### Tester les endpoints

- Documentation auto : http://127.0.0.1:8000/docs
- GET /ping : http://127.0.0.1:8000/ping
- POST /message : utiliser `/docs` → Try it out

---

## 🔑 Points clés à retenir

1. **Pydantic valide automatiquement** les données → tu n'as rien à coder
2. **BaseModel** = classe de base pour créer des modèles
3. **Champs obligatoires** : `nom: type`
4. **Champs facultatifs** : `nom: type = valeur_defaut`
5. **FastAPI + Pydantic** = documentation automatique dans `/docs`

---

## 🚀 Prochaine session

**Session 2 — Persistance avec SQLite**

- Sauvegarder les messages dans une base de données
- Lire les messages sauvegardés
- Apprendre SQL de base

---

## 📖 Ressources

- [Guide technique détaillé](GUIDE_TECHNIQUE.md)
- [Code final](scripts/main.py)
- [Documentation officielle Pydantic](https://docs.pydantic.dev/)
