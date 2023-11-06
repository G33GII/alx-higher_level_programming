#!/usr/bin/python3
def element_at(my_list, idx):

    dx = len(my_list)

    if idx < 0:
        return None
    if idx > dx:
        return None
    return my_list[idx]
