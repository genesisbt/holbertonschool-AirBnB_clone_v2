#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from importlib import import_module
import os


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        return self.__objects

    def new(self, obj):
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj is not None:
            delete_key = obj.to_dict()['__class__'] + '.' + obj.id
            if delete_key in self.__objects.keys():
                del self.__objects[delete_key]

    def close(self):
        self.reload()