#!/usr/bin/python3
""" """

def add_integer(a, b=98):
    """Function """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("a must be an integer")
    return (a + b)

