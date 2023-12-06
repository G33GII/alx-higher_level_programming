#!/usr/bin/python3
"""A Class"""


class BaseGeometry(object):
    """BaseGeometry"""

    def area(self):
        """Method:
            raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise TypeError(f"{name} must be greater than 0")
