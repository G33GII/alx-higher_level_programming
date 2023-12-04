#!/usr/bin/python3
"""function that returns the
list of available attributes and methods of an object"""


def lookup(obj):
    """function that returns
    the list of available attributes and methods of an object
    Args:
        obj(int): Object to be examined.
    Return:
        Returns a list object
    """
    return print(dir(obj))
