0x03. Python - Data Structures: Lists, Tuples

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# Lists are mutable
my_list.append(4)  # This is allowed
my_list[0] = 0    # This is allowed

# Tuples are immutable
# The following will result in an error:
# my_tuple.append(4)
# my_tuple[0] = 0

"""
import sys
sys.stdout.write("#pythoniscool\n")

*******************************************

sys = __import__('sys')
sys.stdout.write("#pythoniscool\n")
arguments = sys.argv
for i, arg in enumerate(arguments):
    print(f"Argument {i}: {arg}")
***************************************

av = __import__("sys").argv
print(av)


"""
