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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        _l = []
        _filename = ""
        for idx, x in enumerate(list_objs):
            _dict = x.to_dictionary()
            _l.append(_dict)

        __filename = list_objs[0].__class__.__name__ + ".json"
        with open(__filename, "w", encoding="utf-8") as f:
            f.write(json.dumps(_l))
