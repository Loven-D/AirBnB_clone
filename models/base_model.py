#!/usr/bin/python3
"""Defines a basemodel class."""
import uuid
from datetime import datetime
from __init__ import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
            self.__class__ = type(kwargs['__class__'], (BaseModel,), {})
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        tmp_dict = self.__dict__.copy()
        tmp_dict['__class__'] = self.__class__.__name__
        tmp_dict['created_at'] = self.created_at.isoformat()
        tmp_dict['updated_at'] = self.updated_at.isoformat()
        return tmp_dict
