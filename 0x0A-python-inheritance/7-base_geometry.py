#!/usr/bin/python3
"""
Module 6-base_geometry
to raise area of a base GeoMetry
"""


class BaseGeometry:
    """
    Methods:
        area(self)
    """
    def area(self):
        """ not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates input
        Args:
            name (str): assumed always a string
            value (int): greater than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
