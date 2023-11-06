#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    str = "{:d}"
    _lx = len(my_list) - 1
    for _dx in range(_lx, -1, -1):
        print(str.format(my_list[_dx]))
