#!/usr/bin/python3

class Square:
    """This class represents a square.

        Attributes:
            size: size of square.
    """

    def __init__(self, size):
        """Initialize a square with a given size.

        Args:
            size: Size of the square (private instance attribute).
        """
        self.__size = size
