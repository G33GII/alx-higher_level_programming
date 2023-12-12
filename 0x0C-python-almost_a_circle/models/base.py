#!/usr/bin/python3
""" A Class:
        This class will be the “base” of all other classes in this project.
"""
import json


class Base(object):
    """Base class:
            The goal of it is to manage id attribute in all your future classes
            and to avoid duplicating the same code
            (by extension, same bugs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Base Class: Constructor.

        Args:
            id (int, None): _description_. Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string: returns the JSON
        string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
