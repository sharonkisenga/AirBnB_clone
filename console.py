#!/usr/bin/python3
"""Command interpreter to execute the console"""
import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex


class HBNBCommand(cmd.Cmd):
    """Hbnb console"""

    prompt = "(hbnb) "
    classes = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
    }

    def do_quit(self, arg):
        """ command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """ command to exit the program\n"""
        return True

    def do_create(self, arg):
        """makea instance of BaseModel\n"""

        """find the classname"""
        if not self.check_class(arg):
            return

        """Creates a instance and saves it"""
        instance = HBNBCommand.classes[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints a specific instance of a class\n"""

        line = self.command_line(arg, 2)

        """find the class name"""
        if not self.check_class(line[0]):
            return

        """find the class id"""
        if not self.check_id(line[0], line[1]):
            return

        key = line[0] + "." + line[1]
        print(storage.all()[key])

    def do_all(self, arg):
        """Prints all the instances of a specific class\n"""

        instances_list = []

        if arg == "":
            for value in storage.all().values():
                instances_list.append(str(value))
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            for key in storage.all().keys():
                if arg in key:
                    instances_list.append(str(storage.all()[key]))

        print(instances_list)

    def do_update(self, arg):
        """Updates the instance based on the class name and the id\n"""

        line = self.command_line(arg, 4)

        """find the class name"""
        if not self.check_class(line[0]):
            return

        """find the class"""
        if not self.check_id(line[0], line[1]):
            return

        """find the class attributes and value"""
        if not self.check_attr(line[2], line[3]):
            return

        value = line[3]
        if value.isnumeric():
            value = int(value)

        key = line[0] + "." + line[1]
        setattr(storage.all()[key], line[2], value)
        storage.save()

    def do_destroy(self, arg):
        """Deletes the instance based on  class name and id\n"""

        line = self.command_line(arg, 2)

        """find the classname"""
        if not self.check_class(line[0]):
            return

        """find class id """
        if not self.check_id(line[0], line[1]):
            return

        key = line[0] + "." + line[1]
        del storage.all()[key]
        storage.save()

    def emptyline(self):
        """Method to cancel command"""
        pass

    def check_class(self, clsname):
        """Validations of class name"""
        if clsname == "":
            print("** class name is not here**")
            return False
        elif clsname not in HBNBCommand.classes:
            print("** where the class **")
            return False
        return True

    def check_id(self, clsname, id):
        """Validations of id"""
        if id == "":
            print("** instance is not here**")
            return False
        elif clsname + "." + id not in storage.all():
            print("** instance found ia not her **")
            return False
        return True

    def check_attr(self, attr, value):
        """Checks the class attributes and the value attribute"""
        if attr == "":
            print("** attribute name taht we are looking **")
            return False
        elif value == "":
            print("** value that we are looking **")
            return False
        return True

    def command_line(self, arg, num_args):
        """Fill line list user's arguments"""

        args = shlex.split(arg)
        line = []

        for i in range(num_args):
            if (len(args) > i):
                line.append(args[i])
                continue
            line.append("")

        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
