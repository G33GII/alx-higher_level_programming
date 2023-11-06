#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Function that adds two tuples element-wise and returns a new tuple."""

    if isinstance(tuple_a, tuple) and isinstance(tuple_b, tuple):
        lx_a = len(tuple_a)
        lx_b = len(tuple_b)
        lx_ = 2  # Use the maximum length

        nw_ = []  # Initialize a list to store the sums

        for i in range(lx_):
            _a = tuple_a[i] if i < lx_a else 0  # Use 0 for missing elements
            _b = tuple_b[i] if i < lx_b else 0  # Use 0 for missing elements
            nw = int(_a) + int(_b)
            nw_.append(nw)

        return tuple(nw_)  # Return the result as a tuple
