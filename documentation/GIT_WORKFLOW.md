# 🌿 Guide Git Workflow

> Guide complet du workflow Git utilisé dans OS Assistant

**Date :** 2026-01-13  
**Basé sur :** Session 5 (feature/session5-css)

---

## 🎯 Vue d'ensemble

Ce guide explique **étape par étape** comment créer une nouvelle fonctionnalité avec Git et GitHub, depuis la création de la branche jusqu'au merge dans `main`.

**Workflow utilisé :** GitHub Flow (simplifié)

---

## 📋 Prérequis

- Git installé
- Repository cloné localement
- Compte GitHub configuré
- PowerShell ou terminal similaire

---

## 🚀 Workflow complet (7 étapes)

### **Étape 1 : Créer une branche feature**

```powershell
# S'assurer d'être sur main et à jour
git checkout main
git pull origin main

# Créer et basculer sur une nouvelle branche
git checkout -b feature/nom-feature

# Exemples de noms de branches :
# - feature/session5-css
# - feature/auto-scroll
# - feature/dark-mode
# - fix/bug-cors
```

**Convention de nommage :**

- `feature/` : Nouvelle fonctionnalité
- `fix/` : Correction de bug
- `docs/` : Documentation uniquement
- `refactor/` : Refactorisation du code

---

### **Étape 2 : Développer la fonctionnalité**

```powershell
# Travailler sur les fichiers
# Tester localement
# S'assurer que tout fonctionne
```

**Bonnes pratiques :**

- ✅ Tester fréquemment pendant le développement
- ✅ Committer régulièrement (petits commits)
- ✅ Suivre la checklist de documentation (si applicable)

---

### **Étape 3 : Vérifier les changements**

```powershell
# Voir les fichiers modifiés
git status

# Voir les différences ligne par ligne
git diff

# Voir les différences pour un fichier spécifique
git diff frontend/style.css
```

**Vérifications :**

- ✅ Tous les fichiers nécessaires sont modifiés
- ✅ Pas de fichiers indésirables (ex: `memory.db`, `.env`)
- ✅ Code testé et fonctionnel

---

### **Étape 4 : Créer le commit**

```powershell
# Ajouter tous les fichiers modifiés
git add .

# OU ajouter fichiers spécifiques
git add frontend/style.css frontend/index.html

# Créer le commit avec message Conventional Commits
git commit -m "feat(css): add modern design with Flexbox and animations [ChatN/SessionX]

Frontend improvements:
- Add style.css (~120 lines) with Flexbox layout
- Add styled chat bubbles (user blue right, assistant gray left)
- Add CSS animations (fadeIn + hover scale)
- Replace innerHTML += with createElement() + appendChild()

Documentation:
- docs/sessions/session_5_css/ with README + GUIDE_TECHNIQUE + scripts/
- docs/INDEX.md and README.md updated

Concepts learned: Flexbox, CSS animations, createElement(), setTimeout()
Tests: All layout, animations, and interactions working perfectly"
```

**Format Conventional Commits :**

```
type(scope): description [ChatN/SessionX]

Corps du message avec détails :
- Point 1
- Point 2

Footer (optionnel)
```

**Types courants :**

- `feat` : Nouvelle fonctionnalité
- `fix` : Correction de bug
- `docs` : Documentation uniquement
- `refactor` : Refactorisation sans changement de fonctionnalité
- `test` : Ajout/modification de tests
- `chore` : Tâches de maintenance (dépendances, config)

**Exemples :**

```bash
feat(frontend): add dark mode toggle [Chat7/Session6]
fix(api): correct CORS headers [Chat4/Session3]
docs(readme): update installation instructions [Chat1/Session0]
refactor(memory): optimize database queries [Chat5/Session4]
```

---

### **Étape 5 : Pousser la branche sur GitHub**

```powershell
# Pousser la branche vers GitHub
git push origin feature/nom-feature

# Exemple concret :
git push origin feature/session5-css
```

**Ce qui se passe :**

- Git envoie la branche vers le repository distant (GitHub)
- GitHub affiche un lien pour créer une Pull Request

