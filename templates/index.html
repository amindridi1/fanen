<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Chat Room</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.min.js"></script>
</head>
<body>
    <h1>Chat Room</h1>
    <div id="chat">
        <!-- Chat messages will appear here -->
    </div>
    <input type="text" id="messageInput" placeholder="Type your message here">
    <button onclick="sendMessage()">Send</button>

    <script>
        const socket = io();

        // Function to send a message
        function sendMessage() {
            const message = document.getElementById('messageInput').value;
            socket.send(message);  // Sends the message to the server
            document.getElementById('messageInput').value = '';  // Clear input
        }

        // Listen for messages from the server and display them
        socket.on('message', (msg) => {
            const chatDiv = document.getElementById('chat');
            const messageElement = document.createElement('p');
            messageElement.textContent = msg;
            chatDiv.appendChild(messageElement);
        });
    </script>
</body>
</html>
