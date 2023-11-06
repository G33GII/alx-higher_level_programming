#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Function that makes a copy and insert into new list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list.copy()

    _lst = my_list.copy()
    _lst[idx] = element
    return _lst
