#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    z = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end='')
            z += 1
        except (IndexError, ValueError, TypeError, AttributeError):
            pass
    print()
    return z
