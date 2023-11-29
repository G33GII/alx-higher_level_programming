#!/usr/bin/python3
"""Module for adding two integers."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        first_integer: The first integer to be added.
        second_integer: The second integer to be added, defaults to 98.

    Raises:
        TypeError: If either a or b are not int or float.

    Returns:
        The sum of the two integers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)

    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
