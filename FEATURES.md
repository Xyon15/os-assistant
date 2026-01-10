# 🚀 Features & Roadmap

> Liste des fonctionnalités futures pour OS Assistant

**Status actuel :** v0.1.0-mvp ✅  
**Date :** 2026-01-10

---

## 📊 Priorités

- 🔴 **Haute** : Améliore significativement l'expérience utilisateur
- 🟡 **Moyenne** : Fonctionnalité utile mais pas critique
- 🟢 **Basse** : Nice-to-have, peut attendre

---

## 🎨 Session 5 — Design & UX (CSS)

**Priorité :** 🔴 Haute  
**Branche :** `feature/session5-css`

### Objectifs

- Ajouter un design moderne et professionnel
- Améliorer la lisibilité de la conversation
- Rendre l'interface plus agréable visuellement

### Fonctionnalités

- [ ] Créer `frontend/style.css`
- [ ] Bulles de chat (comme WhatsApp/Messenger)
  - User : bulles bleues alignées à droite
  - Assistant : bulles grises alignées à gauche
- [ ] Couleurs et typographie
  - Police moderne (ex: Inter, Roboto)
  - Palette de couleurs cohérente
- [ ] Layout avec Flexbox
  - Zone conversation scrollable
  - Input + bouton toujours visibles en bas
- [ ] Animations subtiles
  - Transition apparition messages
  - Hover sur bouton
- [ ] Responsive design (optionnel)
  - Fonctionne bien sur mobile/tablette

### Fichiers à modifier

- `frontend/style.css` (nouveau)
- `frontend/index.html` (ajouter `<link rel="stylesheet" href="style.css">`)

### Estimation

**Temps :** 1-2 heures  
**Difficulté :** 🟢 Facile (CSS pur, pas de logique)

---

## 📜 Chargement de l'historique au démarrage

**Priorité :** 🔴 Haute  
**Branche :** `feature/historique-loading`

### Objectifs

- Afficher les messages précédents quand on ouvre la page
- Permettre de reprendre une conversation

### Fonctionnalités

- [ ] Appeler GET `/messages` au chargement de la page
- [ ] Afficher tous les messages dans `#conversation`
- [ ] Différencier visuellement user vs assistant
- [ ] Limiter le nombre de messages affichés (ex: 50 derniers)
- [ ] Scroll automatique vers le bas après chargement

### Modifications nécessaires

**Frontend (`frontend/app.js`) :**

```javascript
// Au chargement de la page
window.addEventListener("DOMContentLoaded", function () {
  fetch("http://127.0.0.1:8000/messages")
    .then((reponse) => reponse.json())
    .then((donnees) => {
      donnees.messages.forEach((msg) => {
        if (msg.role === "user") {
          conversation.innerHTML +=
            "<p><strong>User:</strong> " + msg.texte + "</p>";
        } else {
          conversation.innerHTML +=
            "<p><strong>Assistant:</strong> " + msg.texte + "</p>";
        }
      });
      conversation.scrollTop = conversation.scrollHeight;
    });
});
```

### Fichiers à modifier

- `frontend/app.js`

### Estimation

**Temps :** 30 minutes  
**Difficulté :** 🟢 Facile

---

## 🗑️ Bouton "Effacer la conversation"

**Priorité :** 🟡 Moyenne  
**Branche :** `feature/clear-button`

### Objectifs

- Permettre de vider la conversation affichée
- (Optionnel) Supprimer aussi les messages en base de données

### Fonctionnalités

- [ ] Ajouter bouton "🗑️ Effacer" dans l'interface
- [ ] Vider `#conversation` au clic
- [ ] Confirmation avant effacement (optionnel)
- [ ] Endpoint DELETE `/messages` dans backend (optionnel)

### Modifications nécessaires

**Frontend (`frontend/index.html`) :**

```html
<button id="clearBtn">🗑️ Effacer</button>
```

**Frontend (`frontend/app.js`) :**

```javascript
const clearBtn = document.getElementById("clearBtn");
clearBtn.addEventListener("click", function () {
  if (confirm("Effacer la conversation ?")) {
    conversation.innerHTML = "";
  }
});
```

**Backend (`backend/main.py`) — Optionnel :**

```python
@app.delete("/messages")
def delete_all_messages():
    connexion = sqlite3.connect("memory.db")
    connexion.execute("DELETE FROM messages")
    connexion.commit()
    connexion.close()
    return {"status": "ok", "message": "Tous les messages ont été supprimés"}
```

### Fichiers à modifier

- `frontend/index.html`
- `frontend/app.js`
- `backend/main.py` (optionnel)

### Estimation

**Temps :** 30 minutes  
**Difficulté :** 🟢 Facile

---

## ⚠️ Gestion d'erreurs améliorée

**Priorité :** 🔴 Haute  
**Branche :** `feature/error-handling`

