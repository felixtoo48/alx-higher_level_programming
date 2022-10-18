#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    prevents user from dynamically creating new instance 
    attributes for anything but for first_name
    """

    __slots__ = ["first_name"]
