# Guide Technique Session 7 : Dark Mode 🌙

> **Public :** Débutant Python/JavaScript  
> **Prérequis :** Session 6 (UX avancées)  
> **Durée :** 1-2h

---

## 📚 Concepts techniques expliqués

### 1. Variables CSS (`:root` et `var()`)

**Analogie :** Des **boîtes de couleurs** avec des étiquettes.

```css
/* Déclaration des boîtes (variables) */
:root {
  --couleur-fond: #ffffff; /* Boîte "fond" contient blanc */
  --couleur-texte: #000000; /* Boîte "texte" contient noir */
}

/* Utilisation des boîtes */
body {
  background-color: var(--couleur-fond); /* Prendre couleur dans boîte "fond" */
  color: var(--couleur-texte); /* Prendre couleur dans boîte "texte" */
}
```

**Pourquoi c'est utile ?**

- Changer UNE variable = changer TOUTES les utilisations
- Plus facile à maintenir
- Permet le dark mode facilement

---

### 2. Classe `.dark-mode` conditionnelle

**Analogie :** Un **interrupteur** qui change toutes les ampoules.

```css
/* Mode clair (par défaut) */
:root {
  --couleur-fond: #ffffff;
  --couleur-texte: #000000;
}

/* Mode sombre (quand classe .dark-mode sur body) */
.dark-mode {
  --couleur-fond: #1a1a1a; /* Redéfinir variable avec gris foncé */
  --couleur-texte: #ffffff; /* Redéfinir variable avec blanc */
}
```

**Comment ça marche ?**

1. Par défaut : `body` utilise variables de `:root` (mode clair)
2. Si `body` a classe `.dark-mode` : variables redéfinies (mode sombre)
3. Tous les éléments utilisant `var()` changent automatiquement !

---

### 3. localStorage (mémoire du navigateur)

**Analogie :** Un **tiroir secret** dans le navigateur qui garde tes affaires.

```javascript
// SAUVEGARDER une donnée dans le tiroir
localStorage.setItem("theme", "dark"); // Mettre étiquette "theme" avec valeur "dark"

// RÉCUPÉRER une donnée du tiroir
const theme = localStorage.getItem("theme"); // Lire ce qu'il y a sur étiquette "theme"
console.log(theme); // Affiche "dark"

// VÉRIFIER si le tiroir contient quelque chose
if (localStorage.getItem("theme") === "dark") {
  console.log("Mode sombre activé !");
}
```

**Caractéristiques :**

