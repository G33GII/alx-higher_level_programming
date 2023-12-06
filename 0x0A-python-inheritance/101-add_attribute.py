#!/usr/bin/python3
"""Function.
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object.

    Args:
        obj: The object to which the attribute will be added.
        attr_name (str): The name of the attribute to be added.
        attr_value: The value of the attribute to be added.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    # Check if the object allows the addition of new attributes
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    # Set the attribute to the object
    setattr(obj, attr_name, attr_value)
