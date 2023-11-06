#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Function that adds two tuples element-wise and returns a new tuple."""

    lx_a = len(tuple_a)
    lx_b = len(tuple_b)
    lx_ = max(lx_a, lx_b)  # Use the maximum length

    nw_ = []  # Initialize a list to store the sums

    for i in range(lx_):
        _a = tuple_a[i] if i < lx_a else 0  # Use 0 for missing elements
        _b = tuple_b[i] if i < lx_b else 0  # Use 0 for missing elements
        nw = _a + _b
        nw_.append(nw)

    return tuple(nw_)  # Return the result as a tuple
