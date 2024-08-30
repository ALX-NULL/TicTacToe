#!/usr/bin/env python3

import os
import hashlib
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
import service
from user import User

secret_key = os.getenv('SECRET_KEY')
app = Flask(__name__)
app.secret_key = secret_key
app.strict_slashes = False


@app.teardown_appcontext
def close_session(exception):
    """ close session """
    storage.close()


@app.route('/login', methods=['GET'])
def login():
    """ login page """
    if 'user' in session:
        return redirect(url_for('/'))

    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    """ login post """
    username = request.form['username']
    password = request.form['password']
    password = hashlib.md5(password.encode()).hexdigest()
    user = service.get_user_by_username(username, password)
    if user:
        session['user'] = user.id
        return redirect(url_for('/'))
    # if wrong credentials
    # return to login page with error message
    return render_template('login.html', error='Invalid username or password')


@app.route('/logout')
def logout():
    """ logout """
    session.pop('user', None)
    return redirect(url_for('index'))


@app.route('/register', methods=['GET'])
def register():
    """ register page """
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_post():
    """ register post """
    username = request.form['username']
    password = request.form['password']
    name = request.form['name']

    if len(password) < 8:
        return render_template('register.html',
                               error='Password must be at least 8 characters')

    if service.check_username(username):
        return render_template('register.html', error='User already exists')

    password = hashlib.md5(password.encode()).hexdigest()
    user = User(name=name, username=username, password=password)
    user.save()
    session['user'] = user.id
    # message success on sign up and redirect to dashboard
    return render_template('register.html',
                           success='User created successfully')
