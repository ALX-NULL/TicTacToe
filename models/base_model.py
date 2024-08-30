#!/usr/bin/python3
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel():
    id = Column(String(60), primary_key=True, nullable=False)
    create_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.updated_at = self.create_at = datetime.now()
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        represntaion = str(self.__class__.__name__) + self.id
        return f"[{represntaion}] {self.__dict__}"

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        # storage.new(self)
        storage.save()

    def delete(self):
        pass
        # delete the obj from the storage
