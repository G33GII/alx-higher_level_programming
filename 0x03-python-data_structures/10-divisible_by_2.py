#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Function that finds all multiples of 2 in a list """

    _dx = len(my_list)
    _nw = []

    for idx in range(_dx):
        if my_list[idx] % 2 == 0:
            _nw.append(True)
        else:
            _nw.append(False)
    return _nw
