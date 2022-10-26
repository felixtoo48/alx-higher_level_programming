#!/usr/bin/python3
"""
Module 0-square
Define class square
"""


class Rectangle:
    """Define a rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize a rectangle.

        Args:
        width (int): width of the new rectangle
        height (int): the height of the new rectangle
        """
        type(self).number_of_instances += 1
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
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """ return printed representation of Rectangle

        Rectangle is printed with # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        shape = []
        for i in range(self.__height):
            [shape.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                shape.append("\n")
        return (''.join(shape))

    def __repr__(self):
        shape = "Rectangle(" + str(self.__width) + ", "
        shape += str(self.__height) + ")"
        return shape

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
