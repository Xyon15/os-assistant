# État actuel — Fin de Session 4

> **Date :** 2026-01-09  
> **Chat :** 5  
> **Session :** 4 — Frontend Interactif

---

## 🎯 Ce qui a été accompli

### ✅ Concepts appris

- **`fetch()` en JavaScript** : Envoyer requêtes HTTP depuis le navigateur (équivalent `requests.post()`)
- **`addEventListener()`** : Écouter événements (clic, touche clavier)
- **`innerHTML`** : Modifier dynamiquement le contenu HTML
- **Promesses JavaScript** : `.then()` pour traiter réponses asynchrones
- **CORS (Cross-Origin Resource Sharing)** : Sécurité navigateur et configuration FastAPI
- **Séparation HTML / JS** : Bonnes pratiques (fichiers externes)
- **Gestion événements** : Clic bouton + touche Entrée

### ✅ Code écrit

#### **Nouveau fichier : `frontend/index.html`**

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Assistant IA</title>
  </head>
  <body>
    <h1>Assistant IA</h1>
    <p>Interface prête</p>
    <div id="conversation"></div>

    <div>
      <input
        id="messageInput"
        type="text"
        placeholder="Tapez votre message ici..."
      />
      <button id="envoyerBtn">Envoyer</button>
    </div>

    <script src="app.js"></script>
  </body>
</html>
```

**Structure :**

- `<div id="conversation">` : Zone d'affichage des messages
- `<input id="messageInput">` : Zone de saisie
- `<button id="envoyerBtn">` : Bouton d'envoi
- `<script src="app.js">` : Charge le JavaScript externe

#### **Nouveau fichier : `frontend/app.js`**

```javascript
// 1. Récupérer les éléments HTML
const bouton = document.getElementById("envoyerBtn");
const input = document.getElementById("messageInput");
const conversation = document.getElementById("conversation");

// 2. Fonction pour envoyer le message
function envoyerMessage() {
  const texte = input.value.trim();

  if (texte === "") {
    return;
  }

  // Afficher message user
  conversation.innerHTML += "<p><strong>User:</strong> " + texte + "</p>";

  // Afficher indicateur chargement
  conversation.innerHTML +=
    "<p id='chargement'><em>Assistant est en train d'écrire...</em></p>";

  input.value = "";

  // Envoyer au backend
  fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: texte }),
  })
    .then((reponse) => reponse.json())
    .then((donnees) => {
      // Enlever message chargement
      const messageChargement = document.getElementById("chargement");
      if (messageChargement) {
        messageChargement.remove();
      }

      // Afficher réponse assistant
      conversation.innerHTML +=
        "<p><strong>Assistant:</strong> " + donnees.reponse + "</p>";
    });
}

// 3. Écouter clic bouton
bouton.addEventListener("click", envoyerMessage);

// 4. Écouter touche Entrée
input.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    envoyerMessage();
  }
});
```

**Fonctionnalités :**

- Récupération éléments HTML avec `getElementById()`
- Fonction `envoyerMessage()` : validation, affichage, fetch, traitement réponse
- Événement clic sur bouton
- Événement touche Entrée dans input
- Message de chargement avec ID unique pour suppression

#### **Modifications : `backend/main.py`**

**Ajout import CORS (ligne 15) :**

```python
from fastapi.middleware.cors import CORSMiddleware
```

**Ajout middleware CORS (après ligne 29) :**

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autoriser toutes origines (dev local)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**Pourquoi nécessaire ?**

- Navigateur effectue requête OPTIONS (pre-flight) avant POST
- Sans CORS, erreur `Access to fetch ... has been blocked by CORS policy`
- `allow_origins=["*"]` autorise toutes origines (`file://`, `localhost`, etc.)

---

## 🧪 Tests réussis

### **Test 1 : Envoyer message avec bouton** ✅

**Commandes :**

1. Double-clic sur `frontend/index.html` (ouvrir sans Live Server)
2. Taper "Bonjour"
3. Cliquer "Envoyer"

**Résultat :**

- `User: Bonjour` affiché immédiatement
- `Assistant est en train d'écrire...` apparaît
- Après ~2-3 secondes : message chargement disparaît
- `Assistant: Bonjour ! Comment puis-je vous aider ?` affiché

### **Test 2 : Envoyer message avec Entrée** ✅

**Commandes :**

