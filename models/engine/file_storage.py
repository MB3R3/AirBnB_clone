#!/usr/bin/python3
"""
This module contains the FileStorage model.
"""
import json

from models.base_model import BaseModel                               from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City                                          from models.place import Place                                        from models.review import Review
                                                                      classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,             "Place": Place, "Review": Review, "State": State, "User": U
ser}

class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    
    __file_path = "file.json"
    __objects = {}

    def save(self):
        """
        Serialize __objects to the JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects if it exist.
        """                                                                   try:
            with open(self.__file_path, 'r') as f:                                    json_object = json.load(f)
            for key in json_object:                                                            self.__objects[key] = classes[json_object[key]["__class__"]](**json_object[key])
        except:
            pass
