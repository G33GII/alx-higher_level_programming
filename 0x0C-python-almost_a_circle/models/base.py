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
        _fn = cls.__name__ + ".json"

        with open(_fn, "w", encoding="utf-8") as f:
            if list_objs is not None:
                _l = [x.to_dictionary() for x in list_objs]
                f.write(cls.to_json_string(_l))
            else:
                f.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string

        Args:
            json_string(dict): is a string representing a list of dictionaries
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            dictionary(dict): can be thought of as a
                            double pointer to a dictionary
        """
        _obj = cls(1, 2)
        _obj.update(**dictionary)
        return _obj
