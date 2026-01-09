# Session 3 — Intégration LLM API

> **Date :** 2026-01-09  
> **Objectif :** Créer un endpoint `/chat` qui appelle une API LLM (GPT-4o) et sauvegarde les conversations

---

## 🎯 Objectifs de la session

1. Comprendre ce qu'est une API LLM et comment l'appeler
2. Créer un module `backend/ai.py` pour appeler GitHub Models (GPT-4o)
3. Gérer les secrets avec `.env` et `python-dotenv`
4. Créer l'endpoint POST `/chat` pour discuter avec le LLM
5. Modifier `memory.py` pour supporter les rôles (user/assistant)
6. Sauvegarder les conversations complètes dans SQLite

---

## 📚 Concepts appris

### **API LLM : "Appeler un ami expert"**

- Une API LLM = service distant qui génère du texte intelligent
- Différence avec SQLite : DB = chercher info déjà écrite, LLM = générer nouvelle réponse
- Requête HTTP POST avec JSON (comme Swagger appelle notre FastAPI)
- Nécessite une clé API (token secret) pour authentification

### **GitHub Models : LLM gratuit pour étudiants**

- Accès gratuit à GPT-4o, Claude 3.5 Sonnet, Llama, Mistral via GitHub Education
- URL : https://github.com/marketplace/models
- Rate-limited mais suffisant pour apprendre
- Alternative parfaite : gratuit + sans utiliser ressources PC locales

### **Fichier `.env` : Stocker les secrets**

- Fichier pour variables d'environnement (clés API, mots de passe)
- Format : `NOM_VARIABLE=valeur` (sans espaces, sans guillemets)
- TOUJOURS dans `.gitignore` → jamais committer les secrets
- Bibliothèque `python-dotenv` pour lire le `.env`

### **Gestion d'erreurs avec `try/except`**

- Bloc `try:` → code qui peut échouer (requête HTTP)
- Bloc `except Exception as e:` → que faire si erreur
- Pattern de réessai : boucle for + `time.sleep(2)` entre tentatives
- Message d'erreur poli si toutes les tentatives échouent

### **Rôles dans les conversations**

- `role="user"` → messages de l'utilisateur
- `role="assistant"` → réponses du LLM
- Permet de reconstruire l'historique de conversation
- Essentiel pour contexte multi-tours (futures sessions)

---

## ✅ Réalisations

### **1. Configuration `.env`**

```bash
GITHUB_TOKEN=ghp_...
MODEL_NAME=gpt-4o
```

### **2. Module `backend/ai.py` créé**

Fonction principale : `demander_llm(prompt: str) -> str`

**Fonctionnalités :**

- Charge le token depuis `.env` avec `os.getenv()`
- Construit requête HTTP vers GitHub Models API
- Réessaie **3 fois** en cas d'échec (avec délai 2 secondes)
- Retourne message d'erreur poli si échec total
- Extrait la réponse du JSON : `resultat["choices"][0]["message"]["content"]`

### **3. Modifications `backend/memory.py`**

- ✅ Ajout colonne `role TEXT` dans la table SQLite
- ✅ `sauvegarder_message()` accepte paramètre `role` (défaut : "user")
- ✅ `recuperer_messages()` retourne le champ `role` dans les dictionnaires
- ✅ DB recréée pour inclure la nouvelle colonne

### **4. Endpoint POST `/chat` dans `backend/main.py`**

- Nouveau modèle Pydantic : `ChatMessage(BaseModel)` avec champ `message: str`
- Import : `from backend.ai import demander_llm`

**Logique de l'endpoint :**

1. Recevoir question utilisateur
2. Sauvegarder avec `role="user"`
3. Appeler `demander_llm(message)`
4. Sauvegarder réponse avec `role="assistant"`
5. Retourner `{"reponse": "..."}`

### **5. Tests réussis**

✅ **Test `backend/ai.py` seul :** GPT-4o répond "Bonjour ! Comment puis-je vous aider ?"  
✅ **Test POST `/chat` :** Question sur PowerShell → réponse complète de GPT-4o  
✅ **Test GET `/messages` :** 2 messages sauvegardés (user + assistant) avec rôles corrects

---

## 🛠️ Commandes utilisées

### Installation des dépendances

```powershell
pip install python-dotenv requests
```

### Recréer la DB avec colonne role

```powershell
rm memory.db
python -c "from backend.memory import initialiser_db; initialiser_db(); print('DB recréée')"
```

### Tester le module ai.py

```powershell
python backend/ai.py
```

### Lancer le serveur

```powershell
uvicorn backend.main:app --reload
```

### Tester avec Swagger

http://127.0.0.1:8000/docs

---

## 📂 Fichiers créés/modifiés

### Nouveaux fichiers

- `backend/ai.py` → Module LLM
- `.env` → Configuration secrets (GITHUB_TOKEN, MODEL_NAME)

### Fichiers modifiés

- `backend/memory.py` → Ajout support `role`
- `backend/main.py` → Endpoint `/chat` + modèle `ChatMessage`
- `requirements.txt` → Ajout `python-dotenv` et `requests`

---

## 🧪 Exemple de conversation testée

**Question (via POST `/chat`) :**

```json
{ "message": "Comment lister les fichiers dans PowerShell ?" }
```

**Réponse de GPT-4o :**

```json
{
  "reponse": "Pour lister les fichiers dans PowerShell, vous pouvez utiliser la commande **`Get-ChildItem`** ou son alias **`ls`**..."
}
```

**Persistance vérifiée (GET `/messages`) :**

- Message 1 : `role="user"`, texte de la question
- Message 2 : `role="assistant"`, réponse complète de GPT-4o

---

## 🎓 Points d'apprentissage clés

### Ce qui a bien fonctionné

- ✅ L'utilisateur a **écrit 100% du code** de `ai.py` lui-même (guidage pseudo-code)
- ✅ Compréhension rapide de l'analogie "appeler un ami expert"
- ✅ Bonne maîtrise de `try/except` et logique de réessai
- ✅ Tests méthodiques (module seul → endpoint → persistance)

### Difficultés rencontrées

- ⚠️ Première tentative : ajout `message` dans classe `Message` au lieu de créer `ChatMessage`
- ⚠️ Correction rapide appliquée : séparation des 2 modèles Pydantic

### Évolution depuis Session 2

- **Plus autonome** : écrit des fonctions complètes sans aide
- **Meilleure compréhension** des requêtes HTTP (POST, headers, JSON)
- **Réflexes sécurité** : comprend pourquoi `.env` dans `.gitignore`

---

## 🔜 Prochaines étapes (Session 4)

### Améliorations possibles

1. **Contexte conversationnel** : envoyer les N derniers messages au LLM (mémoire)
2. **Streaming** : afficher la réponse mot par mot (SSE ou WebSocket)
3. **Frontend interactif** : interface chat dans `frontend/index.html`
4. **Gestion d'erreurs avancée** : timeout configurable, retry exponentiel
5. **Support multi-modèles** : basculer entre GPT-4o, Claude, Llama

---

## 📖 Documentation associée

- **Guide technique détaillé :** [GUIDE_TECHNIQUE.md](./GUIDE_TECHNIQUE.md)
- **Scripts finaux :** Dossier [scripts/](./scripts/)
- **État final :** [docs/chat_transitions/chat_4_session_3/CURRENT_STATE.md](../../chat_transitions/chat_4_session_3/CURRENT_STATE.md)
