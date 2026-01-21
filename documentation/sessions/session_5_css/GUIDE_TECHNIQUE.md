# Guide Technique — Session 5 : CSS & Design

> **Date :** 2026-01-13  
> **Chat :** 6  
> **Session :** 5 — CSS & Design Moderne  
> **Branche Git :** `feature/session5-css`

---

## 🎯 Objectif de la session

Ajouter un design moderne et professionnel à l'interface de chat avec :

- Layout Flexbox (structure verticale)
- Bulles de messages stylisées (user à droite, assistant à gauche)
- Animations douces (apparition + hover)
- Typographie et couleurs harmonieuses

---

## 📚 Concepts appris

### 1. **Flexbox (CSS)**

**Définition :** Système de layout CSS pour aligner et distribuer des éléments de manière flexible.

**Analogie :** Une bibliothèque intelligente qui organise automatiquement les livres selon des règles.

**Propriétés clés :**

- `display: flex` : Active Flexbox sur le conteneur
- `flex-direction` : Axe principal (`row` = horizontal, `column` = vertical)
- `justify-content` : Alignement le long de l'axe principal
- `align-items` : Alignement perpendiculaire à l'axe principal
- `flex: 1` : Prend tout l'espace disponible
- `gap` : Espace entre les éléments enfants

**Exemple minimal :**

```css
.conteneur {
  display: flex; /* Active Flexbox */
  justify-content: center; /* Centre horizontalement */
  align-items: center; /* Centre verticalement */
}
```

**Dans notre projet :**

- `body` : Flexbox colonne (header → conversation → input)
- `#inputZone` : Flexbox row (input + bouton côte à côte)
- Paragraphes messages : Flexbox row (alignement bulles gauche/droite)

---

### 2. **Animations CSS (@keyframes)**

**Définition :** Créer des transitions visuelles fluides entre plusieurs états.

**Structure :**

```css
@keyframes nomAnimation {
  from {
    /* État initial */
  }
  to {
    /* État final */
  }
}

.element {
  animation: nomAnimation 0.3s ease-out;
}
```

**Dans notre projet :**

```css
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px); /* Décalé vers le bas */
  }
  to {
    opacity: 1;
    transform: translateY(0); /* Position normale */
  }
}
```

**Résultat :** Messages apparaissent en fondu par le bas (durée 0.3s).

---

### 3. **Pseudo-classes CSS (:hover)**

**Définition :** Appliquer des styles quand l'utilisateur survole un élément.

**Exemple :**

```css
.bulle-user:hover {
  transform: scale(1.02); /* Agrandit de 2% */
}
```

**Avec transition :**

```css
.bulle-user {
  transition: transform 0.2s ease; /* Animation douce */
}
```

---

### 4. **DOM JavaScript avancé (createElement + appendChild)**

**Pourquoi ?** Éviter `innerHTML +=` qui régénère tout le HTML et rejoue les animations.

**Pattern :**

```javascript
// Créer éléments
const p = document.createElement("p");
p.className = "message-user";

const span = document.createElement("span");
span.className = "bulle-user";
span.textContent = "Mon message";

// Assembler
p.appendChild(span);
conversation.appendChild(p);
```

**Avantages :**

- ✅ Seul le nouveau message est ajouté (pas de régénération)
- ✅ Animations jouées uniquement sur nouveaux messages
- ✅ Plus performant
- ✅ Plus sécurisé (`textContent` échappe automatiquement le HTML)

---

### 5. **setTimeout() pour délais naturels**

**Définition :** Exécuter une fonction après un délai (millisecondes).

**Syntaxe :**

```javascript
setTimeout(function () {
  // Code à exécuter après le délai
}, 400); // 400ms = 0.4 secondes
```

**Dans notre projet :**

```javascript
// Message user apparaît immédiatement
conversation.appendChild(messageUser);

// Message "est en train d'écrire..." apparaît après 400ms
setTimeout(function () {
  conversation.appendChild(messageChargement);
  // Puis fetch vers backend
}, 400);
```

**Résultat :** Délai naturel avant que l'assistant "réponde".

---

## 🛠️ Implémentation étape par étape

### **Étape 1 : Layout Global (Bloc 1)**

**Objectif :** Structure Flexbox verticale (header → conversation → input).

**Fichier :** `frontend/style.css`

