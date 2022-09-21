#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit test suite for Rectangle"""

    def test_docstrings(self):
        """Checks module and function docstrings"""
        modDocstring = __import__('models').base.__doc__
        self.assertIsNotNone(modDocstring)
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)
        self.assertIsNotNone(Base.create.__doc__)

    def test_objects(self):
        """Tests for created objects"""
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)
        Base()
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_docstrings(self):
        """Checks module and function docstrings"""
        modDocstring = __import__('models').base.__doc__
        self.assertIsNotNone(modDocstring)
        clsDocstring = __import__('models').base.Base.__doc__
        self.assertIsNotNone(clsDocstring)

    def test_simple(self):
        """Tests simple, correct use cases"""
        Base._Base__nb_objects = 0
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
        obj2 = Base()
        self.assertEqual(obj2.id, 2)
        obj3 = Base()
        self.assertEqual(obj3.id, 3)
        obj4 = Base(12)
        self.assertEqual(obj4.id, 12)
        obj5 = Base(None)
        self.assertEqual(obj5.id, 4)

    def test_negative(self):
        """Tests negative ids"""
        neg = Base(-1)
        self.assertEqual(neg.id, -1)
        neg = Base(-100)
        self.assertEqual(neg.id, -100)


if __name__ == '__main__':
    unittest.main()
