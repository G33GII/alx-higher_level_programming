#!/usr/bin/python3
"""Function: Returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False."""


def is_kind_of_class(obj, a_class):
    """Function: Returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

    Args:
        obj: An object
        a_class: A class

    Returns:
        Returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
