const socket = io();

// Get the chat area and message input elements
const chatArea = document.getElementById('chat-area');
const messageInput = document.getElementById('message-input');
const sendMessage Button = document.getElementById('send-message');

// Event listener for sending messages
sendMessageButton.addEventListener('click', () => {
  const message = messageInput.value;
  if (message) {
    // Emit the "send_message" SocketIO event with the message text
    socket.emit('send_message', message);
    // Clear the message input field
    messageInput.value = '';
  }
});

// Event listener for receiving messages
socket.on('receive_message', (data) => {
  const messageElement = document.createElement('li');
  messageElement.className = (data.username === sessionStorage.getItem('username')) ? 'sent-message':'received-message'
  // Display the username and message text
  messageElement.innerHTML = `<span class="chat-user"><strong>${data.username}:</strong> </span>${data.message}`;
  const newDate = new Date();
  newDate.getTime()
  messageDate = newDate.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  messageElement.innerText += `<br><span class="${data.username}-messageDate">${messageTime}</span>`
  // Append the new message element to the chat list
  chatArea.appendChild(messageElement);
  // Scroll the chat area to the bottom to show the latest message
 // chatArea.scrollTo(0, chatArea.scrollHeight);
  setTimeout(() => 
  scroll(0, 300), 5
);
});

// Event for user join and display notification
socket.on('user_joined', (data) => {
  const messageElement = ` <span class= "notification-message">${data.username} has joined the  Chat.</span>`  
  const msgElem = document.getElementById('msgElement')
  chatArea.insertBefore(msgElement, chatArea.childNodes[0],{once:true});
});  

//Event for user disconnected and display notification

socket.on('user_left', (data) => {// Emit the "send 
  const chatArea = document.getElementById('chatArea');
 const msgElemnt = document.getElementById('msgElements')
 const messageElemn = document.createRange().createContextualFragment('<span class= \'\'  notification-message> ${data. username} has left chat. </span>')
 msgElmnt.insertBefore(messageElm, msgElmtn.childNodes[4], {once: true} );
 	//chatArea.insertBefore(msgElemt, msgElemt.parentNode.firstChild)

  });



  //Get Username from user on page load 




function handleLogin(e) {
  const email = document.getElementsByName("email");   //Get username input from the form  
  sessionStorage.setItem ('username',email['0'].defaultValue); //store it in local store to re-use it .
   console.log(document.getElementsByName "email");
 const username = email['0'].defaultvalue; 	
   console.debug('User logging in with name:' + username); 	


  // Send username to the server  
  if (username !== '' ) {  console.log("logging in")	
   socket.emit 'login', { username }  
 }   

  e.preventDefault  //Stop the form form submitting  
}; 
  const form =document.querySelector(".myForm");   //Get HTML form 




  form.addEventlistener("keydown", handleLogin);//Listen for form submit
