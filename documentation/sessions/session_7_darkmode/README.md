# Session 7 : Dark Mode 🌙

> **Date :** 2026-01-15  
> **Chat :** Chat 8  
> **Objectif :** Ajouter un mode sombre avec switch + localStorage

---

## 🎯 Objectifs

1. ✅ Créer variables CSS réutilisables
2. ✅ Ajouter classe `.dark-mode` avec couleurs sombres
3. ✅ Intégrer switch dans le header
4. ✅ Coder fonction `toggleDarkMode()` en JavaScript
5. ✅ Sauvegarder préférence utilisateur avec localStorage
6. ✅ Tester persistance du mode sombre

---

## 📚 Concepts enseignés

- **Variables CSS** (`:root`, `--nom-variable`, `var()`)
- **Classes conditionnelles** (`.dark-mode` appliquée sur `<body>`)
- **localStorage** (`setItem()`, `getItem()`, persistance navigateur)
- **Toggle JavaScript** (ajouter/enlever classe avec `classList.toggle()`)
- **Event listeners** (clic sur switch)

---

## 🛠️ Modifications apportées

### 1. Variables CSS ([style.css](../../../frontend/style.css))

**Lignes ajoutées :** ~30 lignes

- Déclaration `:root` avec variables pour mode clair
- Classe `.dark-mode` avec variables pour mode sombre
- Remplacement couleurs fixes par `var(--nom-variable)`

**Concepts :**

- Variables CSS = boîtes de couleurs réutilisables
- `:root` = déclaration globale
- `var()` = utiliser une variable

### 2. Switch HTML ([index.html](../../../frontend/index.html))

**Lignes ajoutées :** ~15 lignes

- Conteneur `.dark-mode-toggle` dans header
- Input type checkbox stylisé
- Label avec emoji 🌙/☀️

**Concepts :**

- Input checkbox pour switch
- Label cliquable
- Accessibilité (for/id)

### 3. Fonction JavaScript ([app.js](../../../frontend/app.js))

**Lignes ajoutées :** ~20 lignes

- Fonction `toggleDarkMode()` : ajoute/enlève classe
- Sauvegarde dans localStorage
- Vérification au chargement de la page

**Concepts :**

- `classList.toggle()` : ajouter/enlever classe
- `localStorage.setItem()` : sauvegarder donnée
- `localStorage.getItem()` : récupérer donnée
- `addEventListener()` : écouter événement

---

## 🧪 Tests effectués

1. ✅ Clic sur switch → couleurs changent instantanément
2. ✅ Rechargement page → préférence conservée
3. ✅ Mode clair → Mode sombre → Mode clair (plusieurs fois)
4. ✅ Fermer navigateur → Rouvrir → Préférence conservée
5. ✅ Console DevTools → localStorage visible

---

## 📊 Comparaison avant/après

| Aspect               | Session 6        | Session 7                     |
| -------------------- | ---------------- | ----------------------------- |
| **Thème**            | Clair uniquement | Clair + Sombre (switch)       |
| **Préférence**       | Aucune           | Sauvegardée (localStorage)    |
| **Personnalisation** | Aucune           | Utilisateur choisit son thème |
| **Accessibilité**    | Bonne            | Meilleure (confort yeux)      |
| **Variables CSS**    | Couleurs fixes   | Variables réutilisables       |

---

## 📁 Fichiers modifiés

```
frontend/
├── index.html     (+15 lignes : switch dans header)
├── app.js         (+20 lignes : toggleDarkMode + localStorage)
└── style.css      (+30 lignes : variables + .dark-mode)
```

---

## 🎓 Ce que tu as appris

1. **Variables CSS** : Comment créer et utiliser des variables
2. **localStorage** : Comment sauvegarder données navigateur
3. **Toggle classe** : Comment changer apparence dynamiquement
4. **Switch personnalisé** : Styliser un checkbox en switch moderne
5. **Persistance** : Faire mémoriser un choix utilisateur

---

## 🚀 Prochaine étape

**Session 8 (Chat 9) : Tests automatisés** 🧪

- Tests pytest pour backend
- Tests Selenium pour frontend
- CI/CD GitHub Actions
