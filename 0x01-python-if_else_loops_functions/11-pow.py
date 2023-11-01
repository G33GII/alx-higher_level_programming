#!/usr/bin/python3
def pow(a, b):
    if a == 0 and b < 0:
        return float('inf')  # Handle division by zero
    if b >= 0:
        result = 1
        for _ in range(b):
            result *= a
        return (result)
    else:
        result = 1
        for _ in range(-b):
            result /= a
        return (result)
