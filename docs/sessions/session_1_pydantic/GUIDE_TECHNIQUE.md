# Guide Technique — Session 1 : Pydantic

> Documentation technique détaillée pour retrouver rapidement les informations.

---

## 📋 Table des matières

1. [Concepts Pydantic](#concepts-pydantic)
2. [Syntaxe détaillée](#syntaxe-détaillée)
3. [Erreurs courantes](#erreurs-courantes)
4. [Exemples pratiques](#exemples-pratiques)
5. [Aide-mémoire](#aide-mémoire)

---

## 🎓 Concepts Pydantic

### Qu'est-ce que Pydantic ?

Pydantic est une **bibliothèque Python** qui permet de :

- **Valider** automatiquement les données
- **Définir des modèles** (structures de données)
- **Convertir** les types automatiquement
- **Générer** de la documentation automatique

### Pourquoi utiliser Pydantic ?

**Sans Pydantic :**

```python
@app.post("/message")
def recevoir_message(data: dict):
    # Tu dois tout vérifier manuellement
    if "texte" not in data:
        return {"erreur": "texte manquant"}
    if not isinstance(data["texte"], str):
        return {"erreur": "texte doit être un texte"}
    if len(data["texte"]) == 0:
        return {"erreur": "texte ne peut pas être vide"}
    # ... etc
```

**Avec Pydantic :**

```python
class Message(BaseModel):
    texte: str

@app.post("/message")
def recevoir_message(msg: Message):
    # Tout est déjà vérifié automatiquement !
    return {"texte": msg.texte}
```

---

## 📝 Syntaxe détaillée

### Importer Pydantic

```python
from pydantic import BaseModel
```

### Créer un modèle (classe)

```python
class NomDuModele(BaseModel):
    champ1: type
    champ2: type = valeur_defaut
```

**Exemples :**

```python
# Modèle simple
class Personne(BaseModel):
    nom: str
    age: int

# Modèle avec champ facultatif
class Livre(BaseModel):
    titre: str
    auteur: str = "Inconnu"  # Facultatif avec défaut

# Modèle avec plusieurs types
class Produit(BaseModel):
    nom: str
    prix: float
    en_stock: bool
    quantite: int = 0
```

### Utiliser un modèle dans un endpoint

```python
@app.post("/chemin")
def nom_fonction(variable: NomModele):
    # variable.champ1 pour accéder aux données
    return {"resultat": variable.champ1}
```

---

## 🔧 Types Python courants

| Type Python | Description         | Exemple             |
| ----------- | ------------------- | ------------------- |
| `str`       | Texte               | `"Bonjour"`         |
| `int`       | Nombre entier       | `42`                |
| `float`     | Nombre décimal      | `3.14`              |
| `bool`      | Booléen (vrai/faux) | `True` ou `False`   |
| `list`      | Liste               | `[1, 2, 3]`         |
| `dict`      | Dictionnaire        | `{"cle": "valeur"}` |

### Exemples de déclaration

```python
class Exemple(BaseModel):
    texte: str           # Champ obligatoire
    nombre: int          # Champ obligatoire
    prix: float = 0.0    # Facultatif, défaut = 0.0
    actif: bool = True   # Facultatif, défaut = True
```

---

## ⚠️ Erreurs courantes

### Erreur 1 : Confusion `=` et `:`

```python
# ❌ FAUX
class Message(BaseModel):
    texte = str  # Assigne la valeur "str"

# ✅ CORRECT
class Message(BaseModel):
    texte: str   # Déclare le type str
```

### Erreur 2 : Oublier le paramètre dans la fonction

```python
# ❌ FAUX
@app.post("/message")
def recevoir_message():  # Pas de paramètre
    return {"erreur": "Où sont les données ?"}

# ✅ CORRECT
@app.post("/message")
def recevoir_message(msg: Message):  # Reçoit le modèle
    return {"texte": msg.texte}
```

### Erreur 3 : Accéder aux champs incorrectement

```python
# ❌ FAUX
def recevoir_message(msg: Message):
    return {"texte": msg["texte"]}  # Syntaxe dictionnaire

# ✅ CORRECT
def recevoir_message(msg: Message):
    return {"texte": msg.texte}  # Syntaxe objet
```

### Erreur 4 : Utiliser `;` au lieu de `,` dans les dictionnaires

```python
# ❌ FAUX
return {"a": 1; "b": 2}  # Point-virgule interdit

# ✅ CORRECT
return {"a": 1, "b": 2}  # Virgule en Python
```

---

## 💡 Exemples pratiques

### Exemple 1 : Modèle utilisateur

```python
class Utilisateur(BaseModel):
    nom: str
    email: str
    age: int = 18  # Défaut = 18

@app.post("/creer-utilisateur")
def creer_utilisateur(user: Utilisateur):
    return {
        "message": f"Utilisateur {user.nom} créé",
        "email": user.email,
        "age": user.age
    }
```

**Test :**

```json
{
  "nom": "Alice",
  "email": "alice@exemple.com"
}
```

**Résultat :**

```json
{
  "message": "Utilisateur Alice créé",
  "email": "alice@exemple.com",
  "age": 18
}
```

### Exemple 2 : Modèle avec validation

```python
from pydantic import BaseModel, Field

class Note(BaseModel):
    titre: str
    contenu: str
    important: bool = False

@app.post("/note")
def ajouter_note(note: Note):
    priorite = "URGENT" if note.important else "Normal"
    return {
        "titre": note.titre,
        "priorite": priorite,
        "longueur": len(note.contenu)
    }
```

---

## 📚 Aide-mémoire rapide

### Syntaxe de base

```python
# Import
from pydantic import BaseModel

# Créer modèle
class MonModele(BaseModel):
    champ_obligatoire: str
    champ_facultatif: int = 0

# Utiliser dans endpoint
@app.post("/route")
def ma_fonction(data: MonModele):
    valeur = data.champ_obligatoire  # Accès
    return {"resultat": valeur}
```

### Valeurs par défaut courantes

```python
class Exemple(BaseModel):
    texte: str = ""           # Chaîne vide
    nombre: int = 0           # Zéro
    prix: float = 0.0         # Zéro décimal
    actif: bool = False       # Faux
    liste: list = []          # Liste vide
    optionnel: str = None     # Aucune valeur
```

### Opérateur `or` pour valeurs par défaut

```python
# Si valeur est None, utiliser "défaut"
resultat = valeur or "défaut"

# Exemples
nom = None or "Anonyme"     # → "Anonyme"
nom = "Alice" or "Anonyme"  # → "Alice"
age = 0 or 18               # → 18 (0 est "faux")
age = 25 or 18              # → 25
```

---

## 🔍 Messages d'erreur Pydantic

### Champ manquant

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "nom_du_champ"],
      "msg": "Field required"
    }
  ]
}
```

**Signification :** Un champ obligatoire est manquant.

### Type incorrect

```json
{
  "detail": [
    {
      "type": "string_type",
      "loc": ["body", "age"],
      "msg": "Input should be a valid string"
    }
  ]
}
```

**Signification :** Le type envoyé ne correspond pas au type attendu.

---

## 🧪 Commandes de test

```powershell
# Activer environnement virtuel
venv\Scripts\Activate.ps1

# Lancer serveur
uvicorn backend.main:app --reload

# Tester avec curl (PowerShell)
Invoke-WebRequest -Uri "http://127.0.0.1:8000/ping" -Method GET

# Tester POST avec curl (PowerShell)
$body = @{texte="Test"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:8000/message" -Method POST -Body $body -ContentType "application/json"
```

**Meilleure méthode :** Utiliser `/docs` dans le navigateur pour tester interactivement.

---

## 📖 Ressources supplémentaires

- [Documentation officielle Pydantic](https://docs.pydantic.dev/)
- [FastAPI + Pydantic Tutorial](https://fastapi.tiangolo.com/tutorial/body/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

## 🎯 Checklist de révision

Avant de passer à la session suivante, tu dois savoir :

- [ ] Importer `BaseModel` depuis `pydantic`
- [ ] Créer une classe qui hérite de `BaseModel`
- [ ] Déclarer un champ obligatoire avec `:`
- [ ] Déclarer un champ facultatif avec `= valeur`
- [ ] Utiliser un modèle dans un endpoint POST
- [ ] Accéder aux champs avec `objet.champ`
- [ ] Comprendre les messages d'erreur de validation

---

**Date de dernière mise à jour :** 2026-01-08
