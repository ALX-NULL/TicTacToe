#!/usr/bin/env python3

""" Defines a function `get_page` with caching and counting """

import storage
import user
from typing import List


def get_users() -> List[user.User]:
    """ Get all users """
    return storage.all('User')


def get_user(user_id: str) -> user.User:
    """ Get a user by ID """
    return storage.get('User', user_id)


def get_user_by_username(username: str, password: str) -> user.User:
    """ Get a user by email """
    users = storage.all('User')
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None


def create_user(username: str, password: str) -> user.User:
    """ Create a new user """
    new_user = user.User(username=username)
    new_user.set_password(password)
    storage.new(new_user)
    storage.save()
    return new_user


def check_username(username: str) -> bool:
    """ Check if a username already exists """
    users = storage.all('User')
    for user in users:
        if user.username == username:
            return True
    return False


def to_dict(obj) -> dict:
    """ Convert object to dictionary """
    dic = {}
    for key, value in obj.__dict__.items():
        if key.startswith('_'):
            continue
        dic[key] = value
    return dic
