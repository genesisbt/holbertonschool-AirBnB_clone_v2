#!/usr/bin/python3
from sqlalchemy import *
from sqlalchemy.orm import *
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'), pool_pre_ping=True))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query objects from the database session by the class name."""

        objects = {}
        classes = [cls] if cls else [BaseModel, User, State, City, Amenity, Place, Review]
        for cls in classes:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        return objects
    
    def new(self, obj):
        """Add object to current db session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit changes of current db session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from current db session"""
        if obj:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """Reloads the database state."""
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)