const express = require('express');
const http = require('http');
const socketIO = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIO(server);

// Serve static files (like your presentation)
app.use(express.static('public'));

// Handle socket connections
io.on('connection', (socket) => {
  console.log('New client connected');
  
  // Handle multiplex events
  socket.on('multiplex-statechanged', (data) => {
    socket.broadcast.emit('multiplex-statechanged', data);
  });

  socket.on('disconnect', () => {
    console.log('Client disconnected');
  });
});

// Start the server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});