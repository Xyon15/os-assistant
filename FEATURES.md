# 🚀 Features & Roadmap

> Liste des fonctionnalités implémentées et futures pour Workly (ex OS Assistant)

**Status actuel :** v1.2.0 (Session 12 terminée) ✅  
**Date :** 2026-02-26

---

## 📊 Priorités

- 🔴 **Haute** : Améliore significativement l'expérience utilisateur
- 🟡 **Moyenne** : Fonctionnalité utile mais pas critique
- 🟢 **Basse** : Nice-to-have, peut attendre

---

## ✅ Fonctionnalités implémentées

### Session 5 — Design & UX (CSS) ✅

- Bulles de chat modernes (user bleu / assistant gris)
- Layout Flexbox, animations fadeIn + hover

### Session 6 — UX avancée ✅

- Auto-scroll, gestion erreurs `.catch()`, bouton Clear
- Désactivation bouton pendant traitement

### Session 7 — Dark Mode ✅

- Variables CSS `:root`, switch toggle, persistance localStorage

### Session 8 — Tests & CI/CD ✅

- pytest backend + Selenium frontend + GitHub Actions (8/8 tests)

### Session 9 — Déploiement production ✅

- Backend Render + Frontend GitHub Pages + domaine personnalisé
- Tag v1.0.0-stable

### Session 10 — Monitoring & PostgreSQL ✅

- Migration SQLite → PostgreSQL (Supabase)
- Endpoints /health, /metrics, /stats
- Logs persistants, monitoring UptimeRobot

### Session 11 — Authentification JWT (backend) ✅

- Table users PostgreSQL (username, email, hashed_password)
- Module auth.py (bcrypt, JWT create/verify)
- Endpoints /register, /login
- Protection /chat via `Depends(get_current_user)`

### Session 12 — Frontend auth + refonte UI ✅

- Page login/register (formulaires avec onglets)
- JWT stocké localStorage, Authorization: Bearer sur /chat
- GET /me : vérification token au démarrage
- Détection doublons username/email (e.pgcode psycopg2)
- Refonte UI : layout sidebar + zone chat, suppression header
- Style Inter + accent violet #8A05FF
- URLs propres sans .html (/login/, /)

---

## 🎯 Prochaines fonctionnalités

### 🔴 Haute priorité

- [ ] **Vérification email** : envoi d'un email de confirmation à l'inscription
- [ ] **Historique conversations** : sauvegarder les messages par utilisateur en DB
- [ ] **Responsive mobile** : sidebar hamburger, layout adaptatif
- [ ] **Validation mot de passe** : longueur min, complexité, confirmation
- [ ] **Rate limiting** : limiter le nombre de requêtes par utilisateur

### 🟡 Moyenne priorité

- [ ] **Multi-conversations** : créer/switcher entre conversations dans la sidebar
- [ ] **Choix du modèle LLM** : sélecteur GPT-4o / Claude / Llama
- [ ] **Contexte système personnalisable** : prompt système éditable par l'utilisateur
- [ ] **Profil utilisateur** : page settings (changer mot de passe, email)
- [ ] **Export conversation** : télécharger en PDF/TXT

### 🟢 Basse priorité

- [ ] **Reconnaissance vocale** : dictée via Web Speech API
- [ ] **Synthèse vocale** : lecture des réponses
- [ ] **PWA** : Progressive Web App (installable)
- [ ] **Notifications desktop**
- [ ] **Dashboard stats** : page analytics avec graphiques
- [ ] **WebSocket** : réponses en temps réel (streaming)

### ⚙️ Optimisations

- [ ] Cache des réponses LLM
- [ ] Pagination de l'historique
- [ ] Compression des messages longs

---

## 🎯 Roadmap

### Phase 1 — Fondations (v0.1.0 → v1.0.0) ✅

1. ✅ Backend FastAPI + LLM API
2. ✅ Frontend HTML/CSS/JS avec chat
3. ✅ Dark mode + UX améliorée
4. ✅ Tests CI/CD + déploiement production

### Phase 2 — Sécurité & Auth (v1.1.0 → v1.2.0) ✅

1. ✅ PostgreSQL + monitoring
2. ✅ Authentification JWT (backend + frontend)
3. ✅ Refonte UI sidebar + design système violet

### Phase 3 — Productivité (v1.3.0) — En cours

1. ⏸️ Historique conversations par utilisateur
2. ⏸️ Multi-conversations (sidebar)
3. ⏸️ Responsive mobile
4. ⏸️ Vérification email

### Phase 4 — Application complète (v2.0.0)

1. ⏸️ Choix du modèle LLM
2. ⏸️ Profil utilisateur / settings
3. ⏸️ PWA + notifications
4. ⏸️ Streaming WebSocket

---

_Dernière mise à jour : 2026-02-26 (Session 12)_
