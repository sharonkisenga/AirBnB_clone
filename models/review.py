#!/usr/bin/python3
"""
A class Review module.
"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
