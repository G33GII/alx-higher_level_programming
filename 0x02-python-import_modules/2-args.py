#!/usr/bin/python3
import sys
if __name__ == "__main__":
    _dx = len(sys.argv)

    if (_dx == 1):
        print("{} arguments.".format(_dx - 1))
    else:
        print("{} arguments:".format(_dx - 1))
        for i, av in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(i, av))
