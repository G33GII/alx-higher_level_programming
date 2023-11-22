#!/usr/bin/python3
"""Defines a class"""


class Square:
    """This class represents a square.

        Attributes:
            size (int): Size of the square (private instance attribute).
                Defaults to 0 if not specified.
    """
    def __init__(self, size=0):
        """Initialize a square with an optional size.

        Args:
            size (int): Size of the square (private instance attribute).
                Defaults to 0 if not specified.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
