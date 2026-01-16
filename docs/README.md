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

### Session 3 — Intégration LLM API

**Objectifs :**

- Comprendre ce qu'est une API LLM
- Créer un module `ai.py` pour appeler GitHub Models (GPT-4o)
- Gérer les secrets avec `.env` et `python-dotenv`
- Créer un endpoint POST `/chat` pour discuter avec le LLM
- Modifier `memory.py` pour supporter les rôles (user/assistant)
- Sauvegarder les conversations dans SQLite

👉 [Accéder à la Session 3](sessions/session_3_llm/README.md)

---

### Session 4 — Frontend Interactif

**Objectifs :**

- Comprendre `fetch()` en JavaScript
- Créer une interface HTML simple (input + bouton)
- Gérer les événements (clic, touche Entrée)
- Afficher la conversation en temps réel
- Configurer CORS dans FastAPI

👉 [Accéder à la Session 4](sessions/session_4_frontend/README.md)

---

### Session 5 — CSS & Design Moderne

**Objectifs :**

- Comprendre Flexbox (layout moderne)
- Créer des bulles de messages stylisées (user/assistant)
- Ajouter des animations CSS (apparition, hover)
- Optimiser le JavaScript avec `createElement()`
- Ajouter des délais naturels avec `setTimeout()`

👉 [Accéder à la Session 5](sessions/session_5_css/README.md)

---

### Session 6 — Améliorations UX

**Objectifs :**

- Ajouter auto-scroll automatique vers nouveaux messages
- Gérer les erreurs avec messages polis
- Créer un bouton Clear pour vider la conversation
- Désactiver le bouton pendant traitement
- Améliorer l'expérience utilisateur globale

👉 [Accéder à la Session 6](sessions/session_6_ux/README.md)

---

### Session 7 — Dark Mode

**Objectifs :**

- Créer variables CSS réutilisables
- Implémenter un switch dark mode avec animation
- Sauvegarder préférence utilisateur avec localStorage
- Adapter toutes les couleurs aux 2 thèmes
- Améliorer accessibilité et confort visuel

👉 [Accéder à la Session 7](sessions/session_7_darkmode/README.md)

---

## 🧭 Comment utiliser cette doc

1. **Lis dans l'ordre des sessions** si tu débutes
2. Chaque session contient :
   - Un **README.md** avec les objectifs et résumé
   - Un **GUIDE_TECHNIQUE.md** avec les détails et explications
   - Un dossier **scripts/** avec le code final de la session

---

_Dernière mise à jour : 2026-01-16 (Session 7)_
