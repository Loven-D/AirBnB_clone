#!/usr/bin/python3
"""
creates a unique FileStorage instance for the application.
"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
