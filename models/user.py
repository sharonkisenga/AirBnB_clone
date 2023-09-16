#!/usr/bin/python3
"""
A class User Module.
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class from BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
