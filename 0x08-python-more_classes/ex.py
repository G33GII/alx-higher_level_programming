def some_function(value):
    if type(value) != int:
        raise TypeError("Width must be an integer")
    # ... other code here

try:
    some_function('abc')
    # Code here will not be executed if an exception is raised above
    print("This won't be printed if the TypeError is raised")
except TypeError as e:
    print(f"Error: {e}")
    # Code to handle the exception goes here
