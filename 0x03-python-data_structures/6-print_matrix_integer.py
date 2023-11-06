#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers"""

    for row in matrix:
        _ln = len(row) - 1
        for element in row:
            if element != row[_ln]:
                print("{:d}".format(element), end=' ')
            else:
                print("{:d}".format(element), end='')
        print()  # Add a newline to separate rows
