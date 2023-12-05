#!/bin/usr/python3
"""function: that appends str at the end of a txt (UTF8)
                        & returns NUM of chars added"""


def append_write(filename="", text=""):
    """append_write: appends str at the end of a txt (UTF8)
                    & returns NUM of chars added"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
