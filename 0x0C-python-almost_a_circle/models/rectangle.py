#!/usr/bin/python3
""" A Class:
        class Rectangle that inherits from Base.
"""
from base import Base


class Rectangle(Base):
    """Recangle: Class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class: Constructor.

         Args:
            width (int): width
            height (int): height
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): id. Defaults to None.
        """

        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y
        super().__init__(id)

    """*******************************************"""
    def area(self):
        """funtion for area"""
        return self.__width * self.__height

    """*******************************************"""
    def display(self):
        """prints in stdout the Rectangle
        instance with the character #"""
        [print() for _ in range(self.y)]

        for a in range(self.__height):
            print(" " * self.x, end='')
            print('#' * self.__width)

    """*******************************************"""
    def update(self, *args, **kwargs):
        """function that assigns an argument to each attribute
        OR that changes the value of an attribute of an instance"""

        # setting all attr acordingly in a list for args
        att = ["id", "width", "height", "x", "y"]

        for x in range(len(args)):
            if x < len(att):
                setattr(self, att[x], args[x])
        if kwargs is not None or args is None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    """*******************************************"""
    def __str__(self):
        return (
            "[Rectangle] ({}) {}/{} - {}/{}"
            .format(self.id, self.x, self.y, self.width, self.height)
            )

    """*******************************************"""
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
