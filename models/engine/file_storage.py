#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        print(self.__class__.__name__ + " " + __name__ )
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        print(self.__class__.__name__ + " " + __name__ )
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        print(self.__class__.__name__ + " " + __name__ )
        """Loads storage dictionary from file"""
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

    def all(self, cls=None):
        """Returns a list of objects of cls type"""
        print(self.__class__.__name__ + " " + __name__ )
        if cls is None:
            return FileStorage.__objects
        objectsofcls = {}
        for key, obj in FileStorage.__objects.items():
            if isinstance(obj, cls):
                objectsofcls[key] = obj
        return objectsofcls

    def delete(self, obj=None):
        print(self.__class__.__name__ + " " + __name__ )
        """Deletes obj from __objects if it exists"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]