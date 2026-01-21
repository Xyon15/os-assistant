# GUIDE TECHNIQUE — Session 9 (Déploiement)

## Backend (Render)

- Start command : `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
- Build command : `pip install -r requirements.txt`
- Health check path : `/ping`
- Variables importantes : `GITHUB_TOKEN`, (optionnel) `SENTRY_DSN`
- Fichier `.python-version` : `3.11.0` (pour compatibilité Render)

## Frontend (GitHub Pages)

- Publier le contenu statique dans `/docs` ou via branche `gh-pages`.
- URL : `https://xyon15.github.io/os-assistant/`
- CORS : mettre `https://xyon15.github.io` dans `ALLOWED_ORIGINS` et autoriser `null` pour tests locaux

## Monitoring

- UptimeRobot : monitor `/ping` (should contain `pong`) et page frontend (should contain `Envoyer`)
- Intervalle recommandé : 5 minutes

## Notes

- Pour un déploiement ultérieur avec persistance, remettre `initialiser_db()` au lifespan et activer migrations
- Ajouter Sentry pour capturer erreurs 500 et stack traces si nécessaire

---

_Dernière mise à jour : 2026-01-21_
