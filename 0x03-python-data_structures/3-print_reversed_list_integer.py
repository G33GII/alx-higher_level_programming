#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Function that  prints all integers of a list, in reverse order"""
    _str = "{:d}"
    my_list = my_list[::-1]
    # my_list.reverse()
    for _dx in my_list:
        print(_str.format(_dx))