**Résultat dans le terminal :**

```
remote: Create a pull request for 'feature/session5-css' on GitHub by visiting:
remote:      https://github.com/Xyon15/os-assistant/pull/new/feature/session5-css
```

---

### **Étape 6 : Créer une Pull Request (PR)**

#### **Méthode A : Via le lien du terminal (recommandé)**

1. Copier le lien affiché dans le terminal après `git push`
2. Ouvrir le lien dans le navigateur
3. Passer à l'étape "Remplir la PR" ci-dessous

#### **Méthode B : Via GitHub.com**

1. Aller sur https://github.com/Xyon15/os-assistant
2. GitHub affiche un bandeau jaune "Compare & pull request"
3. Cliquer sur ce bandeau
4. Passer à l'étape "Remplir la PR" ci-dessous

#### **Remplir la Pull Request**

**Titre :**

```
feat(css): Add modern design with Flexbox and animations [Session 5]
```

**Description (template) :**

```markdown
## 🎨 [Nom de la session/feature]

### ✅ Ce qui a été ajouté

**Code :**

- ✅ Fichier 1 : description
- ✅ Fichier 2 : description
- ✅ Fichier 3 : description

**Documentation :**

- ✅ docs/sessions/sessionN/ créé
- ✅ docs/INDEX.md mis à jour
- ✅ docs/README.md mis à jour
- ✅ README.md racine mis à jour
- ✅ CURRENT_STATE.md créé

### 🧪 Tests

- ✅ Test 1 : résultat
- ✅ Test 2 : résultat
- ✅ Test 3 : résultat

### 📚 Concepts appris

- Concept 1
- Concept 2
- Concept 3

### 📸 Screenshots (optionnel)

[Ajouter captures d'écran si pertinent]
```

**Exemple concret (Session 5) :**

```markdown
## 🎨 Session 5 — CSS & Design Moderne

### ✅ Ce qui a été ajouté

**Frontend :**

- ✅ Fichier `style.css` avec design moderne (~120 lignes)
- ✅ Layout Flexbox (vertical + horizontal)
- ✅ Bulles de chat (user bleue droite, assistant grise gauche)
- ✅ Animations CSS (fadeIn + hover)
- ✅ Optimisation JavaScript (`createElement()` au lieu de `innerHTML +=`)
- ✅ Délai naturel 400ms avant message chargement
- ✅ Commentaires complets sur tous les fichiers frontend

**Documentation :**

- ✅ `docs/sessions/session_5_css/` (README + GUIDE_TECHNIQUE + scripts)
- ✅ `docs/INDEX.md` mis à jour
- ✅ `docs/README.md` mis à jour
- ✅ `README.md` racine mis à jour (4 sections)
- ✅ `CURRENT_STATE.md` créé
- ✅ Instructions Copilot mises à jour

### 🧪 Tests

- ✅ Layout Flexbox fonctionnel
- ✅ Bulles alignées correctement
- ✅ Animations uniquement sur nouveaux messages
- ✅ Délai naturel avant "est en train d'écrire..."
- ✅ Hover sur bulles fonctionne

### 📚 Concepts appris

- Flexbox CSS
- Animations CSS (`@keyframes`, `:hover`)
- `createElement()` + `appendChild()`
- `setTimeout()` pour délais naturels
```

**Assignees (optionnel) :** Assigner la PR à toi-même

**Labels (optionnel) :** `enhancement`, `documentation`, `frontend`

**Cliquer sur "Create pull request"** (bouton vert)

---

### **Étape 7 : Merger la Pull Request**

#### **Vérifications avant merge**

1. ✅ Tous les fichiers sont corrects
2. ✅ Description claire et complète
3. ✅ Tests passés (si applicables)
4. ✅ Pas de conflits avec `main`

#### **Effectuer le merge**

1. Cliquer sur **"Merge pull request"** (bouton vert)
2. Confirmer avec **"Confirm merge"**
3. Optionnel : **"Delete branch"** (nettoyer la branche feature)

