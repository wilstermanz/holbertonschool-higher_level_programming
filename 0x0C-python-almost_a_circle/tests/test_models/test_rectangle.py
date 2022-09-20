#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit test suite for Rectangle"""

    def test_docstrings(self):
        """Checks module and function docstrings"""
        modDocstring = __import__('models').rectangle.__doc__
        self.assertIsNotNone(modDocstring)
        clsDocstring = __import__('models').rectangle.Rectangle.__doc__
        self.assertIsNotNone(clsDocstring)
        mDocstring = __import__('models').rectangle.Rectangle.area.__doc__
        self.assertIsNotNone(mDocstring)
        mDocstring = __import__('models').rectangle.Rectangle.display.__doc__
        self.assertIsNotNone(mDocstring)
        mDocstring = __import__('models').rectangle.Rectangle.update.__doc__
        self.assertIsNotNone(mDocstring)

    def test_simple_testcases(self):
        """Checks for simple, correct test cases"""
        r1 = Rectangle(10, 2, 0, 0, 1)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10, 0, 0, 2)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_negative_id(self):
        """Checks if negative id is valid"""
        r4 = Rectangle(2, 2, 0, 0, -1)
        self.assertEqual(r4.id, -1)

    def test_type_errors(self):
        """Checks for TypeErrors"""
        with self.assertRaises(TypeError):
            Rectangle("height", 1)
        with self.assertRaises(TypeError):
            Rectangle(1, "width")
        with self.assertRaises(TypeError):
            Rectangle(1, 1, "x", 0)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, "y")
        with self.assertRaises(TypeError):
            Rectangle(None)

    def test_value_errors(self):
        """Checks for ValueErrors"""
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 0, -1)

    def test_area(self):
        r = Rectangle(1, 1)
        self.assertEqual(r.area(), 1)
        r = Rectangle(2, 10)
        self.assertEqual(r.area(), 20)
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r = Rectangle(5, 5, 1)
        self.assertEqual(r.__str__(), f"[Rectangle] ({r.id}) 1/0 - 5/5")
        r = Rectangle(1, 1)
        self.assertEqual(r.__str__(), f"[Rectangle] ({r.id}) 0/0 - 1/1")

    def test_update(self):
            r1 = Rectangle(10, 10, 10, 10, 10)
            self.assertEqual(r1.id, 10)
            self.assertEqual(r1.width, 10)
            self.assertEqual(r1.height, 10)
            self.assertEqual(r1.x, 10)
            self.assertEqual(r1.y, 10)
            r1.update(89, 2, 3, 4, 5)
            self.assertEqual(r1.id, 89)
            self.assertEqual(r1.width, 2)
            self.assertEqual(r1.height, 3)
            self.assertEqual(r1.x, 4)
            self.assertEqual(r1.y, 5)
