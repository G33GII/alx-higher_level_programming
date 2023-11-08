#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Function: adds all unique integers in a list (only once for each integer).

    Args:
        my_list (list, optional): The input list. Defaults to [].
    """
    unique_set = set(my_list)
    total = 0

    for itm in unique_set:
        total += itm

    return total        # return sum(set(my_list))
