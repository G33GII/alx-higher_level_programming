#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """class MyList that inherits from list
        Args:
        Returns:
        """
        print(sorted(self))
