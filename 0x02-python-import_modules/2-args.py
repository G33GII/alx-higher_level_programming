#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    av = sys.argv
    _dx = len(av) - 1

    if (_dx == 0):
        print("{} arguments.".format(_dx))

    elif (_dx == 1):
        print("{} argument.".format(_dx))
        print("{}: {}".format(_dx, av[_dx]))

    else:
        print("{} arguments:".format(_dx))
        for i in range(1, _dx + 1):
            print("{}: {}".format(i, av[i]))
