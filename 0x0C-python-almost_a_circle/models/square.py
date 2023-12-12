#!/usr/bin/python3
""" A Class: This class inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class: inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Rectangle Class: Constructor.

        Args:
            size (int): height and width == size.
            id (int):  Defaults to None.
            x (int): X axis.
            y (int): y axis.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        super().width = value
        super().height = value

    def __str__(self):
        """__str__: print(obj)"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

