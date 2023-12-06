#!/usr/bin/python3
"""A function"""


def inherits_from(obj, a_class):
    """Function: That checks direct or indirect inheritance from another class

    Args:
        obj: An object
        a_class: A class

    Returns:
        returns True if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
