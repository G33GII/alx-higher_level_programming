#!/usr/bin/python3
""" A Class: class Rectangle that inherits from Base."""
from models.base import Base


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
        Raises:
            TypeError: If either of x or y is not an int.
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            ValueError: If either of x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width: Getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width: Setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height: Getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height: Setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X: Getter."""
        return self.__x

    @x.setter
    def x(self, value):
        """X: Setter."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """X: Getter."""
        return self.__y

    @y.setter
    def y(self, value):
        """X: Setter."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """_____________________________________________________"""
    def area(self):
        """funtion for area"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle
        instance with the character #"""
        [print() for _ in range(self.y)]

        for a in range(self.height):
            print(" " * self.x, end='')
            print('#' * self.width)

    def update(self, *args, **kwargs):
        """function that assigns an argument to each attribute
        OR that changes the value of an attribute of an instance

        Args:
            args: variable number of args
            kwargs: Variable num of args in a k:v format (dict)
        """

        att = ["id", "width", "height", "x", "y"]

        for x in range(len(args)):
            if x < len(att):
                setattr(self, att[x], args[x])
        if kwargs is not None or args is None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Update the class Rectangle by adding the public method
        that returns the dictionary representation of a Rectangle"""

        return {'x': self.x, 'y': self.y,
                'id': self.id, 'height': self.height, 'width': self.width}

    def __str__(self):
        """__str__: print(obj)"""
        return (
            "[Rectangle] ({}) {}/{} - {}/{}"
            .format(self.id, self.x, self.y, self.width, self.height)
            )
