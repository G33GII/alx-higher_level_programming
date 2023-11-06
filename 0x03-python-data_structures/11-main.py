#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

"""Write a function that deletes the item at a specific position in a list.

Prototype: def delete_at(my_list=[], idx=0):
If idx is negative or out of range, nothing change (returns the same list)
You are not allowed to use pop()
You are not allowed to import any module"""
# my_list = [x for x in my_list if x != 3] Removes all occurrences of 3
