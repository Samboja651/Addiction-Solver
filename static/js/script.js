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

    // Sending the message to the server using Fetch API
    fetch('/peer-chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `message=${encodeURIComponent(message)}`,
    })
    .then(response => response.json())
    .then(data => {
        // Assuming 'messages' is an array of messages returned by the server
        const chatBox = document.getElementById('peerToPeerChat');
        chatBox.innerHTML = data.messages.map(msg => `<p>${msg}</p>`).join('');
    })
    .catch(error => console.error('Error sending peer message:', error));

    // Clear the input field after sending the message
    document.getElementById('peerMessage').value = '';
}

// Function to send a message in the personalized chat with the doctor
function sendDoctorMessage() {
    const message = document.getElementById('doctorMessage').value;

    // Sending the message to the server using Fetch API
    fetch('/doctor-chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `message=${encodeURIComponent(message)}`,
    })
    .then(response => response.json())
    .then(data => {
        // Assuming 'messages' is an array of messages returned by the server
        const chatBox = document.getElementById('doctorChat');
        chatBox.innerHTML = data.messages.map(msg => `<p>${msg}</p>`).join('');
    })
    .catch(error => console.error('Error sending doctor message:', error));

    // Clear the input field after sending the message
    document.getElementById('doctorMessage').value = '';
}

