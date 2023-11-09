#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    """ new_ = {}
    for k in a_dictionary:
        new_[k] = a_dictionary[k] * 2
        x = a_dictionary[k]
    return new_
    """
    return {k: v * 2 for k, v in a_dictionary.items()}
