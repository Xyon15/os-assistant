/*
 * ========================================
 * LOGIN.JS — LOGIQUE DE LOGIN/REGISTER
 * ========================================
 * Gère l'interaction utilisateur avec le login et register :
 * Envoi requêtes au backend (/login, /register)
 * ========================================
 */


// === CONFIGURATION ===
const BACKEND_URL = window.location.hostname === "xyon15.github.io"
    ? "https://os-assistant-backend.onrender.com"
    : "http://localhost:8000";

// === ÉLÉMENTS HTML ===
const tabLogin    = document.getElementById("tab-login");
const tabRegister = document.getElementById("tab-register");
const formLogin   = document.getElementById("form-login");
const formRegister = document.getElementById("form-register");
const authMessage = document.getElementById("auth-message");

// === ONGLETS : switcher entre Login et Register ===
tabLogin.addEventListener("click", function() {
    formLogin.classList.remove("hidden");
    formRegister.classList.add("hidden");
    tabLogin.classList.add("active");
    tabRegister.classList.remove("active");
    authMessage.textContent = "";
});

tabRegister.addEventListener("click", function() {
    formRegister.classList.remove("hidden");
    formLogin.classList.add("hidden");
    tabRegister.classList.add("active");
    tabLogin.classList.remove("active");
    authMessage.textContent = "";
});

// === FORMULAIRE LOGIN ===
formLogin.addEventListener("submit", async function(event) {
    event.preventDefault();  // Empêche le rechargement de page

    const username = document.getElementById("login-username").value.trim();
    const password = document.getElementById("login-password").value.trim();

    // OAuth2 attend un FormData avec les champs "username" et "password"
    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);

    try {
        const reponse = await fetch(BACKEND_URL + "/login", {
            method: "POST",
            body: formData   // Pas de Content-Type header : le navigateur le gère seul
        });

        const donnees = await reponse.json();

        if (reponse.ok) {
            // Stocker le token + username (renvoyé par le backend) pour affichage dans le chat
            localStorage.setItem("token", donnees.access_token);
            localStorage.setItem("username", donnees.username);  // Renvoyé par le backend
            // Rediriger vers le chat
            window.location.href = "../";
        } else {
            authMessage.style.color = "red";
            authMessage.textContent = "❌ " + (donnees.detail || "Identifiants incorrects.");
        }
    } catch (erreur) {
        authMessage.style.color = "red";
        authMessage.textContent = "❌ Impossible de contacter le serveur.";
    }
});

// === FORMULAIRE REGISTER ===
formRegister.addEventListener("submit", async function(event) {
    event.preventDefault();

    const username = document.getElementById("register-username").value.trim();
    const email    = document.getElementById("register-email").value.trim();
    const password = document.getElementById("register-password").value.trim();

    try {
        const reponse = await fetch(BACKEND_URL + "/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username: username, email: email, password: password })
        });

        const donnees = await reponse.json();

        if (reponse.ok) {
            // Succès : afficher message vert et basculer sur l'onglet Login
            authMessage.style.color = "green";
            authMessage.textContent = "✅ Compte créé ! Connecte-toi maintenant.";
            tabLogin.click();  // Bascule sur l'onglet login automatiquement
        } else {
            authMessage.style.color = "red";
            // Pydantic renvoie detail comme tableau [{msg: "..."}], on extrait le message
            let errMsg = "Erreur lors de l'inscription.";
            if (typeof donnees.detail === "string") {
                errMsg = donnees.detail;
            } else if (Array.isArray(donnees.detail) && donnees.detail.length > 0) {
                // Pydantic renvoie des messages en anglais → on traduit les plus courants
                const msg = donnees.detail[0].msg || "";
                if (msg.includes("not a valid email")) {
                    errMsg = "Adresse email invalide. Vérifie le format (ex: nom@exemple.com).";
                } else {
                    errMsg = msg;
                }
            }
            authMessage.textContent = "❌ " + errMsg;
        }
    } catch (erreur) {
        authMessage.style.color = "red";
        authMessage.textContent = "❌ Impossible de contacter le serveur.";
    }
});