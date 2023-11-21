#!/usr/bin/python3
"""Defines a class"""


class Square:
    """
    A class representing a geometric square.

    Attributes:
        size: The length of one side of the square.
        position: A tuple representing the coordinates of the square's position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size: The size of the square's side. Defaults to 0.
            position: A tuple indicating the position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Returns the size of the square's side.

        Returns:
            The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square's side.

        Args:
            value: The new size of the square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Returns the position of the square.

        Returns:
            A tuple representing the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value: A tuple representing the new position of the square.

        Raises:
            TypeError: If the provided position is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints the square using the '#' character.

        Prints empty lines for the vertical position and spaces for the horizontal position.
        If the size of the square is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
