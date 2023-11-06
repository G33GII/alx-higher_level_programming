#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Function that  prints all integers of a list, in reverse order"""
    _lx = (len(my_list) - 1)
    for _dx in range(_lx, -1, -1):
        print("{}".format(my_list[_dx]))
