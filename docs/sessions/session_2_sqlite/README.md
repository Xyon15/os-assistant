# Session 2 — Persistance avec SQLite

> **Date :** 2026-01-08  
> **Chat :** 3  
> **Durée :** ~2h  
> **Objectif :** Apprendre SQLite et sauvegarder les messages dans une base de données

---

## 🎯 Objectifs de la session

- Comprendre ce qu'est SQLite (base de données persistante)
- Créer une base de données et une table
- Sauvegarder des messages dans la DB
- Récupérer les messages sauvegardés
- Intégrer SQLite dans FastAPI

---

## ✅ Ce qui a été accompli

### 1. **Création du module `backend/memory.py`**

Module complet pour gérer la persistance avec SQLite :

- `initialiser_db()` : Créer la table "messages"
- `sauvegarder_message(texte, nom_utilisateur)` : Ajouter un message
- `recuperer_messages()` : Récupérer tous les messages

### 2. **Intégration dans FastAPI (`backend/main.py`)**

- **Lifespan** : Initialiser la DB au démarrage (méthode moderne)
- **POST `/message`** : Sauvegarde maintenant dans SQLite
- **GET `/messages`** : Nouveau endpoint pour lire les messages

### 3. **Tests réussis**

- ✅ Swagger (http://127.0.0.1:8000/docs) : Tous les endpoints fonctionnent
- ✅ Messages persistants après redémarrage
- ✅ Données structurées avec id, texte, nom_utilisateur, date_creation

---

## 📂 Fichiers créés/modifiés

### Nouveaux fichiers

```
backend/
└── memory.py          ✅ Module de gestion SQLite (3 fonctions)
memory.db              ✅ Base de données SQLite (créée automatiquement)
```

### Fichiers modifiés

```
backend/main.py        ✅ Intégration SQLite + lifespan + GET /messages
```

---

## 🧪 Tests à reproduire

### 1. Démarrer le serveur

```powershell
uvicorn backend.main:app --reload
```

### 2. Ouvrir Swagger

http://127.0.0.1:8000/docs

### 3. Tester POST `/message`

```json
{
  "texte": "Mon premier message persistant",
  "nom_utilisateur": "Alice"
}
```

**Résultat attendu :** `{"recu": true}`

### 4. Tester GET `/messages`

**Résultat attendu :**

```json
{
  "messages": [
    {
      "id": 1,
      "texte": "Mon premier message persistant",
      "nom_utilisateur": "Alice",
      "date_creation": "2026-01-08T14:30:00.123456"
    }
  ],
  "total": 1
}
```

### 5. Redémarrer le serveur et re-tester GET `/messages`

**Résultat attendu :** Les messages sont toujours là ! (persistance)

---

## 🎓 Concepts appris

### SQLite

- Base de données relationnelle dans un fichier (memory.db)
- Tables, colonnes, lignes (comme Excel)
- Persistance : données conservées après redémarrage
- Module `sqlite3` inclus dans Python (pas d'installation)

### SQL (Structured Query Language)

- `CREATE TABLE` : Créer une table
- `INSERT INTO` : Ajouter des données
- `SELECT * FROM` : Récupérer des données
- `?` placeholders : Sécurité contre injections SQL

### FastAPI avancé

- **Lifespan** : Remplace `@app.on_event("startup")` (nouvelle méthode)
- `@asynccontextmanager` : Gérer le cycle de vie (démarrage/arrêt)
- `yield` : Séparer code démarrage / code arrêt

### Python avancé

- `cursor.fetchall()` : Récupérer toutes les lignes SQL
- Boucles `for` pour transformer tuples en dictionnaires
- `datetime.now().isoformat()` : Format ISO pour dates
- `Optional[str]` : Type qui peut être str ou None

---

## 📚 Documentation complète

- [GUIDE_TECHNIQUE.md](GUIDE_TECHNIQUE.md) : Explications détaillées ligne par ligne
- [scripts/memory.py](scripts/memory.py) : Code final du module SQLite
- [scripts/main.py](scripts/main.py) : Code final de l'API FastAPI

---

## 🚀 Prochaine session suggérée

**Session 3 — Intégration LLM (API externe)**

- Appeler une API LLM (OpenAI, Anthropic, Ollama)
- Créer un module `backend/ai.py`
- Fonction `ask_llm(prompt) -> str`
- Nouveau endpoint POST `/chat` qui utilise le LLM

---

_Dernière mise à jour : 2026-01-08_
