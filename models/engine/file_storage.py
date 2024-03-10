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
    pass
