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
        """Getter: @size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter: @size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class Square by adding the public method
        Args:
            args: *args is the list of arguments - no-keyworded arguments
            kwargs: can be thought of as a double pointer to a dictionary:
                        key/value (keyworded arguments)
        """
        att = ["id", "size", "x", "y"]

        for x, v in enumerate(args):
            if x < len(att):
                setattr(self, att[x], v)

        for k, v in kwargs.items():
            if k in att:
                setattr(self, k, v)

    def to_dictionary(self):
        """Update the class Square by adding the public method
        that returns the dictionary representation of a Square"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}

    def __str__(self):
        """__str__: print(obj)"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
