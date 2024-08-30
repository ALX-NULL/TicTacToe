import os

from flask import Flask, g, render_template, session

from app.service import get_user
from models import storage
from app.auth import bp as auth

app = Flask(__name__)
app.register_blueprint(auth)

secret_key = os.getenv("SECRET_KEY")
app.secret_key = secret_key
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """hamada"""
    return render_template("index.html")

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
