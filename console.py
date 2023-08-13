#!/usr/bin/python3
"""
Creates a command interface for the user
"""
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
    """
    Implements the command interface for the user
    """
    prompt = "(hbnb) "
    CLASSES = [
            "BaseModel", "User", "State",
            "Amenity", "Place", "City", "Review"
            ]

    def emptyline(self):
        """Do nothing when an emptyline is entered"""
        pass

    def do_quit(self, line):
        """
        Quit command to exit the program

        Usage: quit
        """
        return True

    def do_EOF(self, line):
        """
        Exits the program

        Usage: CTRL + D
        """
        return True

    def do_create(self, line):
        """
        Creates a new instance of a class, saves it and prints the id

        Usage create <object>
        """
        if not line or line == "":
            print("** class name missing **")
        elif line not in HBNBCommand.CLASSES:
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
        """
        Prints string representation of instance based on the class name and id

        Usage: show <object> <id>
        """
        args = line.split()
        if not line or line == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.CLASSES:
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
        """
        Deletes an instance based on the class name and id then saves it

        Usage: destroy <object> <id>
        """
        args = line.split()
        if not line or line == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.CLASSES:
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
        """
        Print string representation of instances based or not on the class name

        Usage: all <object> | all
        """
        args = line.split()
        data = storage.all()
        if line and line != "":
            if args[0] not in HBNBCommand.CLASSES:
                print("** class doesn't exist **")
            else:
                ins_list = []
        else:
            print([str])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id

        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        args = line.split()
        if not line or line == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.CLASSES:
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
