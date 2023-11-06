#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """ function that deletes the item at a specific position in a list """
    _dx = len(my_list)
    _nw = []

    if my_list and idx > -1 and idx < _dx:
        _nw = [my_list[x] for x in range(_dx) if x != idx]
        """for i in range(_dx):
            if i != idx:
                _nw.append(my_list[i])"""
        return (_nw)

    return (my_list)
