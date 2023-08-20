#!/usr/bin/python3
"""Defines a class for Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review class"""
    place_id = ""
    user_id = ""
    text = ""