```css
body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  height: 100vh; /* Plein écran */
  display: flex; /* Active Flexbox */
  flex-direction: column; /* Axe vertical */
  background-color: #f5f5f5;
}

h1 {
  background-color: #2c3e50;
  color: white;
  text-align: center;
  padding: 20px 0;
  margin: 0;
}

#conversation {
  flex: 1; /* Prend tout l'espace disponible */
  overflow-y: auto; /* Scroll si trop de messages */
  padding: 20px;
  background-color: #ffffff;
}
```

**Test :** Titre bleu en haut, zone blanche au milieu.

---

### **Étape 2 : Zone Input + Bouton (Bloc 2)**

**Objectif :** Input et bouton côte à côte avec Flexbox horizontal.

```css
#inputZone {
  display: flex;
  flex-direction: row; /* Côte à côte */
  padding: 15px;
  background-color: #e8e8e8;
  gap: 10px; /* Espace entre input et bouton */
}

#messageInput {
  flex: 1; /* Prend tout l'espace disponible */
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 14px;
  outline: none; /* Enlève bordure bleue au focus */
}

#envoyerBtn {
  padding: 12px 24px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  font-weight: bold;
}

#envoyerBtn:hover {
  background-color: #2980b9; /* Bleu plus foncé au survol */
}
```

**Modifications HTML :** Ajouter `id="inputZone"` au div conteneur.

**Test :** Input s'étire, bouton fixe à droite, survol change couleur.

---

### **Étape 3 : Bulles de Messages (Bloc 3)**

**Objectif :** Messages user à droite (bleu), assistant à gauche (gris).

```css
#conversation p {
  display: flex;
  margin: 10px 0;
  animation: fadeIn 0.3s ease-in-out;
}

.message-user {
  justify-content: flex-end; /* Aligne à droite */
}

.message-assistant {
  justify-content: flex-start; /* Aligne à gauche */
}

.bulle-user {
  background-color: #3498db;
  color: white;
  padding: 12px 16px;
  border-radius: 18px;
  max-width: 70%;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
}

.bulle-assistant {
  background-color: #ecf0f1;
  color: #2c3e50;
  padding: 12px 16px;
  border-radius: 18px;
  max-width: 70%;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
}
```

**Modifications JavaScript :**

```javascript
// Au lieu de innerHTML +=
const messageUser = document.createElement("p");
messageUser.className = "message-user";
const bulleUser = document.createElement("span");
bulleUser.className = "bulle-user";
bulleUser.textContent = texte;
messageUser.appendChild(bulleUser);
conversation.appendChild(messageUser);
```

**Test :** Messages apparaissent en bulles (bleu à droite, gris à gauche).

---

### **Étape 4 : Animations (Bloc 4)**

**Objectif :** Apparition douce + effet hover.

```css
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.bulle-user:hover,
.bulle-assistant:hover {
  transform: scale(1.02); /* Agrandit de 2% au survol */
}
```

**Test :**

- Nouveaux messages apparaissent en fondu
- Bulles grossissent légèrement au survol

---

### **Étape 5 : Délai Naturel (setTimeout)**

**Objectif :** Message "est en train d'écrire..." après 400ms.

```javascript
// Message user immédiat
conversation.appendChild(messageUser);
input.value = "";

// Attendre 400ms avant chargement + fetch
setTimeout(function() {
    // Afficher "est en train d'écrire..."
    conversation.appendChild(messageChargement);

    // Envoyer requête backend
    fetch("http://127.0.0.1:8000/chat", { ... });
}, 400);
```

**Test :** Délai naturel entre message user et "est en train d'écrire...".

---

## 📦 Fichiers modifiés

### **Nouveau fichier : `frontend/style.css`**

**Rôle :** Tous les styles CSS du chat.

**Sections :**

