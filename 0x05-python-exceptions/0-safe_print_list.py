#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
   try:
      z = 0
      for i in my_list:
         print("{}".format(i), end="")
         z += 1
         if z == x:
            break
      print()
      return (z)
   except IndexError:
      z = 0
      for i in my_list:
         print("{}".format(i), end="")
         z += 1
      print()
      return (z)
