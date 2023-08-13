#!/usr/bin/python3
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        tmp_dict = {}
        for key in FileStorage.__objects:
            tmp_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(tmp_dict, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            tmp_dict = {}
            with open(FileStorage.__file_path, 'r') as file:
                tmp_dict = json.load(file)
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
            for key, value in tmp_dict.items():
                class_name = key.split('.')[0]
                if class_name == "BaseModel":
                    instance = BaseModel(**value)
                elif class_name == "User":
                    instance = User(**value)
                elif class_name == "State":
                    instance = State(**value)
                elif class_name == "City":
                    instance = City(**value)
                elif class_name == "Amenity":
                    instance = Amenity(**value)
                elif class_name == "Place":
                    instance = Place(**value)
                elif class_name == "Review":
                    instance = Review(**value)
                FileStorage.__objects[key] = instance
