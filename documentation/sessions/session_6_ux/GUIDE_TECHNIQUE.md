# Guide Technique — Session 6 : Améliorations UX

> **Date :** 2026-01-14  
> **Niveau :** Débutant (explications simples)  
> **Durée lecture :** ~15 min

---

## 📖 Table des matières

1. [Auto-scroll automatique](#1-auto-scroll-automatique)
2. [Gestion des erreurs](#2-gestion-des-erreurs)
3. [Bouton Clear conversation](#3-bouton-clear-conversation)
4. [Désactivation bouton pendant traitement](#4-désactivation-bouton-pendant-traitement)
5. [Récapitulatif technique](#5-récapitulatif-technique)

---

## 1. Auto-scroll automatique

### 🎯 Problème

Quand tu envoies beaucoup de messages, les nouveaux messages apparaissent **hors de l'écran**. Tu dois scroller manuellement pour les voir.

### 💡 Solution

Utiliser `scrollTop` et `scrollHeight` pour descendre automatiquement vers le bas.

### 📝 Explication simple

Imagine un **ascenseur dans un immeuble** :

- `scrollTop` = **étage actuel** de l'ascenseur (0 = rez-de-chaussée)
- `scrollHeight` = **nombre total d'étages** dans l'immeuble
- Si tu fais `scrollTop = scrollHeight`, l'ascenseur monte **tout en haut** !

Pour une page web qui scroll vers le bas : `scrollTop = scrollHeight` → Va tout en bas.

### ⚙️ Code JavaScript

```javascript
// Après avoir ajouté un message au DOM
conversation.scrollTop = conversation.scrollHeight;
```

**Où l'ajouter ?** (3 endroits)

1. Après message user
2. Après message chargement
3. Après réponse assistant (+ dans `.catch()` pour erreurs)

### 🧪 Test

Envoie 10+ messages. **Résultat :** Le dernier message est toujours visible automatiquement.

---

## 2. Gestion des erreurs

### 🎯 Problème

Si tu arrêtes le backend (uvicorn) et envoies un message, le message "est en train d'écrire..." reste affiché **indéfiniment**. L'utilisateur ne sait pas ce qui se passe.

### 💡 Solution

Ajouter `.catch()` après `fetch()` pour attraper les erreurs et afficher un message poli.

### 📝 Explication simple

**Analogie :** Commander une pizza par téléphone

- **Plan A** (`.then()`) : Le restaurant répond, tu commandes, la pizza arrive → Tout va bien ✅
- **Plan B** (`.catch()`) : Personne ne répond, ou le restaurant dit "on ne livre plus" → Il y a un problème ⚠️

En JavaScript, si `fetch()` échoue (backend arrêté, erreur réseau), le code saute directement dans le `.catch()`.

### ⚙️ Code JavaScript

```javascript
fetch("http://127.0.0.1:8000/chat", { ... })
.then(reponse => reponse.json())
.then(donnees => {
    // Plan A : Tout va bien
    // Afficher réponse assistant
})
.catch(erreur => {
    // Plan B : Il y a un problème
    // 1. Supprimer message chargement
    const messageChargement = document.getElementById("chargement");
    if (messageChargement) {
        messageChargement.remove();
    }

    // 2. Afficher message d'erreur poli
    const messageErreur = document.createElement("p");
    messageErreur.className = "message-error";
    const bulleErreur = document.createElement("span");
    bulleErreur.className = "bulle-error";
    bulleErreur.textContent = "⚠️ Désolé, une erreur est survenue. Vérifie que le serveur est démarré et réessaye.";
    messageErreur.appendChild(bulleErreur);
    conversation.appendChild(messageErreur);

    // 3. Scroller vers message d'erreur
    conversation.scrollTop = conversation.scrollHeight;

    // 4. Logger erreur pour développeur
    console.error("Erreur:", erreur);
});
```

### 🎨 Code CSS

```css
/* Message d'erreur centré */
.message-error {
  justify-content: center;
}

/* Bulle rouge pour erreur */
.bulle-error {
  background-color: #e74c3c; /* Rouge */
  color: white;
  padding: 12px 16px;
  border-radius: 18px;
  max-width: 80%;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
  text-align: center;
  font-weight: bold;
}
```

### 🧪 Test

1. Arrête le backend (Ctrl+C dans terminal uvicorn)
2. Envoie un message dans l'interface
3. **Résultat :** Message d'erreur rouge centré avec icône ⚠️

---

## 3. Bouton Clear conversation

### 🎯 Problème

Pour vider la conversation, tu dois recharger la page (F5). Pas pratique !

### 💡 Solution

Ajouter un bouton "🗑️ Effacer conversation" dans le header qui vide tout en 1 clic.

### 📝 Explication simple

**Analogie :** Tableau noir avec plein de messages

Le bouton Clear, c'est comme une **grosse éponge** qui efface tout le tableau ! 🧽

En JavaScript : `innerHTML = ""` → Vide tout le contenu d'un élément.

### ⚙️ Code HTML

**Avant (Session 5) :**

```html
<h1>Assistant IA</h1>
```

**Après (Session 6) :**

```html
<header id="headerBar">
  <h1>Assistant IA</h1>
  <button id="clearBtn">🗑️ Effacer conversation</button>
</header>
```

### ⚙️ Code JavaScript

```javascript
// Récupérer élément bouton Clear
const clearBtn = document.getElementById("clearBtn");

// Fonction pour vider conversation
function effacerConversation() {
  conversation.innerHTML = ""; // Vide tout le contenu
}

// Event listener sur bouton Clear
clearBtn.addEventListener("click", effacerConversation);
```

### 🎨 Code CSS

```css
/* Header avec Flexbox horizontal */
#headerBar {
  display: flex;
  justify-content: space-between; /* Titre à gauche, bouton à droite */
  align-items: center; /* Aligner verticalement au centre */
  padding: 20px;
  background-color: #2c3e50;
}

/* Titre centré qui prend l'espace disponible */
#headerBar h1 {
  color: white;
  margin: 0;
  flex: 1; /* Prend tout l'espace disponible */
  text-align: center;
}

/* Bouton Clear rouge */
#clearBtn {
  padding: 10px 20px;
  background-color: #e74c3c; /* Rouge */
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  font-weight: bold;
}

/* Hover : rouge plus foncé */
#clearBtn:hover {
  background-color: #c0392b;
}
```

### 🧪 Test

1. Envoie 3-4 messages
2. Clique sur "🗑️ Effacer conversation"
3. **Résultat :** Tous les messages disparaissent !

---

## 4. Désactivation bouton pendant traitement

### 🎯 Problème

Si tu cliques très vite plusieurs fois sur "Envoyer", tu peux envoyer **plusieurs messages simultanément**. Pas idéal !

### 💡 Solution

Désactiver le bouton "Envoyer" pendant que l'assistant réfléchit, puis le réactiver quand la réponse arrive (ou en cas d'erreur).

### 📝 Explication simple

**Analogie :** Ascenseur en maintenance

Imagine un **ascenseur en panne** : le bouton est **grisé** et ne répond plus jusqu'à ce que la réparation soit terminée. C'est exactement ce qu'on veut avec le bouton "Envoyer" !

En JavaScript :

- `button.disabled = true;` → Bouton grisé, non cliquable
- `button.disabled = false;` → Bouton actif, cliquable

### ⚙️ Code JavaScript

**Endroit 1 : Désactiver (après message user)**

```javascript
// Désactiver bouton
bouton.disabled = true;
bouton.textContent = "..."; // Changer texte pour feedback visuel
```

**Endroit 2 : Réactiver (après réponse assistant)**

```javascript
// Réactiver bouton
bouton.disabled = false;
bouton.textContent = "Envoyer"; // Remettre texte original
```

**Endroit 3 : Réactiver (en cas d'erreur)**

```javascript
.catch(erreur => {
    // ... (afficher message erreur)

    // Réactiver bouton
    bouton.disabled = false;
    bouton.textContent = "Envoyer";
});
```

### 🎨 Code CSS

```css
/* Style pour bouton désactivé */
#envoyerBtn:disabled {
  opacity: 0.5; /* Semi-transparent */
  cursor: not-allowed; /* Curseur interdit */
  background-color: #95a5a6; /* Gris neutre */
}
```

### 🧪 Test

1. Envoie un message
2. Essaie de cliquer rapidement 2x sur "Envoyer" pendant que l'assistant réfléchit
3. **Résultat :** Le bouton est gris et ne répond pas → 1 seul message envoyé

---

## 5. Récapitulatif technique

### 📊 Propriétés JavaScript apprises

| Propriété             | Type     | Description                          |
| --------------------- | -------- | ------------------------------------ |
| `scrollTop`           | Number   | Position actuelle du scroll (pixels) |
| `scrollHeight`        | Number   | Hauteur totale du contenu (pixels)   |
| `innerHTML`           | String   | Contenu HTML d'un élément            |
| `disabled`            | Boolean  | Activer/désactiver un bouton         |
| `textContent`         | String   | Texte d'un élément (sans HTML)       |
| `.catch(erreur => …)` | Function | Attraper erreurs Promesses (fetch)   |

### 📊 Pseudo-classes CSS apprises

| Pseudo-classe | Description                                          |
| ------------- | ---------------------------------------------------- |
| `:hover`      | Style appliqué quand souris survole élément          |
| `:disabled`   | Style appliqé quand élément est désactivé (disabled) |

### 📊 Flexbox avancé

| Propriété         | Valeur          | Description                                       |
| ----------------- | --------------- | ------------------------------------------------- |
| `justify-content` | `space-between` | Espacer éléments (1er à gauche, dernier à droite) |
| `flex`            | `1`             | Élément prend tout l'espace disponible            |
| `align-items`     | `center`        | Aligner verticalement au centre                   |

### 📊 Pattern "Désactiver → Traiter → Réactiver"

```
1. Désactiver bouton (disabled = true)
2. Changer texte ("...")
3. Traiter requête (fetch)
4a. Si succès → Réactiver bouton (disabled = false)
4b. Si erreur → Réactiver bouton (disabled = false)
```

**⚠️ Important :** Toujours réactiver dans `.then()` **ET** `.catch()` !

---

## 🎯 Points clés à retenir

### ✅ Auto-scroll

- Pattern : `element.scrollTop = element.scrollHeight;`
- À faire **après chaque ajout** au DOM

### ✅ Gestion erreurs

- **Toujours** ajouter `.catch()` après `fetch()`
- Message utilisateur poli + `console.error()` pour développeur

### ✅ Bouton Clear

- `innerHTML = ""` vide tout le contenu
- Placer dans header pour visibilité

### ✅ Désactivation bouton

- Pattern : Désactiver → Traiter → Réactiver
- Ne pas oublier de réactiver dans `.catch()` !

---

## 🚀 Exercices (optionnel)

### Exercice 1 : Auto-scroll manuel

Crée un bouton "↓ Scroll bas" qui descend en bas de la conversation quand tu cliques dessus.

### Exercice 2 : Message d'erreur personnalisé

Modifie le message d'erreur pour afficher l'erreur technique dans la console ET un message différent selon le type d'erreur.

### Exercice 3 : Confirmation Clear

Ajoute une confirmation `confirm()` avant de vider la conversation : "Es-tu sûr de vouloir tout effacer ?"

### Exercice 4 : Compteur messages

Affiche un compteur dans le header : "5 messages" qui s'incrémente/décrémente automatiquement.

---

## 📚 Ressources

### Documentation officielle

- [MDN - Element.scrollTop](https://developer.mozilla.org/fr/docs/Web/API/Element/scrollTop)
- [MDN - Promise.catch()](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)
- [MDN - disabled (HTML)](https://developer.mozilla.org/fr/docs/Web/HTML/Attributes/disabled)
- [MDN - :disabled (CSS)](https://developer.mozilla.org/fr/docs/Web/CSS/:disabled)

### Tutoriels

- [JavaScript.info - Promises, async/await](https://javascript.info/async)
- [CSS-Tricks - Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

---

**Guide technique Session 6 terminé ! Tu maîtrises maintenant les bases de l'UX frontend ! 🎉**
