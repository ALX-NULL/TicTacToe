#!/usr/bin/python3
from sqlalchemy import Column, String, ForeignKey
from models.base_model import Base, BaseModel


class Game(BaseModel, Base):
    __tablename__ = 'games'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    opponent_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    winner = Column(String(16), ForeignKey('users.id'), nullable=False)
