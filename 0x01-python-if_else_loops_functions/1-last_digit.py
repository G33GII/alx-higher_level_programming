#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    _mod = number % 10
else:
    _mod = (-number % 10) * -1

if (_mod == 0):
    print("Last digit of {} is {} and is 0".format(number, _mod))
elif (_mod > 0 and _mod < 6):
    print(f"Last digit of {number} is {_mod} and is less than 6 and not 0")
elif (_mod > 6):
    print(f"Last digit of {number} is {_mod} and is greater than 5")
else:
    print(f"Last digit of {number} is {_mod} and is less than 6 and not 0")