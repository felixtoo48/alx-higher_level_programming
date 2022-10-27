#!/usr/bin/python3
"""
Module 9-rectangle
Contains parent class BaseGeometry
with public instance method area and integer_validator
Contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent
Area method is implemented
should print and return rectangle description
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry
    Methods:
        __init__(self, width, height)
    """
    def __init__(self, width, height):
        """validate and initialize width and height
        Args:
            width (int): private
            height (int): private
        """
        BaseGeometry().integer_validator("width", width)
        self.__width = width
        BaseGeometry().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ print the area of the rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
