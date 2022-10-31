#!/usr/bin/python3
""" Module base

base class of all the classes in the project
"""


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing id in base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
