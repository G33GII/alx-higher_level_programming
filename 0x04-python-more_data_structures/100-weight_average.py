#!/usr/bin/python3

def weight_average(my_list=[]):

    if not my_list:
        return 0

    weighted_values = [value * weight for value, weight in my_list]
    total_weight = sum(weight for _, weight in my_list)

    return sum(weighted_values) / total_weight

    """average = 0
    div = 0

    for tup in my_list:
        average += tup[0] * tup[1]
        div += tup[1]

    return float(average / div)"""
