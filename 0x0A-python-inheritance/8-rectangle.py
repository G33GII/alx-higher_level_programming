#!/usr/bin/python3
"""A Class"""


class BaseGeometry(object):
    """BaseGeometry"""

    def area(self):
        """Method:
            raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name(str):
            value(int):
        Raises:
            TypeError:
            ValueError:
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Reangle Class"""

    def __init__(self, width, height):
        """Initialises heighth and width.
        using a method in the parent to validate width & height

        Args:
            width(int): mostr be an integer
            height(int): mostr be an integer
        """
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
