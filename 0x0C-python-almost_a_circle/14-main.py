#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":
    to_json_string_fct = Base.__dict__.get("to_json_string")
    if to_json_string_fct is None:
        print("Base doesn't have method to_json_string")
        exit(1)

    if type(to_json_string_fct) is not staticmethod:
        print("to_json_string is not a static method")
        exit(1)
    print("OK", end="")

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
