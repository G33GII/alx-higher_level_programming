#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    av = sys.argv
    _lx = len(av)
    _av = 0

    for i in range(1, _lx):
        fx = int(av[i])
        _av += fx
    print(_av)
