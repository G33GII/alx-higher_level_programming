#!/usr/bin/python3
"""Unittest script"""


import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBRS(unittest.TestCase):
    """Base - Rectangle - Square unit tetsing"""

    def test_base(self):
        """Base: specific test cases"""

        s1 = Base(10)
        s2 = Base()
        self.assertEqual(s1.id, 10)
        self.assertEqual(s2.id, 1)

    def test_rectangle(self):
        """Base: specific test cases"""
        r1 = Rectangle(2, 5)
        r2 = Rectangle(1, 4)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.id, 3)

        
        
if __name__ == "__main__":
    unittest.main()
        
        
        