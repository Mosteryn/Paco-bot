function addMessage(username, message) {
    var messageContainer = document.getElementById('message-container');
    var messageElement = document.createElement('div');
    messageElement.innerHTML = '<strong>' + username + '</strong>: ' + message;
    messageContainer.appendChild(messageElement);
    messageContainer.scrollTop = messageContainer.scrollHeight;
  }
  