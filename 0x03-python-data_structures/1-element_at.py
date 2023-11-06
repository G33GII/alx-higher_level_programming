#!/usr/bin/python3

def element_at(my_list, idx):
    """Function that replaces the element at 'idx' if it's a valid index."""
    dx = len(my_list)

    if idx < 0 or idx >= dx:
        return None
    return my_list[idx]
