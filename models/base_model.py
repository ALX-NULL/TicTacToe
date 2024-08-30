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

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.create_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            pass

    def __str__(self):
        represntaion = str(self.__class__.__name__) + self.id
        return f"[{represntaion}] {self.__dict__}"

    def save(self):
        # imopt storage varialble
        self.updated_at = datetime.now()
        # add the obj to the storage
        # save the storage

    def delete(self):
        pass
        # delete the obj from the storage
