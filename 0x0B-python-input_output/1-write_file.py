#!/usr/bin/python3
""" function that writes a string to a text file (UTF8) and
returns the number of characters written:"""


def write_file(filename="", text=""):
    """write_file: writes a string to a txt (UTF8)
    & returns the num of chars written"""
    with open(filename, "w", encoding="utf=8") as f:
        _r = f.write(text)
        return _r
