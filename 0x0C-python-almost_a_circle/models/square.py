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

    def __str__(self):
        """__str__: print(obj)"""
        return (
            "[Square] ({}) {}/{} - {}"
            .format(self.id, self.x, self.y, self.width)
            )
