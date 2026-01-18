# Session 8 : Tests automatisés (pytest + Selenium + GitHub Actions)

> **Date :** 2026-01-16  
> **Durée :** ~2h30  
> **Difficulté :** Moyenne  
> **Prérequis :** Sessions 0-7 complétées

---

## 🎯 Objectif de la session

Apprendre à **tester automatiquement** le code backend (API) et frontend (interface utilisateur) avec :

- **pytest** pour tester les endpoints FastAPI
- **Selenium** pour simuler des clics utilisateur dans le navigateur
- **GitHub Actions** pour lancer les tests automatiquement à chaque commit

---

## 📚 Ce que tu as appris

### Concepts pytest (backend)

1. **TestClient FastAPI** : Simuler des requêtes HTTP sans lancer le serveur
2. **Assertions** : Vérifier que les résultats sont corrects (`assert`)
3. **Fixtures** : Données de test réutilisables (base de données, client HTTP)
4. **Status codes HTTP** : 200 (OK), 422 (validation error), 500 (erreur serveur)

### Concepts Selenium (frontend)

1. **WebDriver** : Pilote automatique pour Chrome/Firefox
2. **Sélecteurs CSS** : Trouver des éléments HTML (`#id`, `.class`, `tag`)
3. **WebDriverWait** : Attendre qu'un élément apparaisse avant de continuer
4. **Mode headless** : Lancer Chrome sans interface graphique (pour CI/CD)

### Concepts GitHub Actions (CI/CD)

1. **Workflow YAML** : Fichier de configuration pour automatiser des tâches
2. **Jobs** : Tâches séparées (backend, frontend) qui s'exécutent dans l'ordre
3. **Runners** : Ordinateurs virtuels GitHub (Ubuntu Linux)
4. **Badge status** : Image dans README.md qui montre si les tests passent ✅ ou échouent ❌

---

## ✅ Fonctionnalités implémentées

### Tests backend (pytest)

- ✅ Test `/ping` : Vérifier que le serveur répond
- ✅ Test `/message` : Sauvegarder un message
- ✅ Test `/messages` : Récupérer tous les messages
- ✅ Test `/chat` : Valider les données envoyées au LLM

**Résultat** : 4 tests passent ✅

### Tests frontend (Selenium)

- ✅ Test ouverture page : Vérifier que `index.html` se charge
- ✅ Test envoi message : Simuler saisie texte + clic bouton + vérifier réponse
- ✅ Test dark mode : Simuler clic switch + vérifier classe CSS `dark-mode`

**Résultat** : 3 tests passent ✅

### CI/CD GitHub Actions

- ✅ Workflow avec 2 jobs séparés (backend + frontend)
- ✅ Tests lancés automatiquement à chaque `git push`
- ✅ Badge status dans README.md
- ✅ Mode headless automatique pour Selenium (détection variable `CI`)

---

## 📂 Fichiers créés

```
tests/
├── __init__.py                  (Package Python pour pytest)
├── test_backend.py              (4 tests pytest pour API)
└── test_frontend.py             (3 tests Selenium pour UI)

.github/
└── workflows/
    └── tests.yml                (Configuration GitHub Actions)
```

---

## 🔧 Commandes apprises

### Tests locaux

```powershell
# Installer pytest et dépendances
pip install pytest pytest-asyncio httpx
pip install selenium webdriver-manager

# Lancer tests backend
pytest tests/test_backend.py -v

# Lancer tests frontend (backend doit être actif)
uvicorn backend.main:app --reload  # Terminal 1
pytest tests/test_frontend.py -v -s  # Terminal 2
```

### GitHub Actions

```powershell
# Créer workflow
mkdir .github\workflows
New-Item .github\workflows\tests.yml

# Push pour déclencher workflow
git push origin feature/session8-tests
```

---

## 🎓 Concepts clés (analogies)

| Concept            | Analogie                                              |
| ------------------ | ----------------------------------------------------- |
| **pytest**         | Professeur qui corrige des exercices automatiquement  |
| **TestClient**     | Postman automatisé dans le code                       |
| **Selenium**       | Robot qui utilise ton navigateur comme un humain      |
| **WebDriverWait**  | Attendre qu'une personne arrive avant de lui parler   |
| **GitHub Actions** | Robot GitHub qui travaille pour toi 24/7              |
| **Headless mode**  | Chrome sans écran (comme un ordinateur sans moniteur) |

---

## 🐛 Problèmes rencontrés et solutions

### Problème 1 : `pywin32` sur Linux (GitHub Actions)

**Erreur** : `ERROR: No matching distribution found for pywin32==311`  
**Cause** : `pywin32` est Windows-only, pas disponible sur Ubuntu  
**Solution** : Installer seulement les dépendances nécessaires dans le workflow (pas `requirements.txt`)

### Problème 2 : Table SQLite manquante

**Erreur** : `sqlite3.OperationalError: no such table: messages`  
**Cause** : Base de données non initialisée avant les tests  
**Solution** : Appeler `initialiser_db()` dans `test_backend.py`

### Problème 3 : Chrome crash en CI/CD

**Erreur** : `SessionNotCreatedException: Chrome instance exited`  
**Cause** : Chrome ne peut pas démarrer en mode graphique sur GitHub Actions  
**Solution** : Mode headless automatique avec détection variable `CI`

### Problème 4 : Sélecteurs CSS incorrects

**Erreur** : `NoSuchElementException`  
**Cause** : IDs HTML différents (`messageInput` vs `message-input`)  
**Solution** : Vérifier les IDs réels dans `index.html`

---

## 💡 Points importants

1. **Tests backend** : Rapides, fiables, toujours exécutés en CI/CD
2. **Tests frontend** : Plus lents, parfois instables (timing, affichage)
3. **Mode headless** : Obligatoire pour CI/CD (pas d'écran disponible)
4. **Timeout** : Toujours prévoir un délai max (10-30s) pour éviter blocages infinis
5. **Badge status** : Rassure les contributeurs que le code fonctionne

---

## 📊 Progression globale du projet

| Session | Thème                   | Status |
| ------- | ----------------------- | ------ |
| 0       | Setup environnement     | ✅     |
| 1       | Pydantic (validation)   | ✅     |
| 2       | SQLite (persistance)    | ✅     |
| 3       | LLM (GPT-4o)            | ✅     |
| 4       | Frontend (HTML + JS)    | ✅     |
| 5       | CSS (design moderne)    | ✅     |
| 6       | UX (auto-scroll, clear) | ✅     |
| 7       | Dark mode               | ✅     |
| **8**   | **Tests automatisés**   | ✅     |
| 9       | Déploiement             | ⏳     |

---

## 🚀 Prochaine session

**Session 9 : Déploiement production**

Tu apprendras à :

- Déployer le backend sur Render ou Railway
- Déployer le frontend sur GitHub Pages ou Vercel
- Configurer un domaine personnalisé
- Ajouter HTTPS automatique

---

## 📝 Notes personnelles

**Ce que j'ai aimé** :

- Voir Chrome s'ouvrir automatiquement (Selenium)
- Tests qui passent en vert ✅ (satisfaction garantie)
- Badge GitHub Actions dans README.md

**Ce qui m'a surpris** :

- Les tests backend sont très rapides (~1 seconde)
- Mode headless détecté automatiquement en CI/CD
- GitHub Actions gratuit pour projets publics

**Difficultés rencontrées** :

- Sélecteurs CSS incorrects (résolu avec vérification HTML)
- Chrome crash en CI/CD (résolu avec mode headless)
- Timeout trop court pour LLM (résolu avec 30 secondes)

---

_Dernière mise à jour : 2026-01-17_
