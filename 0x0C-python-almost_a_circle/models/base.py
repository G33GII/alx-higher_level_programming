#!/usr/bin/python3
""" A Class:
        This class will be the “base” of all other classes in this project.
"""
import json
import csv


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
        string representation of list_dictionaries
        """
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
        _obj = cls(1, 2) if cls.__name__ == 'Rectangle' else cls(1)
        _obj.update(**dictionary)
        return _obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        _fn = cls.__name__ + ".json"
        try:
            with open(_fn, "r", encoding="utf-8") as f:
                _d = cls.from_json_string(f.read())
                _NI = [cls.create(**x) for x in _d]
                return (_NI)
        except FileNotFoundError:
            return ""

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes and deserializes in CSV"""
        _fn = cls.__name__ + ".csv"
        _dict = [x.to_dictionary() for x in list_objs]

        if _fn == "Rectangle.csv":
            field_name = ['id', 'width', 'height', 'x', 'y']
        elif _fn == "Square.csv":
            field_name = ['id', 'size', 'x', 'y']
        else:
            field_name = ['id']

        with open(_fn, "w", newline="") as f:
            _w = csv.DictWriter(f, fieldnames=field_name)  # DW - DictWriter
            _w.writeheader()
            [_w.writerow(_r) for _r in _dict]

    @classmethod
    def load_from_file_csv(cls):
        """Serializes and deserializes in CSV."""

        filename = cls.__name__ + ".csv"

        with open(filename, "r") as f:

            list_dicts = csv.DictReader(f)
            __list_dicts = [dict([k, int(v)] for k, v in z.items())
                            for z in list_dicts]

            return [cls.create(**x) for x in __list_dicts]
