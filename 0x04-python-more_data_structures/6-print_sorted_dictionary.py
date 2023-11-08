#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """function that prints a dictionary by ordered keys.


    Args:
        a_dictionary (_type_): _description_
    """
    _srt = sorted(a_dictionary.keys())
    for k in _srt:
        print("{}: {}".format(k, a_dictionary.get(k)))
