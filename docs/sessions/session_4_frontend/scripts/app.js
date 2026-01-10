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
    conversation.innerHTML += "<p id='chargement'><em>Assistant est en train d'écrire...</em></p>";
    
    // Vider l'input
    input.value = "";
    
    // Envoyer au backend
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
        
        // Afficher la réponse de l'assistant
        conversation.innerHTML += "<p><strong>Assistant:</strong> " + donnees.reponse + "</p>";
    });
}

// 3. Écouter le clic sur le bouton
bouton.addEventListener("click", envoyerMessage);

// 4. Écouter la touche Entrée
input.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        envoyerMessage();
    }
});
