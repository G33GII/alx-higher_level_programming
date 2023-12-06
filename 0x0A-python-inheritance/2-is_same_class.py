#!/usr/bin/python3
"""Function: returns True if the object is exactly an
            instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """Function: returns True if the object is exactly an
            instance of the specified class otherwise False"""
    if isinstance(obj, a_class):
        return True
    return False