#!/bin/usr/python
""" function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """ function that prints My name is <first name> <last name>
    Args:
        last_name(str):
        first_name(str):
    Raises:
        TypeError: first_name must be a string or last_name must be a string
    Returns:
        None.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
