#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
print()
result = uniq_add(my_list)
print("Result: {:d}".format(result))

"""Write a function that adds all unique integers in a list (only once for each integer).

Prototype: def uniq_add(my_list=[]):
You are not allowed to import any module
"""
