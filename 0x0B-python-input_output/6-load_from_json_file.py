#!/usr/bin/python3
"""function: that creates an Object from a “JSON file”"""
js = __import__("json").load


def load_from_json_file(filename):
    """function: that creates an Object from a “JSON file”"""

    with open(filename) as f:
        return js(f)
