#!/usr/bin/python3
"""
A storage class Module.
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Class to serialize & deserialize insts to/from a JSON file."""

    __file_path = "file.json"
    __objects = {}
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def all(self):
        """
        Retrieve all objs stored in the storage.

        Returns:
            dict: A dict.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new obj to d storage.

        Args:
            obj (BaseModel): D obj to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize & save d objs to d JSON file.
        """
        seralize = {}
        for key, value in self.__objects.items():
            seralize[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as ifile:
            json.dump(seralize, ifile)

    def reload(self):
        """
        Deserialize & load objs from d JSON file.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as ifile:
                obj_dict = json.load(ifile)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = self.__classes[class_name](**value)
        except FileNotFoundError:
            pass
