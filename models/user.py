#!/usr/bin/python3
from sqlalchemy import Column, String

from models.base_model import Base, BaseModel


class User(BaseModel, Base):
    __tablename__ = "users"

    username = Column(String(16), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    name = Column(String(32), nullable=True)

    def valid_password(self, password):
        """Check if a given password is valid"""
        return self.passwrd == password
