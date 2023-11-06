#!/usr/bin/env python3
def no_c(my_string):
    _str = ""

    for itx in my_string:
        if itx == "c" or itx == "C":
            continue
        else:
            _str += itx
    return _str
