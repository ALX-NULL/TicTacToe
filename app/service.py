#!/usr/bin/env python3

""" Defines a function `get_page` with caching and counting """

from models import storage
from models.user import User
from typing import List


def get_users() -> List[User]:
    """ Get all users """
    return storage.all('User')


def get_user(user_id: str) -> User:
    """ Get a user by ID """
    return storage.get('User', user_id)


def get_user_by_username(username: str, password: str) -> User | None:
    """ Get a user by email """
    users = storage.all('User')
    for user in users.values():
        if user.username == username and user.password == password:
            return user
    return None


def create_user(name: str, username: str, password: str) -> User:
    """ Create a new user """
    user = User(name=name, username=username, password=password)
    storage.new(user)
    storage.save()
    return user


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
