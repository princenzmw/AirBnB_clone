#!/usr/bin/python3
""" The Base model for my AirBnb project """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class for other classes to inherit common
    attributes/methods."""

    def __init__(self):
        """Initialize a new instance of BaseModel."""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """Return a string representation of the BaseModel instance.

        Returns:
            str: basemodel info
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.

        Returns:
            dict: a dictionary containing all keys/values of __dict__ of
            the instance
        """
        ret_dict = self.__dict__.copy()
        ret_dict["__class__"] = type(self).__name__
        ret_dict["created_at"] = self.created_at.isoformat()
        ret_dict["updated_at"] = self.updated_at.isoformat()
        return ret_dict
