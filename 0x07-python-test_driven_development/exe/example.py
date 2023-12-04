def factorial(n):
    """Return the factorial of n, an exact integer >= 0."""

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    """
    There is also a command line shortcut for running testmod().
    You can instruct the Python interpreter to run the doctest module
    directly from the standard library and pass the module name(s) on the command line:

    python -m doctest -v example.py
    """
    import doctest
    doctest.testfile("example.txt")
