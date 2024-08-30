import os
import secrets

import socketio
from flask import Flask, g, redirect, render_template, session

from app.auth import bp as auth
from app.service import get_user
from app.sockets import sio
from models import storage

app = Flask(__name__)
app.register_blueprint(auth)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

secret_key = os.getenv("SECRET_KEY")
app.secret_key = secret_key
app.url_map.strict_slashes = False


@app.before_request
def before():
    """attach user to to global"""
    user = get_user(session.get("user", ""))
    if user:
        g.user = user


@app.teardown_appcontext
def close_session(_):
    """close session"""
    storage.close()


@app.route("/")
def home():
    """hamada"""
    return render_template("index.html")


@app.route("/rooms")
def rooms():
    """create or join room"""
    return render_template("rooms.html")


@app.route("/rooms/<room_id>")
def room(room_id):
    """socket connection handler, yes everything is here"""
    if room_id == "new":
        return redirect(f"/rooms/{secrets.token_hex(3)}")

    return render_template("room.html")