1. Taper "Ça va ?"
2. Appuyer sur touche Entrée (pas de clic)

**Résultat :**

- Message envoyé sans cliquer sur bouton ✅

### **Test 3 : Plusieurs messages successifs** ✅

**Commandes :**

1. Envoyer "Bonjour"
2. Envoyer "Quelle heure est-il ?"
3. Envoyer "Merci"

**Résultat :**

- Conversation s'affiche correctement avec tous les messages
- Ordre préservé (user, assistant, user, assistant...)

### **Test 4 : Message vide** ✅

**Commandes :**

1. Laisser input vide
2. Cliquer "Envoyer"

**Résultat :**

- Rien ne se passe (validation `if (texte === "")` fonctionne) ✅

---

## 🐛 Problèmes rencontrés et solutions

### **Problème 1 : Page se recharge au clic**

**Symptômes :**

- Message "User: Bonjour" apparaît brièvement puis disparaît
- Page se recharge complètement

**Cause :**

- Live Server rechargeait automatiquement la page
- Comportement de formulaire HTML implicite (input + bouton = formulaire)

**Solutions testées :**

1. ❌ `event.preventDefault()` dans JavaScript → Inefficace
2. ❌ `<form onsubmit="return false;">` → Inefficace avec Live Server
3. ❌ Supprimer `<form>`, utiliser `<div>` → Inefficace avec Live Server
4. ✅ **Ouvrir `index.html` directement (sans Live Server)** → FONCTIONNE

**Solution finale :**

- Double-clic sur `frontend/index.html` pour ouvrir dans navigateur
- Ne PAS utiliser Live Server pour cette application

### **Problème 2 : Erreur 405 Method Not Allowed (OPTIONS)**

**Symptômes :**

```
INFO: 127.0.0.1:28872 - "OPTIONS /chat HTTP/1.1" 405 Method Not Allowed
```

**Cause :**

- Navigateur envoie requête OPTIONS (pre-flight) avant POST
- FastAPI ne sait pas gérer OPTIONS sans middleware CORS

**Solution :**

- Ajouter middleware CORS dans `backend/main.py`
- Résultat : Requête OPTIONS retourne `200 OK` au lieu de `405`

### **Problème 3 : ERR_CONNECTION_REFUSED**

**Symptômes :**

```
Failed to load resource: net::ERR_CONNECTION_REFUSED
```

**Cause :**

- Backend uvicorn arrêté ou non accessible

**Solution :**

- Relancer `uvicorn backend.main:app --reload` dans terminal
- Vérifier dans terminal : `INFO: Uvicorn running on http://127.0.0.1:8000`

---

## 📊 Architecture complète actuelle

```
┌─────────────────────────────────────────────────────────────┐
│  NAVIGATEUR (frontend)                                       │
│  ┌────────────────┐         ┌──────────────────┐           │
│  │  index.html    │  ←────  │     app.js       │           │
│  │  (structure)   │         │  (logique)       │           │
│  └────────────────┘         └──────────────────┘           │
│         │                            │                       │
│         └────────────────┬───────────┘                       │
│                          │ fetch() POST /chat                │
└──────────────────────────┼───────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│  BACKEND FASTAPI (backend/main.py)                           │
│  ┌──────────────┐     ┌──────────────┐     ┌─────────────┐ │
│  │ CORS         │ →   │  POST /chat  │ →   │  memory.py  │ │
│  │ Middleware   │     │  endpoint    │     │  (SQLite)   │ │
│  └──────────────┘     └──────────────┘     └─────────────┘ │
│                              │                               │
│                              ▼                               │
│                       ┌──────────────┐                       │
│                       │    ai.py     │                       │
│                       │ demander_llm │                       │
│                       └──────────────┘                       │
└───────────────────────────┼──────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│  API GITHUB MODELS (GPT-4o)                                  │
│  https://models.inference.ai.azure.com/chat/completions      │
└──────────────────────────────────────────────────────────────┘
```

**Flux complet d'un message :**

1. Utilisateur tape "Bonjour" et clique Envoyer
2. JavaScript (`app.js`) appelle `envoyerMessage()`
3. `fetch()` envoie POST à `http://127.0.0.1:8000/chat`
4. FastAPI reçoit, valide avec Pydantic (`ChatMessage`)
5. Appelle `demander_llm("Bonjour")` dans `ai.py`
6. `ai.py` envoie requête à GitHub Models API (GPT-4o)
7. GPT-4o retourne réponse
8. FastAPI sauvegarde user + assistant dans SQLite
9. FastAPI retourne `{"reponse": "..."}` au frontend
10. JavaScript affiche la réponse dans la conversation