### Objectifs

- Afficher des messages d'erreur user-friendly
- Gérer les cas où le backend est down
- Gérer les timeouts (LLM trop lent)

### Fonctionnalités

- [ ] Ajouter `.catch()` dans `fetch()` (déjà fait partiellement)
- [ ] Afficher message d'erreur dans la conversation
- [ ] Indicateur visuel si backend inaccessible
- [ ] Retry automatique (optionnel)
- [ ] Timeout après 30 secondes (optionnel)

### Modifications nécessaires

**Frontend (`frontend/app.js`) :**

```javascript
fetch("http://127.0.0.1:8000/chat", {...})
    .then(reponse => {
        if (!reponse.ok) {
            throw new Error("Erreur serveur : " + reponse.status);
        }
        return reponse.json();
    })
    .then(donnees => {
        // Afficher réponse
    })
    .catch(erreur => {
        // Enlever message de chargement
        const messageChargement = document.getElementById("chargement");
        if (messageChargement) {
            messageChargement.remove();
        }
        // Afficher erreur de manière user-friendly
        conversation.innerHTML += "<p><strong>⚠️ Erreur :</strong> Impossible de contacter l'assistant. Vérifiez que le serveur est démarré.</p>";
        console.error("Erreur:", erreur);
    });
```

### Fichiers à modifier

- `frontend/app.js`

### Estimation

**Temps :** 30 minutes  
**Difficulté :** 🟢 Facile

---

## 📜 Auto-scroll automatique

**Priorité :** 🟡 Moyenne  
**Branche :** `feature/auto-scroll`

### Objectifs

- Scroller automatiquement vers le bas quand un nouveau message arrive
- Améliorer l'UX pour conversations longues

### Fonctionnalités

- [ ] Scroll automatique après ajout message user
- [ ] Scroll automatique après ajout message assistant
- [ ] Scroll uniquement si déjà en bas (optionnel)

### Modifications nécessaires

**Frontend (`frontend/app.js`) :**

```javascript
function scrollToBottom() {
  conversation.scrollTop = conversation.scrollHeight;
}

// Appeler après chaque ajout de message
conversation.innerHTML += "...";
scrollToBottom();
```

### Fichiers à modifier

- `frontend/app.js`
- `frontend/style.css` (ajouter `overflow-y: auto` sur `#conversation`)

### Estimation

**Temps :** 15 minutes  
**Difficulté :** 🟢 Très facile

---

## 🔒 Sécurité & Validation

**Priorité :** 🟡 Moyenne  
**Branche :** `feature/security`

### Objectifs

- Sécuriser l'application contre les failles courantes
- Valider les entrées côté frontend et backend

### Fonctionnalités

- [ ] Échapper HTML dans les messages (éviter XSS)
  - Utiliser `textContent` au lieu de `innerHTML`
- [ ] Limiter longueur des messages (ex: 1000 caractères)
- [ ] Rate limiting backend (optionnel)
- [ ] Validation Pydantic stricte
- [ ] Sanitization des entrées

### Modifications nécessaires

**Frontend (`frontend/app.js`) :**

```javascript
// Au lieu de innerHTML, utiliser textContent ou createElement
const messageElement = document.createElement("p");
messageElement.innerHTML = "<strong>User:</strong> ";
const textNode = document.createTextNode(texte); // Échappe automatiquement
messageElement.appendChild(textNode);
conversation.appendChild(messageElement);
```

**Backend (`backend/main.py`) :**

```python
from pydantic import BaseModel, Field

class ChatMessage(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000)
```

### Fichiers à modifier

- `frontend/app.js`
- `backend/main.py`

### Estimation

**Temps :** 1 heure  
**Difficulté :** 🟡 Moyenne

---

## 🎤 Reconnaissance vocale (Speech-to-Text)

**Priorité :** 🟢 Basse  
**Branche :** `feature/speech-to-text`

### Objectifs

- Permettre de dicter les messages au lieu de taper
- Utiliser Web Speech API (navigateur)

### Fonctionnalités

- [ ] Bouton "🎤 Dicter"
- [ ] Reconnaissance vocale avec Web Speech API
- [ ] Remplir automatiquement l'input avec le texte dicté
- [ ] Indicateur visuel pendant l'enregistrement

### Modifications nécessaires

**Frontend (`frontend/index.html`) :**

```html
<button id="voiceBtn">🎤</button>
```

**Frontend (`frontend/app.js`) :**

```javascript
const voiceBtn = document.getElementById("voiceBtn");
const recognition = new webkitSpeechRecognition();

voiceBtn.addEventListener("click", function () {
  recognition.start();
});

recognition.onresult = function (event) {
  const texte = event.results[0][0].transcript;
  input.value = texte;
};
```

### Fichiers à modifier

- `frontend/index.html`
- `frontend/app.js`

