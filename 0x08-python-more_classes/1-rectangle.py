#!/usr/bin/python3
"""
Module 0-square
Define class square
"""


class Rectangle:
    """Define a rectangle class"""

    def __init__(self, width="0", height="0"):
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
        try:
            if str(value).isdigit():
                self.__width = value
        except (TypeError, ValueError):
            if TypeError:
                print("width must be an integer")
            if ValueError:
                print("width must be >= 0")

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        try:
            if str(value).isdigit():
                self.__height = value
        except (TypeError, ValueError):
            if TypeError:
                print("height must be an integer")
            if ValueError:
                print("height must be >= 0")
