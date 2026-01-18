# Guide Technique — Session 8 : Tests automatisés

> **Concepts approfondis** : pytest, Selenium, GitHub Actions, CI/CD

---

## 📚 Table des matières

1. [Tests pytest (backend)](#1-tests-pytest-backend)
2. [Tests Selenium (frontend)](#2-tests-selenium-frontend)
3. [GitHub Actions (CI/CD)](#3-github-actions-cicd)
4. [Bonnes pratiques](#4-bonnes-pratiques)

---

## 1. Tests pytest (backend)

### 1.1 Qu'est-ce que pytest ?

**pytest** = framework de test Python qui :

- Trouve automatiquement les fonctions commençant par `test_`
- Exécute chaque test et vérifie les assertions
- Affiche un rapport détaillé (tests passés ✅ / échoués ❌)

**Analogie** : Comme un professeur qui corrige des exercices automatiquement.

---

### 1.2 Structure d'un test pytest

```python
def test_exemple():
    # 1. Arranger (Arrange) : Préparer les données
    payload = {"texte": "Hello"}

    # 2. Agir (Act) : Exécuter l'action à tester
    response = client.post("/message", json=payload)

    # 3. Affirmer (Assert) : Vérifier le résultat
    assert response.status_code == 200
    assert response.json()["recu"] == True
```

**Pattern AAA** (Arrange-Act-Assert) = structure standard pour tous les tests.

---

### 1.3 TestClient FastAPI

**TestClient** = simulateur de requêtes HTTP **sans lancer uvicorn**.

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Envoyer requête GET
response = client.get("/ping")

# Envoyer requête POST avec JSON
response = client.post("/message", json={"texte": "Test"})
```

**Avantages** :

- Pas besoin de lancer le serveur manuellement
- Tests ultra-rapides (~1 seconde pour 4 tests)
- Isolation complète (chaque test redémarre l'app)

---

### 1.4 Assertions pytest

**Assertions** = vérifications que le résultat est correct.

```python
# Vérifier égalité
assert response.status_code == 200

# Vérifier contenu
assert "pong" in response.json()

# Vérifier type
assert isinstance(data["messages"], list)

# Vérifier présence clé
assert "id" in data
```

**Si une assertion échoue**, pytest affiche :

- La ligne exacte qui a échoué
- La valeur attendue vs la valeur obtenue
- Le contexte complet de l'erreur

---

### 1.5 Initialisation base de données

**Problème** : Les tests échouent si la table SQLite n'existe pas.

**Solution** : Appeler `initialiser_db()` **avant** de créer le `TestClient`.

```python
from backend.memory import initialiser_db

# Créer table messages AVANT les tests
initialiser_db()

client = TestClient(app)
```

**Ordre d'exécution** :

1. Imports
2. Initialisation DB
3. Création TestClient
4. Exécution tests

---

## 2. Tests Selenium (frontend)

### 2.1 Qu'est-ce que Selenium ?

**Selenium** = outil qui pilote automatiquement un navigateur (Chrome, Firefox).

**Analogie** : Comme un robot qui utilise ton navigateur à ta place.

**Cas d'usage** :

- Tester l'interface utilisateur (clics, saisie texte, navigation)
- Automatiser des tâches répétitives
- Vérifier que le frontend fonctionne correctement

---

### 2.2 WebDriver et ChromeDriver

**WebDriver** = API standard pour piloter un navigateur.  
**ChromeDriver** = programme qui traduit les commandes Selenium en actions Chrome.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Télécharger et installer ChromeDriver automatiquement
service = Service(ChromeDriverManager().install())

# Créer driver Chrome
driver = webdriver.Chrome(service=service)

# Ouvrir page
driver.get("file:///C:/Dev/os-assistant/frontend/index.html")

# Fermer navigateur
driver.quit()
```

**webdriver-manager** télécharge automatiquement la bonne version de ChromeDriver (pratique !).

---

### 2.3 Sélecteurs CSS

**Sélecteurs CSS** = chemins pour trouver des éléments HTML.

```python
from selenium.webdriver.common.by import By

# Trouver élément par ID
element = driver.find_element(By.CSS_SELECTOR, "#messageInput")

# Trouver élément par classe
element = driver.find_element(By.CSS_SELECTOR, ".slider")

# Trouver élément par tag
element = driver.find_element(By.TAG_NAME, "body")

# Trouver TOUS les éléments correspondants
elements = driver.find_elements(By.CSS_SELECTOR, ".message-user")
```

**Différence** :

- `find_element()` → retourne 1 élément (erreur si absent)
- `find_elements()` → retourne liste (vide si aucun)

---

### 2.4 Interactions avec éléments

```python
# Saisir texte dans input
input_element.send_keys("Bonjour")

# Cliquer sur bouton
button.click()

# Lire attribut
class_name = body.get_attribute("class")

# Lire texte affiché
text = element.text
```

**Important** : L'élément doit être **visible et interactable** (pas caché par CSS).

---

### 2.5 WebDriverWait (attente explicite)

**Problème** : Le navigateur met du temps à charger → erreur si on cherche l'élément trop tôt.

**Solution** : Attendre que l'élément apparaisse avant de continuer.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Attendre max 30 secondes que l'élément apparaisse
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".message-user"))
)

# Maintenant on peut trouver l'élément
bubbles = driver.find_elements(By.CSS_SELECTOR, ".message-user")
```

**Timeout** : Si l'élément n'apparaît pas dans le délai, erreur `TimeoutException`.

---

### 2.6 Mode headless (sans interface)

**Problème** : Sur GitHub Actions, pas d'écran disponible → Chrome crash.

**Solution** : Mode headless (Chrome s'exécute sans fenêtre graphique).

```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")          # Pas d'interface
options.add_argument("--no-sandbox")        # Sécurité Linux
options.add_argument("--disable-dev-shm-usage")  # Mémoire partagée

driver = webdriver.Chrome(service=service, options=options)
```

**Détection automatique CI** : Vérifier variable d'environnement `CI`.

```python
if os.environ.get("CI") == "true":
    options.add_argument("--headless")
```

**Sur GitHub Actions**, `CI=true` est toujours défini automatiquement.

---

### 2.7 Chemin dynamique vers HTML

**Problème** : Chemin absolu hard-codé (`C:\Dev\...`) ne marche pas sur Linux.

**Solution** : Calculer le chemin dynamiquement avec `os.path`.

```python
import os

# Chemin du fichier test_frontend.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Remonter au dossier racine, puis frontend/index.html
html_path = os.path.join(current_dir, '..', 'frontend', 'index.html')

# Convertir en URL file:/// (remplacer \ par /)
html_url = f"file:///{os.path.abspath(html_path).replace(os.sep, '/')}"

driver.get(html_url)
```

**Résultat** : Marche sur Windows (`\`) et Linux (`/`).

---

## 3. GitHub Actions (CI/CD)

### 3.1 Qu'est-ce que GitHub Actions ?

**GitHub Actions** = robot GitHub qui exécute des commandes automatiquement.

**Déclencheurs** :

- À chaque `git push`
- À chaque Pull Request
- Sur un planning (cron)
- Manuellement

**Cas d'usage** :

- Lancer les tests automatiquement
- Déployer une application
- Publier une release

---

### 3.2 Structure workflow YAML

```yaml
name: Tests # Nom du workflow

on: # Quand lancer ?
  push:
    branches: [main, feature/*]
  pull_request:
    branches: [main]

jobs: # Liste des jobs
  backend: # Job 1 : Tests backend
    runs-on: ubuntu-latest # Machine virtuelle Ubuntu

    steps: # Étapes du job
      - name: Checkout code # Télécharger le code
        uses: actions/checkout@v4

      - name: Setup Python # Installer Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install deps # Installer dépendances
        run: |
          pip install fastapi uvicorn
          pip install pytest

      - name: Run tests # Lancer tests
        run: pytest tests/test_backend.py -v

  frontend: # Job 2 : Tests frontend
    runs-on: ubuntu-latest
    needs: backend # Attend que backend termine

    steps:
      # ... (mêmes étapes + Selenium)
```

---

### 3.3 Jobs et steps

**Job** = tâche complète (ex: tester backend).  
**Step** = étape d'un job (ex: installer Python).

**Ordre d'exécution** :

1. Jobs **indépendants** s'exécutent en **parallèle**
2. Jobs avec `needs:` s'exécutent **après** le job spécifié

```yaml
jobs:
  backend:
    # Exécuté en premier

  frontend:
    needs: backend # Exécuté APRÈS backend
```

---

### 3.4 Actions GitHub officielles

**Actions** = modules réutilisables pour tâches courantes.

```yaml
# Télécharger code du repo
- uses: actions/checkout@v4

# Installer Python
- uses: actions/setup-python@v5
  with:
    python-version: "3.10"

# Installer Chrome pour Selenium
- uses: browser-actions/setup-chrome@v1
```

**Avantage** : Pas besoin de réinventer la roue (tout est pré-configuré).

---

### 3.5 Badge status

**Badge** = image dans README.md qui montre le status du workflow.

```markdown
![Tests](https://github.com/USER/REPO/actions/workflows/tests.yml/badge.svg)
```

**Résultat** :

- ✅ Badge vert si tests passent
- ❌ Badge rouge si tests échouent

**Utilité** : Rassure les contributeurs que le code fonctionne.

---

### 3.6 Variable d'environnement CI

**GitHub Actions** définit automatiquement `CI=true`.

**Utilisation** : Détecter si on est en CI/CD pour activer mode headless.

```python
if os.environ.get("CI") == "true":
    # On est sur GitHub Actions
    options.add_argument("--headless")
```

**Avantage** : Pas besoin de changer le code selon l'environnement.

---

## 4. Bonnes pratiques

### 4.1 Tests backend

✅ **DO** :

- Tester tous les endpoints importants
- Vérifier status codes (200, 404, 422, 500)
- Initialiser la base de données avant les tests
- Utiliser `TestClient` (pas de serveur externe)

❌ **DON'T** :

- Faire appel à des services externes (LLM, API) dans les tests
- Modifier la base de données de production
- Oublier de vérifier les réponses JSON

---

### 4.2 Tests frontend

✅ **DO** :

- Utiliser `WebDriverWait` pour attendre les éléments
- Mode headless en CI/CD
- Fermer le driver avec `driver.quit()` à chaque fois
- Vérifier les IDs/classes CSS réels

❌ **DON'T** :

- Utiliser `time.sleep()` partout (préférer `WebDriverWait`)
- Hard-coder les chemins absolus
- Oublier de lancer le backend avant les tests Selenium

---

### 4.3 GitHub Actions

✅ **DO** :

- Séparer jobs backend et frontend
- Installer seulement les dépendances nécessaires
- Utiliser des actions officielles (checkout, setup-python)
- Tester localement avant de push

❌ **DON'T** :

- Installer `requirements.txt` si contient dépendances Windows-only
- Lancer Selenium sans mode headless
- Oublier d'initialiser la base de données

---

### 4.4 Debugging tests

**Test échoue localement** :

1. Lire le message d'erreur complet
2. Vérifier que le backend est lancé (Selenium)
3. Vérifier les IDs/classes CSS (DevTools F12)
4. Augmenter le timeout si nécessaire

**Test échoue sur GitHub Actions** :

1. Vérifier les logs du workflow
2. Vérifier que toutes les dépendances sont installées
3. Vérifier le mode headless (Selenium)
4. Vérifier la compatibilité Linux (chemins, dépendances)

---

## 📊 Comparaison tests backend vs frontend

| Critère         | Tests backend (pytest) | Tests frontend (Selenium)        |
| --------------- | ---------------------- | -------------------------------- |
| **Vitesse**     | ⚡ Très rapide (~1s)   | 🐢 Lent (~10-30s)                |
| **Fiabilité**   | ✅ Très fiable         | ⚠️ Parfois instable              |
| **Maintenance** | ✅ Facile              | ⚠️ Moyenne (IDs CSS changent)    |
| **CI/CD**       | ✅ Toujours            | ⚠️ Optionnel (headless requis)   |
| **Coût**        | 💰 Gratuit             | 💰💰 Consomme plus de ressources |

**Recommandation** : Privilégier tests backend (rapides, fiables). Tests frontend = bonus pour vérifier UI critique.

---

## 🔗 Ressources utiles

- **pytest** : https://docs.pytest.org/
- **Selenium** : https://www.selenium.dev/documentation/
- **GitHub Actions** : https://docs.github.com/actions
- **FastAPI Testing** : https://fastapi.tiangolo.com/tutorial/testing/

---

_Dernière mise à jour : 2026-01-17_
