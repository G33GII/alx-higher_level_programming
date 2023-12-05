#!/usr/bin/python3
"""function: writes an Object to a txt, using a JSON representation"""


def save_to_json_file(my_obj, filename):
    """from_json_string: writes an Object to a txt,
                        using a JSON representation"""
    json = __import__("json").dumps
    __r = json(my_obj)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(__r)
