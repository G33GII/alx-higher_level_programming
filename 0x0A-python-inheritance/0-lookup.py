#!/usr/bin/python3
"""function that returns the
list of available attributes and methods of an object"""


def lookup(obj):
    """function that returns
    the list of available attributes and methods of an object

    Args:
        obj: Object to be examined.

    Returns:
        list: List of available attributes and methods of the object.
    """
    return dir(obj)
