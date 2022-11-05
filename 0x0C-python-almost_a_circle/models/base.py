#!/usr/bin/python3
""" Module contains class Base

base class of all the classes in the project
"""

import json


class Base:
    """
    defines class base
    class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing id in base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Creates the JSON representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON representation of the list of dictionaries.
        """
        temp = []
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return str(temp)
        temp = json.dumps(list_dictionaries)
        return temp

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None and list_objs == 0:
            with open(cls.__name + '.json', 'w', encode='utf-8') as f:
                f.write(cls.to_json_string(temp))
        else:
            for v in list_objs:
                temp.append(v.to_dictionary())
            with open(cls.__name + '.json', 'w', encode='utf-8') as f:
                f.write(cls.to_json_string(temp))
