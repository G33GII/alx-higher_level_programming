#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of a square (based on 4-square.py).

    Attributes:
        size (int): Size of the square's side. Defaults to 0.
                Must be a non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square's side. Defaults to 0.
                Must be a non-negative integer.
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size ** 2).
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (int): Size of the square's side.
                Must be a non-negative integer.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Prints the square using '#' characters.

        If the size is 0, prints an empty line.
            Otherwise, prints a square with '#'
            of size side by side and on each row.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
