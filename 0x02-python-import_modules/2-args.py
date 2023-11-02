#!/usr/bin/python3
import sys
if __name__ == "__main__":
    _dx = len(sys.argv) - 1

    if (_dx == 0):
        print("{} arguments.".format(_dx))
    elif (_dx == 1):
        print("{} argument.".format(_dx))
    else:
        print("{} arguments:".format(_dx))
    for i, av in enumerate(sys.argv[1:], 1):
        print("{}: {}".format(i, av))
