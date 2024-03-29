document.getElementById('addiction-form-section').addEventListener('submit', function(event) {
    var form = event.target;
    var isValid = true;

    // Validate each form field
    for (var i = 0; i < form.elements.length; i++) {
        var element = form.elements[i];

        if (element.type !== "submit" && element.value.trim() === "") {
            alert("Please fill in all fields.");
            isValid = false;
            break;
        }

    }

    if (!isValid) {
        event.preventDefault(); // Prevent form submission if validation fails
    }
});

// Function to send a message in the peer-to-peer forum
function sendPeerMessage() {
    const message = document.getElementById('peerMessage').value;
    appendMessage('peerToPeerChat', message);
    // Clear the input field after sending the message
    document.getElementById('peerMessage').value = '';
}

// Function to send a message in the personalized chat with the doctor
function sendDoctorMessage() {
    const message = document.getElementById('doctorMessage').value;
    appendMessage('doctorChat', message);
    // Clear the input field after sending the message
    document.getElementById('doctorMessage').value = '';
}

// Function to append a message to a chat box
function appendMessage(chatBoxId, message) {
    const chatBox = document.getElementById(chatBoxId);
    const messageElement = document.createElement('p');
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
};

// ----------------------------------------------

let initformBtn = document.getElementById('form-init-btn');
let addictionForm = document.getElementById('addiction-form-section');
let quote1 = document.getElementById('quote-1');
let quote2 = document.getElementById('quote-2');
// console.log(quote1)
// console.log(initformBtn);
// console.log(addictionForm);

initformBtn.addEventListener('click', ()=>{
    addictionForm.style.display = 'block';
    addictionForm.style.marginTop = '-10%';
    quote1.style.display = 'block';
    quote2.style.display = 'block';
})

