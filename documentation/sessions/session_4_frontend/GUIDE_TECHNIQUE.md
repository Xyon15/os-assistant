# Guide Technique — Session 4 : Frontend Interactif

> **Explications ligne par ligne** du code HTML et JavaScript  
> **Date :** 2026-01-09

---

## 📄 Fichier : `frontend/index.html`

### **Structure HTML complète**

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Assistant IA</title>
  </head>
  <body>
    <h1>Assistant IA</h1>
    <p>Interface prête</p>
    <div id="conversation"></div>

    <div>
      <input
        id="messageInput"
        type="text"
        placeholder="Tapez votre message ici..."
      />
      <button id="envoyerBtn">Envoyer</button>
    </div>

    <script src="app.js"></script>
  </body>
</html>
```

### **Explication ligne par ligne**

#### **Ligne 1-2 : Déclaration HTML**

```html
<!DOCTYPE html>
<html></html>
```

- `<!DOCTYPE html>` = Dire au navigateur "ceci est du HTML5"
- `<html>` = Balise racine (tout le contenu est dedans)

#### **Ligne 3-6 : En-tête (head)**

```html
<head>
  <meta charset="UTF-8" />
  <title>Assistant IA</title>
</head>
```

- `<head>` = Métadonnées (pas affichées à l'écran)
- `<meta charset="UTF-8">` = Encodage des caractères (pour accents français)
- `<title>` = Titre de l'onglet du navigateur

#### **Ligne 7-9 : Titre et sous-titre**

```html
<body>
  <h1>Assistant IA</h1>
  <p>Interface prête</p>
</body>
```

- `<body>` = Corps de la page (tout ce qui est affiché)
- `<h1>` = Titre principal (gros et gras)
- `<p>` = Paragraphe de texte

#### **Ligne 10 : Zone de conversation**

```html
<div id="conversation"></div>
```

- `<div>` = Conteneur vide (pour le moment)
- `id="conversation"` = Identifiant unique (pour le retrouver en JavaScript)
- **Analogie :** C'est comme un tableau blanc vide où on va écrire les messages

#### **Ligne 12-15 : Zone de saisie + Bouton**

```html
<div>
  <input
    id="messageInput"
    type="text"
    placeholder="Tapez votre message ici..."
  />
  <button id="envoyerBtn">Envoyer</button>
</div>
```

- `<input type="text">` = Zone de texte (comme un champ de formulaire)
- `id="messageInput"` = Identifiant pour le retrouver en JavaScript
- `placeholder="..."` = Texte grisé affiché quand le champ est vide
- `<button>` = Bouton cliquable
- `id="envoyerBtn"` = Identifiant du bouton

#### **Ligne 17 : Charger le JavaScript**

```html
<script src="app.js"></script>
```

- `<script src="app.js">` = Charger le fichier JavaScript externe
- Le code JavaScript s'exécute après le chargement du HTML

---

## 📄 Fichier : `frontend/app.js`

### **Code JavaScript complet**

```javascript
// 1. Récupérer les éléments HTML
const bouton = document.getElementById("envoyerBtn");
const input = document.getElementById("messageInput");
const conversation = document.getElementById("conversation");

// 2. Fonction pour envoyer le message
function envoyerMessage() {
  // Récupérer le texte tapé
  const texte = input.value.trim();

  // Ne rien faire si le message est vide
  if (texte === "") {
    return;
  }

  // Afficher le message de l'utilisateur
  conversation.innerHTML += "<p><strong>User:</strong> " + texte + "</p>";

  // Afficher "est en train d'écrire..."
  conversation.innerHTML +=
    "<p id='chargement'><em>Assistant est en train d'écrire...</em></p>";

  // Vider l'input
  input.value = "";

  // Envoyer au backend
  fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: texte }),
  })
    .then((reponse) => reponse.json())
    .then((donnees) => {
      // Enlever le message de chargement
      const messageChargement = document.getElementById("chargement");
      if (messageChargement) {
        messageChargement.remove();
      }

      // Afficher la réponse de l'assistant
      conversation.innerHTML +=
        "<p><strong>Assistant:</strong> " + donnees.reponse + "</p>";
    });
}

// 3. Écouter le clic sur le bouton
bouton.addEventListener("click", envoyerMessage);

