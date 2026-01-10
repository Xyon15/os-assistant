# 🌳 Workflow Git — Branches & Organisation

> Guide complet pour travailler avec les branches Git (local + GitHub)

---

## 📚 Table des matières

1. [Concept des branches](#concept-des-branches)
2. [Commandes essentielles](#commandes-essentielles)
3. [Workflow recommandé](#workflow-recommandé)
4. [Gestion des conflits](#gestion-des-conflits)
5. [Exemples pratiques](#exemples-pratiques)
6. [Aide-mémoire](#aide-mémoire)

---

## 🌳 Concept des branches

### **Analogie : Arbre avec branches**

```
         🌳 Arbre (ton projet)
              |
        ══════════════ main (tronc principal = version stable)
        ║
        ║
   ┌────╨────┐
   │         │
   🌿       🌿  Branches (expérimentations)
feature/  feature/
  css    historique
```

**Principe :**

- **`main`** = Version stable et fonctionnelle (MVP)
- **Branches** = Copies parallèles pour expérimenter
- Si l'expérience réussit → **fusionner** dans `main`
- Si l'expérience échoue → **supprimer** la branche (main reste intact)

---

## ⚙️ Commandes essentielles

### **Voir les branches**

```bash
# Branches locales (sur ton PC)
git branch

# Branches locales + GitHub (remote)
git branch -a

# Voir quelle branche est active (avec *)
git branch
# * main          ← Tu es ici
#   feature/css
```

### **Créer une branche**

```bash
# Créer ET se déplacer sur la nouvelle branche
git checkout -b nom-branche

# Exemple :
git checkout -b feature/css
```

**Alternative (Git moderne) :**

```bash
git switch -c nom-branche
```

### **Changer de branche**

```bash
# Aller sur une autre branche
git checkout nom-branche

# Exemple : retourner sur main
git checkout main
```

**Alternative (Git moderne) :**

```bash
git switch nom-branche
```

### **Fusionner une branche**

```bash
# 1. Aller sur la branche de destination (main)
git checkout main

# 2. Fusionner une autre branche dans main
git merge nom-branche

# Exemple : intégrer feature/css dans main
git checkout main
git merge feature/css
```

### **Supprimer une branche**

```bash
# Supprimer localement (après fusion)
git branch -d nom-branche

# Forcer la suppression (même sans fusion)
git branch -D nom-branche

# Supprimer sur GitHub
git push origin --delete nom-branche
```

### **Pousser une branche vers GitHub**

```bash
# Pousser la branche actuelle vers GitHub
git push origin nom-branche

# Exemple : pousser feature/css
git push origin feature/css
```

---

## 🔄 Workflow recommandé

### **Structure organisée**

```
main (MVP stable - v0.1.0-mvp)
└── RÈGLE : Ne JAMAIS coder directement dans main

Pour chaque nouvelle feature :
├── feature/session5-css           # Design et style
├── feature/historique-loading     # Charger historique
├── feature/clear-button           # Bouton effacer
└── feature/error-handling         # Gestion erreurs
```

### **Workflow étape par étape**

#### **1. Créer une branche pour une nouvelle feature**

```bash
# Toujours partir de main à jour
git checkout main
git pull origin main  # Récupérer dernières modifications GitHub

# Créer la branche
git checkout -b feature/nom-feature

# Exemple :
git checkout -b feature/session5-css
```

#### **2. Travailler sur la branche**

```bash
# Faire tes modifications (éditer fichiers, ajouter code...)
# Exemple : créer frontend/style.css

# Committer les changements
git add .
git commit -m "feat(css): add modern chat bubbles"

# Tu peux faire plusieurs commits sur la branche
git add .
git commit -m "feat(css): add colors and spacing"
```

#### **3. Pousser la branche vers GitHub (sauvegarde cloud)**

```bash
git push origin feature/session5-css
```

**Résultat :** Ta branche est maintenant sur GitHub (sauvegarde + partage possible).

#### **4. Tester que tout fonctionne**

```bash
# Tester localement
uvicorn backend.main:app --reload
# Ouvrir frontend/index.html
# Vérifier que le CSS fonctionne bien
```

#### **5. Fusionner dans main (quand satisfait)**

```bash
# Retourner sur main
git checkout main

# Fusionner la branche
git merge feature/session5-css

# Pousser main mis à jour vers GitHub
git push origin main
```

#### **6. Supprimer la branche (ménage)**

```bash
# Local
git branch -d feature/session5-css

# GitHub
git push origin --delete feature/session5-css
```

---

## ⚠️ Gestion des conflits

### **Question : Plusieurs branches en même temps = conflits ?**

**Réponse courte : NON, pas automatiquement !**

### **Cas 1 : Branches indépendantes (PAS de conflit)**

```
main
├── feature/css              ← Modifie frontend/style.css
└── feature/historique       ← Modifie backend/main.py
```

**Résultat :** Aucun conflit !

- Les deux branches modifient des **fichiers différents**
- Tu peux les fusionner dans n'importe quel ordre

```bash
git checkout main
git merge feature/css           # OK ✅
git merge feature/historique    # OK ✅
```

### **Cas 2 : Branches qui touchent le même fichier (CONFLIT possible)**

```
main
├── feature/css              ← Modifie frontend/index.html (ligne 10)
└── feature/historique       ← Modifie frontend/index.html (ligne 10 aussi !)
```

**Résultat :** Git détecte un **conflit** !

#### **Comment Git signale un conflit**

Quand tu fais `git merge feature/historique` après avoir fusionné `feature/css` :

```bash
Auto-merging frontend/index.html
CONFLICT (content): Merge conflict in frontend/index.html
Automatic merge failed; fix conflicts and then commit the result.
```

#### **Résoudre le conflit**

Git modifie le fichier en conflit avec des marqueurs :

**frontend/index.html (avec conflit) :**

```html
<body>
  <h1>Assistant IA</h1>
  <<<<<<< HEAD
  <div id="historique"></div>
  ← Version de main (après merge CSS) =======
  <div id="conversation"></div>
  ← Version de feature/historique >>>>>>> feature/historique
</body>
```

**Étapes pour résoudre :**

1. **Ouvrir le fichier** dans VS Code
2. **Choisir quelle version garder** (ou fusionner manuellement)
3. **Supprimer les marqueurs** `<<<<<<<`, `=======`, `>>>>>>>`
4. **Committer la résolution**

```bash
# Après avoir édité le fichier
git add frontend/index.html
git commit -m "merge: resolve conflict in index.html"
```

### **Stratégie pour ÉVITER les conflits**

#### **1. Fusionner régulièrement main dans tes branches**

Si tu travailles longtemps sur une branche :

```bash
# Sur ta branche feature/css
git checkout feature/css

# Récupérer les changements de main
git checkout main
git pull origin main

# Fusionner main dans ta branche
git checkout feature/css
git merge main

# Résoudre conflits éventuels maintenant (plus facile)
```

**Avantage :** Conflits résolus **progressivement** au lieu de tous en même temps.

#### **2. Diviser le travail intelligemment**

**Bonne pratique :**

```
feature/css              ← Modifie uniquement frontend/style.css
feature/historique       ← Modifie uniquement backend/main.py
feature/clear-button     ← Modifie uniquement frontend/app.js
```

**À éviter :**

```
feature/css              ← Modifie frontend/index.html
feature/historique       ← Modifie frontend/index.html aussi
                          ← CONFLIT PROBABLE !
```

#### **3. Fusionner dans l'ordre logique**

Si deux branches dépendent l'une de l'autre :

```bash
# D'abord feature/css (base)
git checkout main
git merge feature/css

# Puis feature/historique (dépend du CSS)
git merge feature/historique
```

---

## 💡 Exemples pratiques

### **Exemple 1 : Ajouter CSS (Session 5)**

```bash
# 1. Créer branche
git checkout -b feature/session5-css

# 2. Créer fichier frontend/style.css
# 3. Modifier frontend/index.html pour charger style.css

# 4. Committer
git add .
git commit -m "feat(css): add modern chat interface design"

# 5. Pousser vers GitHub
git push origin feature/session5-css

# 6. Tester localement
# Ouvrir frontend/index.html et vérifier le design

# 7. Fusionner dans main
git checkout main
git merge feature/session5-css

# 8. Pousser main
git push origin main

# 9. Supprimer branche
git branch -d feature/session5-css
git push origin --delete feature/session5-css
```

### **Exemple 2 : Plusieurs branches en parallèle**

```bash
# Créer branche CSS
git checkout -b feature/css
# ... faire modifications CSS ...
git add .
git commit -m "feat(css): add styles"
git push origin feature/css

# Retourner sur main et créer branche historique
git checkout main
git checkout -b feature/historique
# ... faire modifications historique ...
git add .
git commit -m "feat(historique): load messages on startup"
git push origin feature/historique

# Fusionner les deux (ordre indifférent si pas de conflit)
git checkout main
git merge feature/css           # Fusionner CSS
git merge feature/historique    # Fusionner historique
git push origin main

# Supprimer branches
git branch -d feature/css feature/historique
git push origin --delete feature/css feature/historique
```

### **Exemple 3 : Annuler une branche (expérience ratée)**

```bash
# Créer branche test
git checkout -b feature/test-new-idea

# Faire des modifications
git add .
git commit -m "test: try new approach"

# Finalement, tu n'aimes pas → ANNULER

# Retourner sur main
git checkout main

# Supprimer la branche (SANS fusionner)
git branch -D feature/test-new-idea  # -D (majuscule) force la suppression

# Si déjà poussée sur GitHub
git push origin --delete feature/test-new-idea
```

**Résultat :** Comme si tu n'avais jamais essayé ! `main` reste intact.

---

## 📋 Aide-mémoire

### **Commandes quotidiennes**

```bash
# Voir où je suis
git branch

# Créer et aller sur nouvelle branche
git checkout -b feature/nom

# Changer de branche
git checkout nom-branche

# Committer changements
git add .
git commit -m "type(scope): description"

# Pousser vers GitHub
git push origin nom-branche

# Fusionner dans main
git checkout main
git merge feature/nom

# Supprimer branche
git branch -d feature/nom                # Local
git push origin --delete feature/nom     # GitHub
```

### **Cas d'urgence**

```bash
# Annuler tous les changements non commités
git reset --hard

# Retourner à un commit précédent (dangereux !)
git reset --hard <commit-hash>

# Voir l'historique des commits
git log --oneline

# Annuler le dernier commit (garder modifications)
git reset --soft HEAD~1
```

### **Conflits**

```bash
# Voir les fichiers en conflit
git status

# Après résolution manuelle
git add fichier-resolu.py
git commit -m "merge: resolve conflict"

# Annuler un merge en cours
git merge --abort
```

---

## ✅ Checklist pour chaque feature

```
□ Créer branche depuis main à jour
□ Nommer clairement : feature/nom-descriptif
□ Faire modifications + commits réguliers
□ Pousser vers GitHub (sauvegarde)
□ Tester localement
□ Fusionner dans main
□ Pousser main vers GitHub
□ Supprimer branche (local + GitHub)
□ Mettre à jour documentation si besoin
```

---

## 🎯 Bonnes pratiques

1. **Une branche = une feature** (pas tout mélanger)
2. **Commits fréquents** avec messages clairs
3. **Tester avant de fusionner** dans main
4. **Main toujours stable** (MVP fonctionnel)
5. **Supprimer branches fusionnées** (garder propre)
6. **Pousser régulièrement** vers GitHub (sauvegarde)
7. **Fusionner main dans branche longue durée** (éviter conflits)

---

## 🚀 Organisation recommandée pour ce projet

### **Structure des branches**

```
main (v0.1.0-mvp) ← Stable et fonctionnel
├── feature/session5-css           ← Design moderne
├── feature/historique-loading     ← Charger messages
├── feature/clear-button           ← Bouton effacer
├── feature/error-handling         ← Gestion erreurs
└── feature/auto-scroll            ← Scroll automatique
```

### **Workflow projet**

```bash
# Pour chaque Session/Feature :

# 1. Créer branche
git checkout -b feature/sessionX-nom

# 2. Développer + committer
# (plusieurs commits OK)

# 3. Pousser vers GitHub
git push origin feature/sessionX-nom

# 4. Tester

# 5. Documenter (README, GUIDE_TECHNIQUE)

# 6. Fusionner + taguer si nouvelle version
git checkout main
git merge feature/sessionX-nom
git tag -a v0.X.0 -m "Description"
git push origin main --tags

# 7. Nettoyer
git branch -d feature/sessionX-nom
git push origin --delete feature/sessionX-nom
```

---

## ❓ FAQ

**Q : Puis-je avoir plusieurs branches en même temps ?**  
**R :** Oui ! Tant qu'elles modifient des fichiers différents, pas de problème.

**Q : Que se passe-t-il si j'oublie de fusionner une branche ?**  
**R :** Rien ! La branche reste là. Tu peux la fusionner plus tard ou la supprimer.

**Q : Puis-je revenir en arrière après une fusion ?**  
**R :** Oui, mais c'est plus complexe (`git revert` ou `git reset`). Mieux vaut tester avant de fusionner !

**Q : Dois-je toujours pousser mes branches vers GitHub ?**  
**R :** Pas obligatoire, mais **fortement recommandé** (sauvegarde + possibilité de partage).

**Q : Comment voir les différences entre deux branches ?**  
**R :** `git diff main..feature/css`

---

_Dernière mise à jour : 2026-01-10_
