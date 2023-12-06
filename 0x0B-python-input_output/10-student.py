#!/usr/bin/python3
"""class Student that defines a student by: (based on 9-student.py)"""


class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Create a JSON-like representation of the Student object.

        Args:
            attrs (list): A list of attributes to include in
                                the JSON representation.

        Returns:
            dict: A dictionary representation of
                        the Student object with specified attributes.
                  If 'attrs' is None or invalid,
                                returns all attributes in the object.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
