#!/usr/bin/python3

""" Module 1-my_list

inherits from list and prints int in a sorted order
"""


class MyList(list):

    def print_sorted(self):
        """ prints int list in a sorted order """
        print(sorted(self))
