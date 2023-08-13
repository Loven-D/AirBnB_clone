#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def emptyline(self):
        """Do nothing when an emptyline is entered"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ctrl+d to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of a class, saves it and prints the id"""
        if not line or line == "":
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            if line == "BaseModel":
                instance = BaseModel()
            elif line == "User":
                instance = User()
            elif line == "State":
                instance = State()
            elif line == "City":
                instance = City()
            elif line == "Amenity":
                instance = Amenity()
            elif line == "Place":
                instance = Place()
            elif line == "Review":
                instance = Review()
            storage.save()
            print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        args = line.split()
        if not line or line == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id then saves it"""
        args = line.split()
        if not line or line == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name."""
        args = line.split()
        data = storage.all()
        if line and line != "":
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                ins_list = []
        else:
            print([str])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute then saves it"""  
        args = line.split()
        if not line or line == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
