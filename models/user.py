#!/usr/bin/python3
"""Defines a class for User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
