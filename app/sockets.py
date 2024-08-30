"""Handling Socket.io events by the server"""

import socketio

sio = socketio.Server()

app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print("connect ", sid)


@sio.event
def my_message(sid, data):
    print("message ", data)


@sio.event
def disconnect(sid):
    print("disconnect ", sid)
