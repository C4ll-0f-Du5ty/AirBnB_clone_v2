#!/usr/bin/python3
"""DataBase Storage For The HBNB Project"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
HBNB_ENV = getenv('HBNB_ENV')

Classes = {'User': User, 'State': State,
           'City': City, 'Amenity': Amenity,
           'Place': Place, 'Review': Review}


class DBStorage:
    """The interactions with my Database"""
    __engine = None
    __session = None

    def __init__(self):
        """the first step in the interactions process"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST, HBNB_MYSQL_DB))

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of the data in my Database"""
        if not self.__session:
            self.reload()
        newDict = {}
        if type(cls) == str:
            cls = Classes.get(cls, None)
        if cls is None:
            for C in Classes.values():
                objects = self.__session.query(C)
                for obj in objects:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    newDict[key] = obj
        else:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = f'{obj.__class__.__name__}.{obj.id}'
                newDict[key] = obj
        return newDict

    def new(self, obj):
        """Adding A new Object"""
        self.__session.add(obj)

    def save(self):
        """Saving the Changes"""
        self.__session.commit()

    def delete(self, obj=None):
        if not self.__session:
            self.reload()
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloading and creating all tables in the database"""
        Base.metadata.create_all(self.__engine)

        self.__session = scoped_session(sessionmaker(self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """Closes current session"""
        self.__session.remove()
