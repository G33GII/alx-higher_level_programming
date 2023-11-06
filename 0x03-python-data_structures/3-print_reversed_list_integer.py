#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Function that  prints all integers of a list, in reverse order"""

    for item in my_list[::-1]:
        print("{}".format(item))
