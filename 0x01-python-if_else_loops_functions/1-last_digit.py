#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
_mod = number % 10
if (_mod == 0):
    # print(f"Last digit of {number} is {_mod} and is 0")
    print("Last digit of {} is {} and is 0".format(number, _mod))
elif (_mod > 0 and _mod < 6):
    print(f"Last digit of {number} is {_mod} and is less than 6 and not 0")
    # print("Last digit of {} is {} and is less than 6 and not 0"
    #                                           .format(number, _mod))
else:
    print(f"Last digit of {number} is {_mod} and is graeter than 5")
    # print("Last digit of {} is {} and is graeter than 5"
    #                                       .format(number, _mod))
