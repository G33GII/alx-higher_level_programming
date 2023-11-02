#!/usr/bin/python3

# Import the 'add' and 'sub' functions from 'magic_calculation_102'
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        # Calculate the initial result by adding 'a' and 'b'
        result = add(a, b)

        # Add numbers from 4 to 5 to the result
        for i in range(4, 6):
            result = add(result, i)

        return result
    else:
        # If 'a' is greater than or equal to 'b', subtract 'b' from 'a'
        return sub(a, b)
