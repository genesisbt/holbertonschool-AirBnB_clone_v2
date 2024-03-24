#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import *

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)

    state_id = Column(String(60), nullable=False, ForeignKey="states.id")

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
    
Base.metadata.create_all(engine)