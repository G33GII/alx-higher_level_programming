#!/usr/bin/python3

def multiple_returns(sentence):
    """Function that: returns a tuple: length & first character of a str"""
    return len(sentence), None if len(sentence) == 0 else sentence[0]
