"""Handling Socket.io events by the server"""
import socketio

sio = socketio.Server(namespaces=['socket.io'])


def connect(sid, environ):
    print(f'Client connected: {sid}')
    sio.send(sid, 'Welcome to the Socket.IO server!')

# Define a message event handler
@sio.event
def message(sid, data):
    print(f'Message from {sid}: {data}')
    sio.send(sid, f'Received your message: {data}')

# Define a disconnection event handler
@sio.event
def disconnect(sid):
    print(f'Client disconnected: {sid}')
