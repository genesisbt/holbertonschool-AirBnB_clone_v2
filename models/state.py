#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import *
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """Getter attribute to return cities associated with this state"""
        from models import storage
        from models.city import City
        Citylist = []
        for element in storage.all():
            if isinstance(element, City):
                if element.state_id == self.id:
                    Citylist.append(element)
        return [Citylist]