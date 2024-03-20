#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, int, CHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from engine.file_storage import FileStorage
from models.city import City

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(60), nullable=False)
    cities = relationship('City', backref='state', cascade="all, delete")

    @property
    def cities(self):
        return [city for city in FileStorage.all(City)
                if City.state_id == self.id]
