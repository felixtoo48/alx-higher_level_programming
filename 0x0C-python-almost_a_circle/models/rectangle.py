#!/usr/bin/python3
"""
Module rectangle
create a class rectangle that inherits from base
Private instance attributes,
each with its own public getter and setter
call super class with id
assign each argument to the right attribute
"""

from models.base import Base


class Rectangle(Base):
    """
    defines class Rectangle; inherits from class Base
    Inherited Attributes:
        id
    Class Attributes:
        __width          __height
        __x              __y
    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
        width(self)      width(self, value)
        height(self)     height(self, value)
        x(self)          x(self, value)
        y(self)          y(self, value)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """Get the x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Get the area of the rectangle"""
        return (self.height * self.width)

    def display(self):
        """ return

        Rectangle printed with # character.
        Updating class Rectangle
        print # by  by taking care of x and y
        """
        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end='') for x in range(self.x)]
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """ initialize str """
        return "[{:s}] ({}) {:d}/{:d} - \
{:d}/{:d}".format(self.__class__.__name__,
                  self.id, self.__x, self.__y,
                  self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates the attributes of this polygon.
        Args:
            args (tuple): A tuple of non-keyword arguments.
            kwargs (dict): A dictionary of keyword arguments.
        """
        attrs = ('id', 'width', 'height', 'x', 'y')
        for key, val in zip(attrs, args):
            setattr(self, key, val)
        if (type(args) is None or len(args) == 0) and (type(kwargs) is dict):
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)
