#!/usr/bin/python3
"""
Module Square
creates a class Square
Inherits properties from class Rectangle
Initializing the class Square
getter and setter for size
method to return square properties
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    defines class Square; inherits from class Rectangle
    Inherited Attributes:
        width, height, id, x, y
    Class Attributes:
        size
        __x              __y
    Methods:
        def __init__(self, size, x=0, y=0, id=None):
        size(self)      size(self, value)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square"""
        return self.__width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return ("[{:s}] ({:d}) {:d}/{:d} - \
{:d}".format(self.__class__.__name__, self.id, self.x, self.y, self.width))