// 4. Écouter la touche Entrée
input.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    envoyerMessage();
  }
});
```

---

## 🔍 Explication détaillée

### **Partie 1 : Récupérer les éléments HTML (lignes 2-4)**

```javascript
const bouton = document.getElementById("envoyerBtn");
const input = document.getElementById("messageInput");
const conversation = document.getElementById("conversation");
```

**Explication :**

- `document` = La page HTML entière
- `.getElementById("envoyerBtn")` = "Va chercher l'élément HTML qui a l'`id` 'envoyerBtn'"
- `const bouton = ...` = Stocke cet élément dans une variable `bouton`

**Analogie :** C'est comme si tu cherchais 3 objets dans une pièce :

- Le bouton "Envoyer"
- La zone de texte
- Le tableau blanc (zone conversation)

---

### **Partie 2 : Fonction envoyerMessage() (lignes 7-40)**

#### **2.1 Récupérer le texte (ligne 9)**

```javascript
const texte = input.value.trim();
```

- `input.value` = Le texte tapé dans le champ
- `.trim()` = Enlever les espaces avant/après (ex: `"  Bonjour  "` → `"Bonjour"`)

#### **2.2 Vérifier si vide (lignes 12-14)**

```javascript
if (texte === "") {
  return;
}
```

- Si `texte` est vide (`""`), arrêter la fonction (`return`)
- Empêche d'envoyer des messages vides

#### **2.3 Afficher le message User (ligne 17)**

```javascript
conversation.innerHTML += "<p><strong>User:</strong> " + texte + "</p>";
```

- `conversation.innerHTML` = Le contenu HTML de la zone conversation
- `+=` = Ajouter à la fin (comme `append()` en Python)
- `"<p><strong>User:</strong> " + texte + "</p>"` = Créer un paragraphe HTML

**Exemple :** Si `texte = "Bonjour"`, cela crée :

```html
<p><strong>User:</strong> Bonjour</p>
```

#### **2.4 Afficher message de chargement (ligne 20)**

```javascript
conversation.innerHTML +=
  "<p id='chargement'><em>Assistant est en train d'écrire...</em></p>";
```

- Ajoute un paragraphe avec `id='chargement'` (pour le retrouver plus tard)
- `<em>` = Texte en italique

#### **2.5 Vider l'input (ligne 23)**

```javascript
input.value = "";
```

- Efface le texte dans la zone de saisie
- Permet de taper le prochain message immédiatement

#### **2.6 Envoyer au backend avec fetch() (lignes 26-29)**

```javascript
fetch("http://127.0.0.1:8000/chat", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ message: texte }),
});
```

**Décomposition :**

- `fetch("http://...")` = Envoyer une requête HTTP (comme `requests.post()` en Python)
- `method: "POST"` = Type de requête (POST pour envoyer des données)
- `headers: {"Content-Type": "application/json"}` = Dire au serveur "j'envoie du JSON"
- `body: JSON.stringify({message: texte})` = Transformer `{message: "Bonjour"}` en texte JSON

**Analogie :** C'est comme appeler ton backend au téléphone et lui dire :

> "Salut ! J'ai un message : 'Bonjour'. Peux-tu le traiter ?"

#### **2.7 Traiter la réponse (lignes 30-39)**

```javascript
.then(reponse => reponse.json())
.then(donnees => {
    // ...
});
```

**Explication `.then()` :**

- `.then()` = "Quand tu auras la réponse, fais ceci"
- C'est une **promesse** : le code attend la réponse du serveur

**Ligne 30 :** `reponse => reponse.json()`

- Transformer la réponse HTTP en objet JavaScript
- `reponse.json()` retourne une nouvelle promesse

**Lignes 32-35 :** Enlever le message de chargement

```javascript
const messageChargement = document.getElementById("chargement");
if (messageChargement) {
  messageChargement.remove();
}
```

- Retrouver l'élément avec `id='chargement'`
- Vérifier qu'il existe (`if (messageChargement)`)
- Le supprimer avec `.remove()`

**Ligne 38 :** Afficher la réponse

```javascript
conversation.innerHTML +=
  "<p><strong>Assistant:</strong> " + donnees.reponse + "</p>";
```

- `donnees.reponse` = La réponse du LLM (retournée par le backend)
- Ajoute un paragraphe "Assistant: [réponse]"

---

### **Partie 3 : Écouter le clic (ligne 43)**

```javascript
bouton.addEventListener("click", envoyerMessage);
```

**Explication :**

- `addEventListener("click", ...)` = "Quand on clique sur le bouton, fais ceci"
- `envoyerMessage` = La fonction à exécuter (sans parenthèses !)

**Analogie :** C'est comme mettre un détecteur de mouvement sur le bouton qui dit :

> "Dès que quelqu'un clique, appelle la fonction `envoyerMessage()`"

---

### **Partie 4 : Écouter la touche Entrée (lignes 46-50)**

```javascript
input.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    envoyerMessage();
  }
});
```

**Explication :**

- `addEventListener("keypress", ...)` = "Quand on appuie sur une touche dans l'input, fais ceci"
- `function(event)` = Fonction anonyme qui reçoit l'événement clavier
- `event.key` = La touche qui a été pressée
- `if (event.key === "Enter")` = Si la touche est "Entrée"
- `envoyerMessage()` = Appeler la fonction (avec parenthèses cette fois)

**Analogie :** C'est comme dire :

> "Si quelqu'un tape dans la zone de texte, vérifie quelle touche. Si c'est Entrée, envoie le message !"

---

## 🧪 Cas d'usage : Envoyer "Bonjour"

### **Étape 1 : Utilisateur tape "Bonjour" et clique sur Envoyer**

1. JavaScript détecte le clic (`addEventListener("click")`)
2. Appelle `envoyerMessage()`

### **Étape 2 : Fonction envoyerMessage() s'exécute**

1. Récupère `"Bonjour"` depuis l'input → `texte = "Bonjour"`
2. Vérifie que `texte` n'est pas vide → OK
3. Affiche `<p><strong>User:</strong> Bonjour</p>` dans la conversation
4. Affiche `<p id='chargement'><em>Assistant est en train d'écrire...</em></p>`
5. Vide l'input → champ vide maintenant
6. Envoie requête HTTP POST à `http://127.0.0.1:8000/chat` avec `{message: "Bonjour"}`

