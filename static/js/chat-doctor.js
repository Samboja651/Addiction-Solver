// script.js

// Function to send a message
function sendMessage() {
    // Get the message content from the input field
    var message = document.getElementById('messageInput').value;

    // Make an AJAX request to send the message to the server
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/send-message', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                // Message sent successfully, do something if needed
            } else {
                // Handle error
            }
        }
    };
    xhr.send(JSON.stringify({ message: message }));
}

// Function to fetch and display messages
function fetchMessages() {
    // Make an AJAX request to fetch messages from the server
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/fetch-messages', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                // Parse the JSON response
                var messages = JSON.parse(xhr.responseText);

                // Display messages on the page
                var messageList = document.getElementById('messageList');
                messageList.innerHTML = ''; // Clear previous messages
                messages.forEach(function(message) {
                    var listItem = document.createElement('li');
                    listItem.textContent = message;
                    messageList.appendChild(listItem);
                });
            } else {
                // Handle error
            }
        }
    };
    xhr.send();
}

// Call the fetchMessages function periodically to update the chat
setInterval(fetchMessages, 1000); // Fetch messages every second (adjust as needed)
