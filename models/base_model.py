#!/usr/bin/python3
"""
A module.
"""
import uuid
import json
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Init a nnew inst of BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(
                          self,
                          key,
                          datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                        )
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return %s rep of D BaseModel inst."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Update D updated_at attribute wit D curent datetym."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        newDict = self.__dict__.copy()
        newDict['__class__'] = self.__class__.__name__
        newDict['created_at'] = self.created_at.isoformat()
        newDict['updated_at'] = self.updated_at.isoformat()
        return newDict