**Types de merge disponibles :**

- **Merge commit** (par défaut) : Crée un commit de merge
- **Squash and merge** : Fusionne tous les commits en un seul
- **Rebase and merge** : Applique les commits un par un

**Recommandation :** Utiliser **"Merge commit"** pour garder l'historique complet.

---

## 🔄 Après le merge : Revenir sur main

```powershell
# Revenir sur la branche main
git checkout main

# Récupérer les derniers changements depuis GitHub (incluant le merge)
git pull origin main

# Vérifier que tout est à jour
git status

# Résultat attendu :
# On branch main
# Your branch is up to date with 'origin/main'.
# nothing to commit, working tree clean
```

**Optionnel : Supprimer la branche locale**

```powershell
# Si la branche a été supprimée sur GitHub, la supprimer aussi localement
git branch -d feature/session5-css

# Force delete si nécessaire (attention !)
git branch -D feature/session5-css
```

---

## 📊 Résumé visuel du workflow

```
main (local)
    ↓ git checkout -b feature/nom
feature/nom (local)
    ↓ développement + commits
feature/nom (local avec commits)
    ↓ git push origin feature/nom
feature/nom (GitHub)
    ↓ Créer Pull Request
Pull Request sur GitHub
    ↓ Review + Merge
main (GitHub avec nouveaux changements)
    ↓ git pull origin main
main (local à jour)
```

---

## 🔍 Commandes utiles

### **Voir l'historique des commits**

```powershell
# Historique complet
git log

# Historique compact (une ligne par commit)
git log --oneline

# Historique avec graphe
git log --oneline --graph --all
```

### **Voir les différences**

```powershell
# Différences non stagées
git diff

# Différences stagées (après git add)
git diff --staged

# Différences entre deux branches
git diff main feature/session5-css
```

### **Annuler des changements (avec prudence !)**

```powershell
# Annuler modifications NON commitées d'un fichier
git checkout -- frontend/style.css

# Annuler dernier commit (GARDE les changements)
git reset --soft HEAD~1

# Annuler dernier commit (SUPPRIME les changements)
git reset --hard HEAD~1
```

### **Gestion des branches**

```powershell
# Lister toutes les branches locales
git branch

# Lister toutes les branches (locales + distantes)
git branch -a

# Supprimer une branche locale
git branch -d feature/old-feature

# Supprimer une branche distante
git push origin --delete feature/old-feature
```

---

## ⚠️ Situations courantes

### **Problème : Conflits de merge**

**Symptômes :**

```
CONFLICT (content): Merge conflict in frontend/app.js
Automatic merge failed; fix conflicts and then commit the result.
```

**Solution :**

1. Ouvrir les fichiers en conflit dans VS Code
2. Choisir les changements à garder (Accept Current / Accept Incoming / Accept Both)
3. Sauvegarder les fichiers
4. Committer :
   ```powershell
   git add .
   git commit -m "fix: resolve merge conflicts"
   git push origin feature/nom
   ```

---

### **Problème : Oublié de commit avant de changer de branche**

**Solution :**

```powershell
# Sauvegarder les changements temporairement
git stash

# Changer de branche
git checkout main

# Revenir sur la branche et restaurer les changements
git checkout feature/nom
git stash pop
```

---

### **Problème : Commit avec mauvais message**

**Solution (si pas encore pushé) :**

```powershell
# Modifier le message du dernier commit
git commit --amend -m "nouveau message"

# Si déjà pushé, force push (attention !)
git push origin feature/nom --force
```

---

### **Problème : Fichier sensible commité par erreur (.env, memory.db)**

**Solution :**

```powershell
# Supprimer du suivi Git (garde le fichier localement)
git rm --cached .env

# Ajouter au .gitignore
echo ".env" >> .gitignore

# Committer
git add .gitignore
git commit -m "chore: remove .env from git tracking"
git push origin feature/nom
```

---

## 📋 Checklist complète pour chaque feature

