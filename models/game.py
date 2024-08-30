#!/usr/bin/python3
from sqlalchemy import Column, String, ForeginKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Game(BaseModel, Base):
    __tablename__ = 'games'
    user_id = Column(String(60), ForeginKey('users.id'), nullable=False)
    opponent_id = Column(String(60), ForeginKey('users.id'), nullable=False)
    winner = Column(String(16), ForeginKey('users.username'), nullable=False)
    users = relationship('User', back_populates='games')
