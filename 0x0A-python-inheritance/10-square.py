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
            name(str): The name of the parameter.
            value(int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
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
            width(int): most be an integer
            height(int): most be an integer
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width

    def area(self):
        """Area: different from the parent area method"""
        return self.__width * self.__height

    def __str__(self):
        """___str___: for print(obj)"""
        return f"[Rectangle] {self.__width}/{self.__height}"


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
