# Session 4 — Frontend Interactif

> **Date :** 2026-01-09  
> **Chat :** 5  
> **Durée :** ~2h  
> **Objectif :** Créer une interface web interactive pour communiquer avec le backend

---

## 🎯 Objectifs de la session

- ✅ Comprendre `fetch()` en JavaScript (équivalent de `requests.post()`)
- ✅ Créer une interface HTML simple (input + bouton + zone conversation)
- ✅ Gérer les événements (clic, touche Entrée)
- ✅ Afficher les messages en temps réel
- ✅ Corriger problème CORS avec FastAPI
- ✅ Résoudre problème de rechargement de page

---

## 📚 Concepts appris

### **1. `fetch()` en JavaScript**

```javascript
fetch("http://127.0.0.1:8000/chat", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ message: "Bonjour" }),
})
  .then((reponse) => reponse.json())
  .then((donnees) => {
    console.log(donnees.reponse);
  });
```

**Analogie :** Comme `requests.post()` en Python, mais dans le navigateur !

### **2. `addEventListener()` — Écouter les événements**

```javascript
// Écouter le clic sur un bouton
bouton.addEventListener("click", maFonction);

// Écouter la touche Entrée
input.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    maFonction();
  }
});
```

### **3. `innerHTML` — Modifier le contenu HTML**

```javascript
// Ajouter du contenu
conversation.innerHTML += "<p>Nouveau message</p>";

// Remplacer tout le contenu
conversation.innerHTML = "<p>Effacé et remplacé</p>";
```

### **4. CORS (Cross-Origin Resource Sharing)**

**Problème :** Le navigateur bloque les requêtes vers le backend par défaut.

**Solution :** Ajouter le middleware CORS dans FastAPI :

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autoriser toutes les origines (dev seulement)
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### **5. Problème de rechargement de page**

**Cause :** Live Server rechargeait automatiquement la page.

**Solution :** Ouvrir `index.html` directement (double-clic) sans Live Server.

---

## 🗂️ Fichiers créés/modifiés

### **Nouveaux fichiers**

- `frontend/index.html` : Structure HTML de l'interface
- `frontend/app.js` : Logique JavaScript (fetch, événements)

### **Fichiers modifiés**

- `backend/main.py` : Ajout middleware CORS

---

## 🧪 Tests effectués

### **Test 1 : Envoyer un message avec le bouton** ✅

1. Ouvrir `frontend/index.html` (double-clic)
2. Taper "Bonjour"
3. Cliquer "Envoyer"
4. Résultat : Message affiché + réponse GPT-4o

### **Test 2 : Envoyer un message avec touche Entrée** ✅

1. Taper "Ça va ?"
2. Appuyer sur Entrée
3. Résultat : Envoyé sans cliquer sur le bouton

### **Test 3 : Message de chargement** ✅

1. Envoyer un message
2. Observer "Assistant est en train d'écrire..."
3. Résultat : Message apparaît puis disparaît quand la réponse arrive

### **Test 4 : Plusieurs messages successifs** ✅

1. Envoyer 3 messages d'affilée
2. Résultat : Conversation s'affiche correctement

---

## 📊 Résultat final

**Fonctionnalités :**

- ✅ Interface chat complète
- ✅ Envoi avec bouton ou Entrée
- ✅ Message de chargement pendant réflexion LLM
- ✅ Communication frontend ↔ backend ↔ LLM opérationnelle

**Architecture complète :**

```
Navigateur (frontend/index.html + app.js)
    ↓ fetch() POST /chat
Backend FastAPI (backend/main.py)
    ↓ demander_llm()
API GitHub Models (GPT-4o)
    ↓ réponse
Backend → Frontend → Affichage
```

---

## 🎓 Apprentissages clés

**1. JavaScript dans le navigateur ≠ JavaScript Node.js**

- Pas besoin d'installer de packages
- Fonctionne directement dans le HTML avec `<script>`

**2. `fetch()` retourne une promesse**

- `.then()` = "quand tu auras la réponse, fais ceci"
- Comme `async/await` mais syntaxe différente

**3. CORS est une sécurité du navigateur**

- Empêche les sites malveillants d'accéder à tes APIs
- En dev local, on autorise tout (`allow_origins=["*"]`)
- En production, on spécifie l'URL exacte du frontend

**4. Live Server peut causer des problèmes**

- Rechargement automatique interfère avec JavaScript
- Pour tester, ouvrir le fichier directement (`file://`)

---

## 📝 Prochaine étape (Session 5 — Optionnel)

**Améliorations possibles :**

- Ajouter du CSS pour un design moderne
- Afficher l'historique des messages au chargement (GET /messages)
- Ajouter auto-scroll automatique vers le bas
- Afficher les erreurs de manière plus jolie

---

## 📚 Ressources

- [MDN - fetch()](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API)
- [MDN - addEventListener()](https://developer.mozilla.org/fr/docs/Web/API/EventTarget/addEventListener)
- [FastAPI - CORS](https://fastapi.tiangolo.com/tutorial/cors/)
