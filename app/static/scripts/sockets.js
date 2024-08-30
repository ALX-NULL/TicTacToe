// Connect to the Socket.IO server
socket = io("http://localhost:5000");

// Handle connection event
socket.on("connect", () => {
  console.log("Connected to server");
});

// Handle incoming messages from the server
socket.on("message", (data) => {
  console.log("Message from server:", data);
});

// Send a message to the server
socket.send("Hello from the client!");

// Handle disconnection event
socket.on("disconnect", () => {
  console.log("Disconnected from server");
});
