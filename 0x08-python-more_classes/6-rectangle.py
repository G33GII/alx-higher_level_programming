#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """A class representing a rectangle."""
    number = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """

        self.__height = height
        self.__width = width
        Rectangle.number += 1

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

        if not isinstance(value, int):
            raise TypeError("Width must be an integer")

        if value < 0:
            raise ValueError("Width must be >= 0")

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

        if not isinstance(value, int):
            raise TypeError("Height must be an integer")

        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        _w = self.__width
        _h = self.__height

        if _w == 0 or _h == 0:
            return 0
        return 2 * (_w + _h)

    def __str__(self):
        """Return a string representation of the rectangle."""
        _r = ""
        _w = self.__width
        _h = self.__height
        if _w == 0 or _h == 0:
            return _r

        for i in range(_h):
            _r += "#" * _w + "\n" if i is not _h - 1 else "#" * _w
        return _r

    def __repr__(self):
        """Return a string representation of the rectangle."""
        _w = self.__width
        _h = self.__height
        return f"Rectangle({_w}, {_h})"

    def __del__(self):
        """Prints a message when Rectangle instance is deleted."""
        Rectangle.number -= 1
        print('Bye rectangle...')

    @classmethod
    def number_of_instances(cls):
        """Returns the current number of instances."""
        return cls.number

