#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Function that computes the square value of all integers in a matrix.

    Args:
        matrix (list, optional): A 2-dimensional array. Defaults to [].
    """
    return [[x ** 2 for x in row] for row in matrix]
