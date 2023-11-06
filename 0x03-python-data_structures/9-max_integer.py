#!/usr/bin/python3

def max_integer(my_list=[]):
    """Function that finds the biggest integer of a list"""

    if len(my_list) != 0 or my_list != [] or my_list:
        _rx = my_list[0]

        for x in my_list:
            _rx = x if x > _rx else _rx

        return _rx
