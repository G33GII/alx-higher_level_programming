#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    z = 0
    for n in range(x):
        try:
            print(int(my_list[n]), end='')
            z += 1
        except (IndexError, ValueError, TypeError):
            continue
    print()
    return z
