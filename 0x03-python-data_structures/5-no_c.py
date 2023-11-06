#!/usr/bin/env python3

def no_c(my_string):
    """Function that  that removes all characters c and C from a string"""

    if isinstance(my_string, str):
        _str = ""
        for itx in my_string:
            # if itx != 'c' and itx != 'C':
            if itx not in ('c', 'C'):
                _str += itx
        return _str
