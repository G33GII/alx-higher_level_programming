#!/usr/bin/python3
"""A Class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
