# 📚 Index — OS Assistant

> Documentation complète du projet OS Assistant

---

## 📖 Sessions documentées

- [Session 0 — Setup & Premier serveur FastAPI](sessions/session_0_setup/README.md) ✅
- [Session 1 — Validation avec Pydantic](sessions/session_1_pydantic/README.md) ✅
- [Session 2 — Persistance avec SQLite](sessions/session_2_sqlite/README.md) ✅
- [Session 3 — Intégration LLM API](sessions/session_3_llm/README.md) ✅
- [Session 4 — Frontend Interactif](sessions/session_4_frontend/README.md) ✅
- [Session 5 — CSS & Design Moderne](sessions/session_5_css/README.md) ✅
- [Session 6 — Améliorations UX](sessions/session_6_ux/README.md) ✅

---

## 🗂️ Organisation

- **INDEX.md** (ce fichier) : Sommaire général de toute la documentation
- **README.md** : Vue d'ensemble et guide de navigation
- **sessions/** : Documentation détaillée de chaque session d'apprentissage

---

## 📅 Historique

| Session | Date       | Sujet                    | Status     |
| ------- | ---------- | ------------------------ | ---------- |
| 0       | 2026-01-08 | Setup & /ping endpoint   | ✅ Terminé |
| 1       | 2026-01-08 | Validation avec Pydantic | ✅ Terminé |
| 2       | 2026-01-08 | Persistance avec SQLite  | ✅ Terminé |
| 3       | 2026-01-09 | Intégration LLM API      | ✅ Terminé |
| 4       | 2026-01-09 | Frontend Interactif      | ✅ Terminé |
| 5       | 2026-01-13 | CSS & Design Moderne     | ✅ Terminé |
| 6       | 2026-01-14 | Améliorations UX         | ✅ Terminé |

---

## 🎓 Concepts appris

### Session 0

- API REST et modèle client/serveur
- FastAPI et décorateurs Python
- Dictionnaires Python et JSON
- requirements.txt et pip
- uvicorn et serveur ASGI

### Session 1

- Pydantic et BaseModel
- Validation automatique des données
- Modèles de données (classes)
- Champs obligatoires et facultatifs
- Endpoint POST avec validation

### Session 2

- SQLite et bases de données relationnelles
- Persistance des données (fichier memory.db)
- SQL : CREATE TABLE, INSERT INTO, SELECT
- Sécurité avec placeholders `?`
- Lifespan FastAPI (@asynccontextmanager)
- Transformation tuples → dictionnaires
- Endpoint GET /messages

### Session 3

- API LLM et appels HTTP avec `requests`
- GitHub Models (GPT-4o gratuit pour étudiants)
- Fichier `.env` et gestion des secrets
- `python-dotenv` pour variables d'environnement
- `try/except` et gestion d'erreurs robuste
- Pattern de réessai avec `time.sleep()`
- Rôles conversationnels (user/assistant)
- Endpoint POST /chat

### Session 4

- `fetch()` JavaScript pour requêtes HTTP
- `addEventListener()` pour événements (clic, touche)
- `innerHTML` pour modifier le DOM
- Promesses JavaScript et `.then()`
- CORS (Cross-Origin Resource Sharing)
- Middleware FastAPI
- Séparation HTML / JavaScript (bonnes pratiques)
- Gestion événements navigateur

### Session 5

- Flexbox CSS (`display: flex`, `flex-direction`, `justify-content`, `align-items`)
- Animations CSS (`@keyframes`, `animation`, `transition`)
- Pseudo-classes (`:hover`)
- `createElement()` et `appendChild()` (DOM moderne)
- `setTimeout()` pour délais naturels
- Bulles de chat stylisées (alignment, border-radius, box-shadow)
- Code commenté professionnellement

### Session 6

- Auto-scroll JavaScript (`scrollTop`, `scrollHeight`)
- Gestion erreurs Promesses (`.catch()`)
- Messages d'erreur utilisateur polis
- Manipulation DOM (`innerHTML = ""`)
- Désactivation boutons (`disabled`)
- Pseudo-classe CSS (`:disabled`)
- Flexbox avancé (`justify-content: space-between`, `flex: 1`)
- Pattern UX : Désactiver → Traiter → Réactiver

---

_Dernière mise à jour : 2026-01-14_
