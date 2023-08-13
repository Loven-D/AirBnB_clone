#!/usr/bin/python3
"""Defines a basemodel for all classes."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Represents the basemodel class for all other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes every instance of BaseModel

        Args:
            *args (tuples): contains arguments.
            **kwargs (dictionary): Contains arguments with key-value pairs
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representing an object
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, str(self.__dict__))

    def save(self):
        """
        updates the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representing an instance of the object
        """
        tmp_dict = self.__dict__.copy()
        tmp_dict['__class__'] = self.__class__.__name__
        tmp_dict['created_at'] = self.created_at.isoformat()
        tmp_dict['updated_at'] = self.updated_at.isoformat()
        return tmp_dict
