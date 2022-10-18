#!/usr/bin/python3
"""
Module 0-square
Define class square
"""


class Rectangle:
    """Define a rectangle class"""

    def __init__(self, width=0, height=0):
        """ Initialize a rectangle.

        Args:
        width (int): width of the new rectangle
        height (int): the height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width is 0 or self.height is 0:
            return 0
        else:
            return (2 * (self.width + self.height))
