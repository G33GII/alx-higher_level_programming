#!/usr/bin/python3
"""Function: returns True if the object is exactly an
            instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """Function: returns True if the object is exactly an
            instance of the specified class otherwise False
        Args:
            obj: An object, or instance
            a_class: A class
        Returns:
            returns True if the object is exactly an
            instance of the specified class else False
    """
    if type(obj) is a_class and isinstance(obj, a_class):
        return True
    return False