---

## 📁 Structure actuelle du projet

```
os-assistant/
├── backend/
│   ├── ai.py              ← Session 3 (LLM API)
│   ├── main.py            ← Session 0-4 (endpoints + CORS)
│   ├── memory.py          ← Session 2 (SQLite)
│   └── __pycache__/
├── frontend/              ← ✨ NOUVEAU Session 4
│   ├── index.html         ← Structure HTML
│   └── app.js             ← Logique JavaScript
├── docs/
│   ├── INDEX.md
│   ├── README.md
│   ├── chat_transitions/
│   │   ├── chat_1_session_0/
│   │   ├── chat_2_session_1/
│   │   ├── chat_3_session_2/
│   │   ├── chat_4_session_3/
│   │   └── chat_5_session_4/  ← ✨ NOUVEAU
│   │       └── CURRENT_STATE.md (ce fichier)
│   └── sessions/
│       ├── session_0_setup/
│       ├── session_1_pydantic/
│       ├── session_2_sqlite/
│       ├── session_3_llm/
│       └── session_4_frontend/  ← ✨ NOUVEAU
│           ├── README.md
│           ├── GUIDE_TECHNIQUE.md
│           └── scripts/
│               ├── index.html
│               ├── app.js
│               └── main.py
├── .env                   ← Secrets (GITHUB_TOKEN)
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🎓 Apprentissages clés Session 4

### **1. JavaScript dans le navigateur**

- Pas besoin d'installer Node.js ou packages
- Fichier `.js` chargé avec `<script src="app.js">`
- Code s'exécute après chargement du HTML

### **2. `fetch()` est asynchrone**

- Le code continue pendant que la requête est en cours
- `.then()` = "quand tu auras la réponse, fais ceci"
- Différent du code synchrone Python

### **3. CORS est une sécurité du navigateur**

- Empêche sites malveillants d'accéder à tes APIs
- Obligatoire dès que frontend et backend sont sur origines différentes
- En dev : `allow_origins=["*"]`
- En prod : `allow_origins=["https://mon-site.com"]`

### **4. Live Server peut interférer**

- Rechargement automatique = comportement non souhaité ici
- Mieux : ouvrir fichier directement (`file://`) pour tester

### **5. `innerHTML` modifie le DOM**

- `+=` ajoute sans effacer (`append`)
- `=` remplace tout le contenu
- Attention : peut créer failles XSS si contenu non sécurisé

---

## 🚀 Prochaines étapes possibles (Session 5 — Optionnel)

### **Améliorations UX :**

- Ajouter CSS (bulles de chat, couleurs, Flexbox)
- Auto-scroll vers le bas automatiquement
- Désactiver bouton pendant envoi (éviter double-clic)
- Afficher erreur si backend down

### **Fonctionnalités :**

- Charger historique au démarrage (GET `/messages`)
- Bouton "Effacer conversation"
- Indicateur "en ligne" / "hors ligne" pour backend

### **Sécurité :**

- Échapper contenu HTML (éviter XSS)
- Limiter longueur des messages
- Rate limiting côté backend

---

## 📚 Ressources utilisées

- [MDN - fetch() API](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API)
- [MDN - addEventListener()](https://developer.mozilla.org/fr/docs/Web/API/EventTarget/addEventListener)
- [MDN - innerHTML](https://developer.mozilla.org/fr/docs/Web/API/Element/innerHTML)
- [FastAPI - CORS](https://fastapi.tiangolo.com/tutorial/cors/)
- [JavaScript Promises](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Promise)

---

## ✅ Status final

**Session 4 : TERMINÉE avec succès** ✅

**Fonctionnalités opérationnelles :**

- ✅ Frontend HTML/JavaScript fonctionnel
- ✅ Communication frontend ↔ backend
- ✅ Envoi messages (bouton + Entrée)
- ✅ Affichage conversation en temps réel
- ✅ Message de chargement pendant réflexion LLM
- ✅ CORS configuré correctement
- ✅ Aucun rechargement de page (quand ouvert directement)

**Prêt pour Session 5 (CSS) ou considérer projet MVP complet !** 🎉
