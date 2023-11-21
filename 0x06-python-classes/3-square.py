#!/usr/bin/python3
""" Defines a CLASS """


class Square:
    """
    Class that defines properties of a square (based on 2-square.py).

    Attributes:
        __size: Size of a square (1 side).
    """

    def __init__(self, size=0):
        """Creates new instances of a square.

        Args:
            size (int): Size of the square (1 side). Defaults to 0.
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

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2
