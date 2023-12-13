#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":



    Rectangle.save_to_file([Square(2), Square(4, 1), Square(7, 3, 4)])

    with open("Square.json", "r") as file:
        print(file.read())