```
□ 1. Créer branche : git checkout -b feature/nom
□ 2. Développer la fonctionnalité
□ 3. Tester localement (backend + frontend)
□ 4. Vérifier fichiers : git status
□ 5. Ajouter fichiers : git add .
□ 6. Committer : git commit -m "type(scope): message"
□ 7. Pousser : git push origin feature/nom
□ 8. Créer Pull Request sur GitHub
□ 9. Remplir description PR (checklist complète)
□ 10. Merger la PR
□ 11. Revenir sur main : git checkout main
□ 12. Mettre à jour : git pull origin main
□ 13. (Optionnel) Supprimer branche : git branch -d feature/nom
□ 14. Mettre à jour FEATURES.md (cocher ✅)
```

---

## 🎓 Bonnes pratiques

### **Commits**

✅ **DO :**

- Commits fréquents et petits
- Messages descriptifs (Conventional Commits)
- Tester avant de committer
- Inclure [ChatN/SessionX] dans les commits

❌ **DON'T :**

- Commits géants avec 50 fichiers modifiés
- Messages vagues ("fix", "update")
- Committer du code non testé
- Committer fichiers sensibles (.env, clés API)

### **Branches**

✅ **DO :**

- Créer une branche par fonctionnalité/session
- Noms descriptifs (feature/session5-css)
- Merger régulièrement dans main
- Supprimer branches mergées

❌ **DON'T :**

- Travailler directement sur main
- Branches avec noms vagues (test, temp)
- Garder branches old/inactives
- Branches trop longues (plusieurs sessions)

### **Pull Requests**

✅ **DO :**

- Description complète avec checklist
- Tests documentés
- Screenshots si pertinent
- Merger rapidement après validation

❌ **DON'T :**

- PR sans description
- PR énormes (+500 lignes modifiées)
- Laisser PR ouvertes trop longtemps

---

## 📚 Ressources

- [Git Documentation officielle](https://git-scm.com/doc)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Oh Shit, Git!?!](https://ohshitgit.com/) (Guide de dépannage humoristique)

---

## 🎯 Exemple complet (Session 5)

**Commandes exactes utilisées :**

```powershell
# 1. Créer branche
git checkout -b feature/session5-css

# 2. Développement (création style.css, modifications app.js, index.html, documentation)

# 3. Vérifier changements
git status

# 4. Ajouter tous les fichiers
git add .

# 5. Committer avec message détaillé
git commit -m "feat(css): add modern design with Flexbox and animations [Chat6/Session5]

Frontend improvements:
- Add style.css (~120 lines) with Flexbox layout
- Add styled chat bubbles (user blue right, assistant gray left)
- Add CSS animations (fadeIn + hover scale)
- Replace innerHTML += with createElement() + appendChild()
- Add 400ms delay before loading message (natural UX)
- Add comprehensive comments to all frontend files

Modified files:
- frontend/style.css (NEW): 4 blocks (layout, input, bubbles, animations)
- frontend/index.html: remove 'Interface prête', add id='inputZone', add comments
- frontend/app.js: optimize DOM manipulation, add setTimeout, add comments

Documentation:
- docs/sessions/session_5_css/ with README + GUIDE_TECHNIQUE + scripts/
- docs/INDEX.md updated (Session 5 added)
- docs/README.md updated (Session 5 section)
- README.md root updated (4 sections: sessions, guides, changelog, status)
- docs/chat_transitions/chat_6_session_5/CURRENT_STATE.md created
- .github/instructions/ updated with Session 5 observations

Concepts learned: Flexbox, CSS animations, createElement(), setTimeout()
Tests: All layout, animations, and interactions working perfectly"

# 6. Pousser vers GitHub
git push origin feature/session5-css

# 7. Créer Pull Request sur GitHub (via navigateur)

# 8. Merger la Pull Request (via navigateur)

# 9. Revenir sur main
git checkout main

# 10. Récupérer les changements
git pull origin main

# 11. Vérifier que tout est à jour
git status
```

**Résultat :** Session 5 complète, mergée et documentée ! 🎉

---

_Dernière mise à jour : 2026-01-13 (basé sur Session 5)_