- Données **persistent** même après fermeture navigateur
- Données **locales** à un domaine (ton site uniquement)
- Accepte **uniquement du texte** (pas d'objets directement)

---

### 4. Toggle classe avec JavaScript

**Analogie :** Ajouter/enlever un **badge** sur une personne.

```javascript
// Récupérer l'élément body
const body = document.body;

// VÉRIFIER si body a la classe "dark-mode"
if (body.classList.contains("dark-mode")) {
  console.log("Mode sombre actif");
}

// AJOUTER la classe "dark-mode"
body.classList.add("dark-mode");

// ENLEVER la classe "dark-mode"
body.classList.remove("dark-mode");

// TOGGLE : ajouter si absente, enlever si présente
body.classList.toggle("dark-mode"); // ⭐ Le plus simple !
```

**`.toggle()` en détail :**

- Si classe absente → ajoute
- Si classe présente → enlève
- Parfait pour un interrupteur on/off !

---

### 5. Event listener sur checkbox

**Analogie :** Un **gardien** qui surveille la porte et te prévient quand quelqu'un entre.

```javascript
// Récupérer le switch (checkbox)
const switchElement = document.getElementById("dark-mode-switch");

// Placer un gardien sur le switch
switchElement.addEventListener("change", function () {
  // Cette fonction s'exécute quand on clique sur le switch
  console.log("Switch cliqué !");

  // Vérifier si checkbox cochée
  if (switchElement.checked) {
    console.log("Switch ON");
  } else {
    console.log("Switch OFF");
  }
});
```

**Événement `change` :**

- Se déclenche quand l'état du checkbox change
- ON → OFF ou OFF → ON
- Parfait pour un switch !

---

## 🛠️ Implémentation détaillée

### Étape 1 : Variables CSS dans style.css

**Où ajouter ?** En haut du fichier, avant `* { margin: 0; }`

```css
/* ========================================
   VARIABLES CSS (Mode clair + Mode sombre)
   ======================================== */

/* Mode clair (par défaut) */
:root {
  --couleur-fond: #f5f5f5;
  --couleur-texte: #333333;
  --couleur-header: #ffffff;
  --couleur-user: #007bff;
  --couleur-assistant: #e0e0e0;
  --couleur-input: #ffffff;
  --couleur-bouton: #007bff;
  --couleur-bouton-hover: #0056b3;
  --couleur-clear: #dc3545;
  --couleur-clear-hover: #c82333;
}

/* Mode sombre */
.dark-mode {
  --couleur-fond: #1a1a1a;
  --couleur-texte: #e0e0e0;
  --couleur-header: #2d2d2d;
  --couleur-user: #4a9eff;
  --couleur-assistant: #3a3a3a;
  --couleur-input: #2d2d2d;
  --couleur-bouton: #4a9eff;
  --couleur-bouton-hover: #3d8de0;
  --couleur-clear: #ff4d4d;
  --couleur-clear-hover: #e63939;
}
```

**Ensuite :** Remplacer toutes les couleurs fixes par `var(--nom-variable)`

Exemple :

```css
/* Avant */
body {
  background-color: #f5f5f5;
  color: #333;
}

/* Après */
body {
  background-color: var(--couleur-fond);
  color: var(--couleur-texte);
}
```

---

### Étape 2 : Switch HTML dans index.html

**Où ajouter ?** Dans le header, après le titre, avant le bouton Clear

```html
<!-- Switch Dark Mode -->
<div class="dark-mode-toggle">
  <input type="checkbox" id="dark-mode-switch" />
  <label for="dark-mode-switch">
    <span class="sun">☀️</span>
    <span class="moon">🌙</span>
  </label>
</div>
```

---

### Étape 3 : Styles du switch dans style.css

**Où ajouter ?** Après les styles du header

```css
/* ========================================
   SWITCH DARK MODE
   ======================================== */

.dark-mode-toggle {
  position: relative;
}

.dark-mode-toggle input[type="checkbox"] {
  display: none; /* Cacher le checkbox natif */
}

.dark-mode-toggle label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  font-size: 1.5rem;
  padding: 8px 12px;
  background-color: var(--couleur-input);
  border-radius: 20px;
  transition: background-color 0.3s ease;
}

.dark-mode-toggle label:hover {
  opacity: 0.8;
}

/* Mode clair : montrer soleil, cacher lune */
.dark-mode-toggle .moon {
  display: none;
}

.dark-mode-toggle .sun {
  display: inline;
}

/* Mode sombre : cacher soleil, montrer lune */
.dark-mode .dark-mode-toggle .moon {
  display: inline;
}

.dark-mode .dark-mode-toggle .sun {
  display: none;
}
```

---

### Étape 4 : JavaScript dans app.js

**Où ajouter ?** À la fin du fichier

```javascript
// ========================================
// DARK MODE
// ========================================

// Fonction pour activer/désactiver le mode sombre
function toggleDarkMode() {
  // Toggle classe "dark-mode" sur body
  document.body.classList.toggle("dark-mode");

  // Vérifier si mode sombre activé
  const isDarkMode = document.body.classList.contains("dark-mode");

  // Sauvegarder préférence dans localStorage
  localStorage.setItem("theme", isDarkMode ? "dark" : "light");

  // Mettre à jour état du switch
  document.getElementById("dark-mode-switch").checked = isDarkMode;
}

// Au chargement de la page : vérifier préférence utilisateur
document.addEventListener("DOMContentLoaded", function () {
  const savedTheme = localStorage.getItem("theme");

  // Si utilisateur avait choisi mode sombre
  if (savedTheme === "dark") {
    document.body.classList.add("dark-mode");
    document.getElementById("dark-mode-switch").checked = true;
  }

  // Écouter les clics sur le switch
  document
    .getElementById("dark-mode-switch")
    .addEventListener("change", toggleDarkMode);
});
```

---

## 🧪 Tests à effectuer

### Test 1 : Toggle basique

1. Ouvrir application
2. Cliquer sur switch → Mode sombre s'active
3. Cliquer à nouveau → Mode clair revient

### Test 2 : Persistance

1. Activer mode sombre
2. Recharger page (F5) → Mode sombre toujours actif
3. Désactiver mode sombre
4. Recharger page (F5) → Mode clair

### Test 3 : localStorage DevTools

1. F12 → Onglet Application → Local Storage
2. Vérifier présence clé "theme" avec valeur "dark" ou "light"

### Test 4 : Fermeture navigateur

1. Activer mode sombre
2. Fermer complètement navigateur
3. Rouvrir application → Mode sombre toujours actif

---

## 🎯 Résumé Session 7

**Tu as appris :**

1. ✅ Variables CSS (`:root`, `var()`)
2. ✅ Classes conditionnelles (`.dark-mode`)
3. ✅ localStorage (sauvegarder/récupérer)
4. ✅ Toggle classes JavaScript
5. ✅ Event listeners

**Fichiers modifiés :**

- [style.css](../../../frontend/style.css) : +30 lignes
- [index.html](../../../frontend/index.html) : +15 lignes
- [app.js](../../../frontend/app.js) : +20 lignes

**Résultat :** Application avec mode sombre persistant ! 🌙
