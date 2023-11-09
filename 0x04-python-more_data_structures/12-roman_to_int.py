#!/usr/bin/python3

def roman_to_int(roman_string):

    if not roman_string or type(roman_string) is not str:
        return 0

    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_n = 0

    for j in range(len(roman_string)):
        if j > 0 and roman_d[roman_string[j]] > roman_d[roman_string[j - 1]]:
            roman_n += roman_d[roman_string[j]] - 2 * \
                        roman_d[roman_string[j - 1]]
        else:
            roman_n += roman_d[roman_string[j]]

    return roman_n

    """
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_n = 0

    prev_value = 0
    for c in roman_string[::-1]:  # Reverse string for easy subtraction logic
        value = roman_d.get(c, 0)

        if value >= prev_value:
            roman_n += value
        else:
            roman_n -= value

        prev_value = value

    return roman_n"""