### **Étape 3 : Backend reçoit la requête**

1. FastAPI reçoit POST `/chat`
2. Appelle `demander_llm("Bonjour")`
3. GPT-4o génère une réponse (ex: "Bonjour ! Comment puis-je vous aider ?")
4. Backend retourne `{reponse: "Bonjour ! Comment puis-je vous aider ?"}`

### **Étape 4 : JavaScript reçoit la réponse**

1. `.then(reponse => reponse.json())` transforme la réponse en objet JavaScript
2. `.then(donnees => ...)` reçoit `donnees = {reponse: "Bonjour ! Comment puis-je vous aider ?"}`
3. Retrouve le message de chargement (`id='chargement'`)
4. Le supprime avec `.remove()`
5. Affiche `<p><strong>Assistant:</strong> Bonjour ! Comment puis-je vous aider ?</p>`

### **Résultat final dans la page :**

```
User: Bonjour
Assistant: Bonjour ! Comment puis-je vous aider ?
```

---

## 🔧 Modifications apportées au backend

### **Fichier : `backend/main.py`**

**Ajout du middleware CORS (lignes 14-15, 30-36)**

```python
# Import ajouté
from fastapi.middleware.cors import CORSMiddleware

# Middleware ajouté après app = FastAPI(...)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # "*" = autoriser TOUTES les origines (OK pour dev local)
    allow_credentials=True,  # Autoriser cookies/authentification
    allow_methods=["*"],  # Autoriser GET, POST, OPTIONS...
    allow_headers=["*"],  # Autoriser tous les headers HTTP
)
```

**Pourquoi c'est nécessaire ?**

Le navigateur effectue une **requête OPTIONS** (pre-flight) avant d'envoyer le POST pour vérifier si le backend autorise les requêtes depuis une autre origine (ex: `file://` ou `http://localhost:5500`).

Sans CORS, le navigateur bloque la requête avec l'erreur :

```
Access to fetch at 'http://127.0.0.1:8000/chat' from origin 'file://' has been blocked by CORS policy
```

**Analogie :** C'est comme un garde de sécurité qui vérifie si tu as l'autorisation d'entrer dans un bâtiment. Sans CORS, le garde dit "Non, tu n'es pas sur la liste !".

---

## 🐛 Problèmes rencontrés et solutions

### **Problème 1 : Page se recharge au clic**

**Cause :** Live Server rechargeait automatiquement la page.  
**Solution :** Ouvrir `index.html` directement (double-clic) sans Live Server.

### **Problème 2 : Erreur 405 Method Not Allowed (OPTIONS)**

**Cause :** CORS non configuré dans FastAPI.  
**Solution :** Ajouter middleware CORS dans `backend/main.py`.

### **Problème 3 : ERR_CONNECTION_REFUSED**

**Cause :** Backend uvicorn arrêté.  
**Solution :** Relancer `uvicorn backend.main:app --reload`.

---

## 📚 Comparaison Python vs JavaScript

| **Concept**          | **Python (backend)**            | **JavaScript (frontend)**                  |
| -------------------- | ------------------------------- | ------------------------------------------ |
| Envoyer requête HTTP | `requests.post(url, json=data)` | `fetch(url, {body: JSON.stringify(data)})` |
| Transformer en JSON  | `reponse.json()`                | `reponse.json()` (identique !)             |
| Boucle si erreur     | `for tentative in range(1, 4):` | Pas implémenté ici (optionnel)             |
| Afficher à l'écran   | `print(texte)`                  | `element.innerHTML += texte`               |

---

## 🎓 Points clés à retenir

1. **`fetch()` est asynchrone** : Le code continue pendant que la requête est en cours.
2. **`.then()` gère les promesses** : "Quand tu auras la réponse, fais ceci".
3. **`innerHTML` modifie le HTML** : Attention à ne pas supprimer les messages précédents (utiliser `+=` au lieu de `=`).
4. **CORS est obligatoire** : Dès que le frontend et le backend sont sur des origines différentes.
5. **Live Server peut interférer** : Préférer ouvrir le fichier directement pour éviter les rechargements intempestifs.

---

## 📝 Améliorations possibles (Session 5)

- Ajouter du CSS pour un design moderne (bulles de chat, couleurs)
- Afficher l'historique au chargement (GET `/messages`)
- Auto-scroll automatique vers le bas
- Gestion d'erreurs avec `.catch()`
- Désactiver le bouton pendant l'envoi (éviter double-clic)
