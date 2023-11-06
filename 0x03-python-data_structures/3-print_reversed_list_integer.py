#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Function that  prints all integers of a list, in reverse order"""
    if isinstance(my_list, list):
        # _str = "{:d}"
        # my_list.reverse()
        my_list = my_list[::-1]
        for _dx in my_list:
            print("{:d}".format(_dx))
