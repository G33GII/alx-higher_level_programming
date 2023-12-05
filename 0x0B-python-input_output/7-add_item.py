#!/usr/bin/python3
"""Script: that adds all arguments to a Python list,
                    and then save them to a file"""
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
argv = __import__("sys").argv
js = __import__("json").dumps


_l = [x for x in argv[1:]]
filename = "add_item.json"

try:
    _r = (load_from_json_file(filename))
    _r += _l
    save_to_json_file(_r, filename)
except FileNotFoundError:
    save_to_json_file(_l, filename)
