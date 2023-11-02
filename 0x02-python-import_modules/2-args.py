#!/usr/bin/python3
'''
if __name__ == "__main__":
    import sys
    av = sys.argv
    _dx = len(sys.argv) - 1

    if (_dx == 0):
        print("{} arguments.".format(_dx))
    elif (_dx == 1):
        print("{} argument.".format(_dx))
    else:
        print("{} arguments:".format(_dx))
    for i in range(1, _dx + 1):
        print("{}: {}".format(i, av[i]))

#!/usr/bin/python3
#  Prints the number of and the list of its arguments
if __name__ == "__main__":
    import sys

    arg = sys.argv
    size = len(arg) - 1

    if size > 1:
        print("{} arguments:".format(size))
        for i in range(1, size + 1):
            print("{}: {}".format(i, arg[i]))

    elif size == 0:
        print("{} arguments.".format(size))

    else:
        print("{} argument:".format(size))
        print("{}: {}".format(size, arg[1]))
'''
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

    if i >= 1:
        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
