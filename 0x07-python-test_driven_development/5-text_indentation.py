#!/bin/usr/python3
"""function that prints a text with 2 new
            lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """function that prints a text with 2 new lines
            after each of these characters: ., ? and :
    Args:
        text(str):
    Raises:
        TypeError: text must be a string.
    Returns:
        prints a text with 2 new lines
                after each of these characters: ., ? and :
    """
    _delim = ('.', '?', ':')
    y = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for x in text:
        if y in _delim and x == " ":
            continue
        print(x, end='')
        print('\n' * 1) if x in _delim else None
        y = x


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
