# 📖 Documentation — OS Assistant

> Guide complet pour comprendre et développer OS Assistant

---

## 🎯 À propos de cette documentation

Cette documentation suit ton apprentissage **session par session**. Chaque session couvre un concept ou une fonctionnalité spécifique.

---

## 🗺️ Navigation

- **[INDEX.md](INDEX.md)** : Sommaire de toutes les sessions
- **[sessions/](sessions/)** : Dossier contenant la documentation détaillée de chaque session

---

## 📚 Sessions disponibles

### Session 0 — Setup & Premier serveur FastAPI

**Objectifs :**

- Comprendre ce qu'est une API
- Structurer le projet
- Créer un endpoint `/ping` avec FastAPI
- Tester localement avec `uvicorn`

👉 [Accéder à la Session 0](sessions/session_0_setup/README.md)

---

### Session 1 — Validation avec Pydantic

**Objectifs :**

- Comprendre Pydantic et la validation automatique
- Créer un modèle de données `Message`
- Créer un endpoint POST `/message`
- Valider les entrées utilisateur automatiquement

👉 [Accéder à la Session 1](sessions/session_1_pydantic/README.md)

---

### Session 2 — Persistance avec SQLite

**Objectifs :**

- Comprendre SQLite (base de données persistante)
- Créer un module `memory.py` pour gérer la DB
- Sauvegarder et récupérer des messages
- Intégrer SQLite dans FastAPI avec lifespan

👉 [Accéder à la Session 2](sessions/session_2_sqlite/README.md)

---

## 🧭 Comment utiliser cette doc

1. **Lis dans l'ordre des sessions** si tu débutes
2. Chaque session contient :
   - Un **README.md** avec les objectifs et résumé
   - Un **GUIDE_TECHNIQUE.md** avec les détails et explications
   - Un dossier **scripts/** avec le code final de la session

---

_Dernière mise à jour : 2026-01-08 (Session 2)_
