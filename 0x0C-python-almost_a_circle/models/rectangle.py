#!/usr/bin/python3
""" A Class:
        class Rectangle that inherits from Base.
"""
import sys
sys.path.append('/workspaces/alx-higher_level_programming/0x0C-python-almost_a_circle/models/')
from base import Base


class Rectangle(Base):
    """Recangle:
            Class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class: Constructor."""

        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def height(self):
        """Height: Getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height: Setter."""
        self.__height = value

    @property
    def width(self):
        """Width: Getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width: Setter."""
        self.__width = value

    @property
    def x(self):
        """X: Getter."""
        return self.__x
    @x.setter
    def x(self, value):
        """X: Setter."""
        self.__x = value

    @property
    def y(self):
        """X: Getter."""
        return self.__y
    @y.setter
    def y(self, value):
        """X: Setter."""
        self.__y = value
