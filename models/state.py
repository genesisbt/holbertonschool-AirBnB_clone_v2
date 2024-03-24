#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import *


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
<<<<<<< HEAD

Base.metadata.create_all(engine)
=======
>>>>>>> e9ff852cdcc0edb5425818338b28653989b485b8