1. Layout global (body, h1, #conversation)
2. Zone input + bouton (#inputZone, #messageInput, #envoyerBtn)
3. Bulles de messages (.message-user, .bulle-user, etc.)
4. Animations (@keyframes fadeIn, :hover)

**Taille :** ~120 lignes (commentaires inclus)

---

### **Modifié : `frontend/index.html`**

**Changements :**

1. Ajout `<link rel="stylesheet" href="style.css">` dans `<head>`
2. Suppression `<p>Interface prête</p>` (inutile avec CSS)
3. Ajout `id="inputZone"` au div conteneur input+bouton
4. Ajout commentaires HTML pour structure

---

### **Modifié : `frontend/app.js`**

**Changements :**

1. Remplacement `innerHTML +=` par `createElement()` + `appendChild()`
2. Ajout classes CSS (`.message-user`, `.bulle-user`, etc.)
3. Ajout `setTimeout(400ms)` avant message chargement
4. Ajout commentaires détaillés (en-tête + blocs logiques)

**Lignes modifiées :** ~30 lignes de logique d'affichage

---

## 🧪 Tests

### **Test 1 : Layout Flexbox**

```
✅ Titre bleu en haut colle au bord
✅ Zone conversation blanche prend tout l'espace
✅ Input + bouton en bas gris clair
✅ Input s'étire, bouton taille fixe
```

### **Test 2 : Bulles de messages**

```
✅ Message user = bulle bleue à droite
✅ Message assistant = bulle grise à gauche
✅ Max 70% de largeur d'écran
✅ Ombre légère visible
```

### **Test 3 : Animations**

```
✅ Nouveaux messages apparaissent en fondu (0.3s)
✅ Anciens messages ne rejouent PAS l'animation
✅ Hover sur bulle → agrandissement 2%
✅ Transition fluide (0.2s)
```

### **Test 4 : Délai naturel**

```
✅ Message user apparaît immédiatement
✅ "Est en train d'écrire..." après 400ms
✅ Réponse assistant remplace message chargement
```

### **Test 5 : Bouton hover**

```
✅ Bouton bleu (#3498db) par défaut
✅ Bouton bleu foncé (#2980b9) au survol
✅ Transition douce
```

---

## 🐛 Problèmes rencontrés et solutions

### **Problème 1 : Toutes les bulles rejouent l'animation**

**Cause :** Utilisation de `innerHTML +=` régénère tout le HTML.

**Solution :**

```javascript
// ❌ Avant
conversation.innerHTML += "<p>...</p>";

// ✅ Après
const p = document.createElement("p");
// ...
conversation.appendChild(p);
```

---

### **Problème 2 : Input ne prend pas toute la largeur**

**Cause :** Sélecteur CSS incorrect (`body > div:last-child`).

**Solution :**

1. Ajouter `id="inputZone"` au div
2. Utiliser `#inputZone` en CSS

---

### **Problème 3 : Message chargement instantané (pas naturel)**

**Cause :** Affichage immédiat après message user.

**Solution :**

```javascript
setTimeout(function () {
  // Afficher chargement + fetch
}, 400);
```

---

### **Problème 4 : Erreurs syntaxe CSS**

**Exemples corrigés :**

```css
/* ❌ Erreur */
display; flex;
gap: 10px
.conversation { }

/* ✅ Correct */
display: flex;
gap: 10px;
#conversation { }
```

---

## 📊 Comparaison Avant / Après

| Aspect          | Session 4 (Avant)             | Session 5 (Après)                 |
| --------------- | ----------------------------- | --------------------------------- |
| **Design**      | HTML basique sans style       | Interface moderne professionnelle |
| **Layout**      | Éléments empilés par défaut   | Flexbox structuré                 |
| **Messages**    | Texte plat avec `<strong>`    | Bulles stylisées (bleu/gris)      |
| **Alignement**  | Tous à gauche                 | User droite, assistant gauche     |
| **Animations**  | Aucune                        | Apparition douce + hover          |
| **Performance** | `innerHTML +=` (régénération) | `appendChild()` (optimisé)        |
| **Sécurité**    | `innerHTML` (risque XSS)      | `textContent` (échappement auto)  |

---

## 🎓 Points clés à retenir

1. **Flexbox = Layout moderne simple** : `display: flex` + `flex-direction` + `justify-content`
2. **Animations CSS** : `@keyframes` + `animation` pour effets visuels
3. **`:hover` + `transition`** : Interactions fluides au survol
4. **`createElement()` > `innerHTML`** : Performance + sécurité + contrôle animations
5. **`setTimeout()`** : Créer délais naturels dans interfaces

---

## 🚀 Prochaines étapes possibles

- **Session 6 (Optionnel) :** Auto-scroll vers dernier message
- **Session 7 (Optionnel) :** Dark mode (switch CSS)
- **Session 8 :** Tests automatisés (pytest + Selenium)
- **Session 9 :** Déploiement (Render/HuggingFace)

---

## 📚 Ressources

- [MDN Flexbox Guide](https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Flexible_Box_Layout)
- [MDN Animations CSS](https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Animations)
- [MDN createElement()](https://developer.mozilla.org/fr/docs/Web/API/Document/createElement)
