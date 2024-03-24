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
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        host = os.environ.get("HBNB_MYSQL_HOST")
        database = os.environ.get("HBNB_MYSQL_DB")
        env = os.environ.get("HBNB_ENV")
        print("Connecting to MySQL database...")
        print(f"User: {user}, Host: {host}, Database: {database}")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}".
                                      format(user, password, host, database),
                                      pool_pre_ping=True)

        Session = sessionmaker(bind=self.__engine)
        Session.configure(bind=self.__engine)
        self.__session = Session()

        if env == "test":
            print("Dropping existing tables...")
            Base.metadata.drop_all(self.__engine)
        print("Creating tables...")
        Base.metadata.create_all(self.__engine)
        print("Initialization completed.")

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
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
        Base.metadata.create_all(self.__engine)