#!/usr/bin/env python3

import hashlib
from flask import Blueprint, render_template, request, redirect, url_for, session
import app.service as service


bp = Blueprint("auth", __name__)


@bp.route('/login', methods=['GET'])
def login():
    """ login page """
    if 'user' in session:
        return redirect('/')

    return render_template('login.html')


@bp.route('/login', methods=['POST'])
def login_post():
    """ login post """
    username = request.form['username']
    password = request.form['password']
    password = hashlib.md5(password.encode()).hexdigest()
    user = service.get_user_by_username(username, password)
    if user:
        session['user'] = user.id
        return redirect('/')
    # if wrong credentials
    # return to login page with error message
    return render_template('login.html', error='Invalid username or password')


@bp.route('/logout')
def logout():
    """ logout """
    session.pop('user', None)
    return redirect('/')


@bp.route('/register', methods=['GET'])
def register():
    """ register page """
    if 'user' in session:
        return redirect('/')
    return render_template('register.html')


@bp.route('/register', methods=['POST'])
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
    user = service.create_user(name, username, password)
    session['user'] = user.id
    # message success on sign up and redirect to dashboard
    return render_template('register.html',
                           success='User created successfully')
