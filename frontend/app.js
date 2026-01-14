/*
 * ========================================
 * APP.JS — LOGIQUE DE CHAT
 * ========================================
 * Gère l'interaction utilisateur avec le chat :
 * 1. Récupération des éléments HTML
 * 2. Affichage des messages (user + assistant)
 * 3. Envoi requêtes au backend (/chat)
 * 4. Événements (clic bouton + touche Entrée)
 * ========================================
 */

// === 1. RÉCUPÉRATION DES ÉLÉMENTS HTML ===
const bouton = document.getElementById("envoyerBtn");
const input = document.getElementById("messageInput");
const conversation = document.getElementById("conversation");

// === 2. FONCTION PRINCIPALE : ENVOYER MESSAGE ===
// Appelée au clic bouton ou touche Entrée
function envoyerMessage() {
    // Récupérer et nettoyer le texte tapé
    const texte = input.value.trim();
    
    // Ne rien faire si le message est vide
    if (texte === "") {
        return;
    }
    
    // --- Afficher le message de l'utilisateur (bulle bleue à droite) ---
    const messageUser = document.createElement("p");
    messageUser.className = "message-user";
    const bulleUser = document.createElement("span");
    bulleUser.className = "bulle-user";
    bulleUser.textContent = texte;
    messageUser.appendChild(bulleUser);
    conversation.appendChild(messageUser);
    
    conversation.scrollTop = conversation.scrollHeight;
    
    // Vider l'input immédiatement
    input.value = "";
    
    // --- Attendre 400ms avant d'afficher "est en train d'écrire..." (effet naturel) ---
    setTimeout(function() {
        // Afficher message de chargement (bulle grise à gauche avec id pour suppression)
        const messageChargement = document.createElement("p");
        messageChargement.className = "message-assistant";
        messageChargement.id = "chargement";
        const bulleChargement = document.createElement("span");
        bulleChargement.className = "bulle-assistant";
        const texteChargement = document.createElement("em");
        texteChargement.textContent = "Assistant est en train d'écrire...";
        bulleChargement.appendChild(texteChargement);
        messageChargement.appendChild(bulleChargement);
        conversation.appendChild(messageChargement);
        conversation.scrollTop = conversation.scrollHeight;
        
        // --- Envoyer requête POST au backend ---
        fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({message: texte})
        })
        .then(reponse => reponse.json())
        .then(donnees => {
            // Enlever le message de chargement
            const messageChargement = document.getElementById("chargement");
            if (messageChargement) {
                messageChargement.remove();
            }
            
            // Afficher la réponse de l'assistant (bulle grise à gauche)
            const messageAssistant = document.createElement("p");
            messageAssistant.className = "message-assistant";
            const bulleAssistant = document.createElement("span");
            bulleAssistant.className = "bulle-assistant";
            bulleAssistant.textContent = donnees.reponse;
            messageAssistant.appendChild(bulleAssistant);
            conversation.appendChild(messageAssistant);
            conversation.scrollTop = conversation.scrollHeight;
        });
    }, 400); // Délai de 400ms pour effet naturel
}

// === 3. ÉVÉNEMENTS : ÉCOUTER INTERACTIONS UTILISATEUR ===

// Clic sur le bouton "Envoyer"
bouton.addEventListener("click", envoyerMessage);

// Touche "Entrée" dans l'input
input.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        envoyerMessage();
    }
});