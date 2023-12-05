#!/usr/bin/python
"""class: Student that defines a student"""


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

    def to_json(self):
        """
        Create a JSON-like representation of the Student object.

        Returns:
            dict: A dictionary representation of the Student object.
        """
        return self.__dict__