### Estimation

**Temps :** 1 heure  
**Difficulté :** 🟡 Moyenne

---

## 🔊 Synthèse vocale (Text-to-Speech)

**Priorité :** 🟢 Basse  
**Branche :** `feature/text-to-speech`

### Objectifs

- Lire à voix haute les réponses de l'assistant
- Utiliser Web Speech API

### Fonctionnalités

- [ ] Bouton "🔊 Lire" à côté de chaque message assistant
- [ ] Synthèse vocale avec Web Speech API
- [ ] Pause/Stop

### Modifications nécessaires

**Frontend (`frontend/app.js`) :**

```javascript
function lireMessage(texte) {
  const utterance = new SpeechSynthesisUtterance(texte);
  utterance.lang = "fr-FR";
  speechSynthesis.speak(utterance);
}
```

### Fichiers à modifier

- `frontend/app.js`

### Estimation

**Temps :** 1 heure  
**Difficulté :** 🟡 Moyenne

---

## 📊 Statistiques & Analytics

**Priorité :** 🟢 Basse  
**Branche :** `feature/analytics`

### Objectifs

- Afficher des statistiques sur l'utilisation
- Dashboard simple

### Fonctionnalités

- [ ] Nombre total de messages
- [ ] Nombre de conversations
- [ ] Messages par jour (graphique)
- [ ] Endpoint GET `/stats` dans backend

### Fichiers à modifier

- `backend/main.py` (nouveau endpoint)
- `frontend/stats.html` (nouvelle page)

### Estimation

**Temps :** 2-3 heures  
**Difficulté :** 🟡 Moyenne

---

## 🌐 Déploiement

**Priorité :** 🟡 Moyenne (quand MVP stable)  
**Branche :** `feature/deployment`

### Objectifs

- Déployer l'application en ligne
- Accessible depuis n'importe où

### Options

- **Backend :** Render, Railway, Heroku
- **Frontend :** GitHub Pages, Netlify, Vercel
- **Base de données :** PostgreSQL (au lieu de SQLite)

### Étapes

- [ ] Créer Procfile pour Render/Heroku
- [ ] Configurer variables d'environnement en production
- [ ] Remplacer SQLite par PostgreSQL
- [ ] Déployer backend
- [ ] Déployer frontend
- [ ] Configurer CORS pour domaine de production

### Estimation

**Temps :** 2-4 heures  
**Difficulté :** 🔴 Difficile (nouveau concept)

---

## 📝 Notes & Idées diverses

### Futures explorations

- [ ] Mode sombre / clair
- [ ] Choix du modèle LLM (GPT-4, Claude, Llama)
- [ ] Contexte système personnalisable
- [ ] Export conversation en PDF/TXT
- [ ] Recherche dans l'historique
- [ ] Tags/catégories pour les conversations
- [ ] Multi-utilisateurs (authentification)
- [ ] Notifications desktop
- [ ] PWA (Progressive Web App)

### Optimisations

- [ ] Cache des réponses LLM
- [ ] Compression des messages longs
- [ ] Pagination de l'historique (au lieu de tout charger)
- [ ] WebSocket pour temps réel (au lieu de polling)

---

## 🎯 Roadmap suggérée

### Phase 1 — Améliorations essentielles (v0.2.0)

1. ✅ Session 5 — CSS & Design
2. ✅ Chargement historique au démarrage
3. ✅ Gestion erreurs améliorée
4. ✅ Auto-scroll

**Estimation :** 3-4 heures  
**Résultat :** Application beaucoup plus agréable à utiliser

### Phase 2 — Fonctionnalités avancées (v0.3.0)

1. ✅ Bouton "Effacer"
2. ✅ Sécurité & Validation
3. ✅ Reconnaissance vocale (optionnel)

**Estimation :** 3-4 heures  
**Résultat :** Application plus robuste et polyvalente

### Phase 3 — Déploiement (v1.0.0)

1. ✅ Déploiement en ligne
2. ✅ PostgreSQL (au lieu de SQLite)
3. ✅ Configuration production

**Estimation :** 4-6 heures  
**Résultat :** Application accessible publiquement

---

## ✅ Checklist pour chaque feature

```
□ Créer branche feature/nom-feature
□ Implémenter la fonctionnalité
□ Tester localement
□ Documenter (README, GUIDE_TECHNIQUE si nécessaire)
□ Committer avec message Conventional Commits
□ Pousser vers GitHub
□ Fusionner dans main
□ Supprimer la branche
□ Mettre à jour ce fichier (cocher ✅)
```

---

## 📚 Ressources utiles

- [MDN - Web Speech API](https://developer.mozilla.org/fr/docs/Web/API/Web_Speech_API)
- [CSS Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [GitHub Pages](https://pages.github.com/)

---

_Dernière mise à jour : 2026-01-10_
