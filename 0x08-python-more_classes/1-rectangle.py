#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if type(value) is not int:
            raise TypeError ("width must be an integer")
        if value < 0:
            raise ValueError ("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if type(value) is not int:
            raise TypeError ("height must be an integer")
        if value < 0:
            raise ValueError ("height must be >= 0")
        self.__height = value
