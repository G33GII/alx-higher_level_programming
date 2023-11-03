#!/usr/bin/python3
import sys

"""

if __name__ == "__main__":
    import sys

    av = sys.argv
    _lx = len(av)
    _av = 0

    for i in range(1, _lx):
        fx = int(av[i])
        _av += fx
    print(_av)
"""


if __name__ == "__main":
    # Initialize the result to 0
    result = 0

    # Iterate through the command-line arguments (excluding the script name)
    for arg in sys.argv[1:]:
        # Cast each argument to an integer and add it to the result
        result += int(arg)

    # Print the result
    print(result)
