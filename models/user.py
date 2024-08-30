#!/usr/bin/python3
from sqlalchemy import Column,  String, relationship
from models.base_model import Base, BaseModel


class User(BaseModel, Base):
    __tablename__ = "users"

    username = Column(String(16), nullable=False, unique=True)
    passwrd = Column(String(128), nullable=False)
    name = Column(String(32), nullable=True)
    games = relationship('Game', back_populates='users', cascade='all, delete orphan')
