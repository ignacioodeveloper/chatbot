var chatSocket = new WebSocket(
    'ws://' + window.location.host +
    '/ws/chat/{{ chat_id }}/'  // Reemplaza {{ chat_id }} con el ID de tu chat
);

chatSocket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var message = data['message'];

    var chatMessagesDiv = document.querySelector('#chat-messages');
    var newMessageDiv = document.createElement('div');
    newMessageDiv.innerText = message;

    chatMessagesDiv.appendChild(newMessageDiv);
};

document.querySelector('#chat-form').addEventListener('submit', function(e) {
    e.preventDefault();
    var userMessageInput = document.querySelector('#user-message-input');
    var message = userMessageInput.value;
    userMessageInput.value = '';

    chatSocket.send(JSON.stringify({
        'message': message
    }));
});