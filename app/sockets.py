import socketio

sio = socketio.Server()


@sio.event
def connect(sid, environ):
    print(f'Client connected: {sid}')
    sio.emit('message', 'Welcome to the Socket.IO server!', room=sid)


@sio.event
def message(sid, data):
    print(f'Message from {sid}: {data}')
    sio.emit('message', f'Received your message: {data}', room=sid)


@sio.event
def gameState(sid, data):
    print(f'Game state from {sid}: {data}')
    sio.emit('gameState', data, skip_sid=sid)


@sio.event
def disconnect(sid):
    print(f'Client disconnected: {sid}')
