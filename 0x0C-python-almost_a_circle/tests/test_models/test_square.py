#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit test suite for Square"""

    def test_docstrings(self):
        """Checks module and function docstrings"""
        modDocstring = __import__('models').square.__doc__
        self.assertIsNotNone(modDocstring)
        clsDocstring = __import__('models').square.Square.__doc__
        self.assertIsNotNone(clsDocstring)
        mDocstring = __import__('models').square.Square.area.__doc__
        self.assertIsNotNone(mDocstring)
        mDocstring = __import__('models').square.Square.display.__doc__
        self.assertIsNotNone(mDocstring)
        mDocstring = __import__('models').square.Square.update.__doc__
        self.assertIsNotNone(mDocstring)

    def test_simple_testcases(self):
        """Checks for simple, correct test cases"""
        r1 = Square(10, 0, 0, 1)
        self.assertEqual(r1.id, 1)
        r2 = Square(2, 0, 0, 2)
        self.assertEqual(r2.id, 2)
        r3 = Square(10, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_negative_id(self):
        """Checks if negative id is valid"""
        r4 = Square(2, 0, 0, -1)
        self.assertEqual(r4.id, -1)

    def test_type_errors(self):
        """Checks for TypeErrors"""
        with self.assertRaises(TypeError):
            Square("size")
        with self.assertRaises(TypeError):
            Square(1, "x", 0)
        with self.assertRaises(TypeError):
            Square(1, 0, "y")
        with self.assertRaises(TypeError):
            Square(None)

    def test_value_errors(self):
        """Checks for ValueErrors"""
        with self.assertRaises(ValueError):
            Square(0, 1)
        with self.assertRaises(ValueError):
            Square(1, -1, 0)
        with self.assertRaises(ValueError):
            Square(1, 0, -1)

    def test_area(self):
        r = Square(1)
        self.assertEqual(r.area(), 1)
        r = Square(2)
        self.assertEqual(r.area(), 4)
        r = Square(8, 0, 0, 12)
        self.assertEqual(r.area(), 64)

    def test_str(self):
        r = Square(4, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Square] (12) 2/1 - 4")
        r = Square(5, 1)
        self.assertEqual(r.__str__(), f"[Square] ({r.id}) 1/0 - 5")
        r = Square(1)
        self.assertEqual(r.__str__(), f"[Square] ({r.id}) 0/0 - 1")

    def test_update_args(self):
        r1 = Square(10, 10, 10, 10)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_update_kwargs(self):
        r1 = Square(10, 10, 10, 10)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 3)
