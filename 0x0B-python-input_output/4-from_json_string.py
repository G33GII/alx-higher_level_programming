#!/usr/bin/python3
"""function: that returns an object (Python data structure)
                                represented by a JSON string"""


def from_json_string(my_str):
    """from_json_string: returns an object (Python data structure)
                                represented by a JSON string"""
    json = __import__("json").loads
    return json(my_str)
