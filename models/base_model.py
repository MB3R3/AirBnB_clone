#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    """
    Base model that defines all common attributes/methods for other classes

    ...

    Attributes
    ----------
    id : str
        unique identifier assigned  when an instance is created.

    created_at : datetime
        the current datetime when an instance is created.

    updated_at :datetime
        the current datetime when an instance is updated,
        the default value is the time the instance was created.
    """

    def __init__(self, id=uuid.uuid4(), created_at=datetime.datetime.now(), updated_at=datetime.datetime.now()):
        """
        Parameters
        ----------
        id : str
            Unique identifier for each instance
        created_at : datetime
            The current datetime when the instace was created
        updated_at : datetime
            The current datetime when the instance was updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at  = datetime.datetime.now()
        self.__str__ = f"[__name__] (self.id) self.__dict__"

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        return self.__dict__


