#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """matrix_divided:


    Args:
        matrix:
        div:

    Raise:
        TypeError: matrix must be a matrix (list of lists) of integers/floats

    Returns:
        Returns a new matrix.
    """
    _l = len(matrix[0])

    if any(not isinstance(z, (int, float)) for x in matrix for z in x):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(z) != _l for z in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Applying division and rounding using nested list comprehension
    _nw = [[round(z / div, 2) for z in x] for x in matrix]

    return _nw


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
