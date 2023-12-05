def append_after(filename="", search_string="", new_string=""):
    """
    Append 'new_string' after the 'search_string' in the specified file.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in the file.
        new_string (str): The string to append after the 'search_string'.
    """
    _txt = ""
    with open(filename, "r") as f:
        for line in f:
            _txt += line
            if search_string in line:
                # Append 'new_string' after finding 'search_string'
                _txt += new_string

    # Write the modified _txt back to the file
    with open(filename, "w") as f:
        f.write(_txt)
