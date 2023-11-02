#!/usr/bin/python3
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


def add_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return
    else:
        i = 1
        add = 0
        while i <= n:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
