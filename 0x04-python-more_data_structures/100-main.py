#!/usr/bin/python3
weight_average = __import__('100-weight_average').weight_average

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))

"""Write a function that returns the weighted average of all integers tuple (<score>, <weight>)

Prototype: def weight_average(my_list=[]):
Returns 0 if the list is empty
You are not allowed to import any module
 """
