#!/usr/bin/python3
"""A function"""


def is_kind_of_class(obj, a_class):
    """Function: That checks the class or subclass of an Object.

    Args:
        obj: An object
        a_class: A class

    Returns:
        True if the obj is an instance of / if the obj is an instance of
        a class that inherited from, the specified class ; otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
