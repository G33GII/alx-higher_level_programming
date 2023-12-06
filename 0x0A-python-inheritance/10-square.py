#!/usr/bin/python3
"""A Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """New class for squares"""

    def __init__(self, size):
        """Initialises heighth and width.
        using a method in the parent to validate width & height
        & set height=width=self.__size for squares

        Args:
            size(int): most be an integer
        """
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(width=self.__size, height=self.__size)
