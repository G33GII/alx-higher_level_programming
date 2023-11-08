#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list.

    Args:
        my_list (list): my_list is the initial list
        search (char): search is the element to replace in the list
        replace (char): replace is the new element
    """
    return [itm if itm != search else replace for itm in my_list]
