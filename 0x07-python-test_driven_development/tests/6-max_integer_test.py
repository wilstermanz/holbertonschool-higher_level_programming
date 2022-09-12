#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unit test suite for max_integer

    Args:
        unittest (_type_): _description_
    """

    def test_simple(self):
        # Tests with simple, positive integers
        self.assertEqual(max_integer([0, 1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1, 0]), 3)
        self.assertEqual(max_integer([4, 10, 75, 2]), 75)

    def test_negative(self):
        # Tests with lists containing negative integers
        self.assertEqual(max_integer([0, 1, -2, 3]), 3)
        self.assertEqual(max_integer([3, -2, 1, 0]), 3)
        self.assertEqual(max_integer([4, 10, -75, 2]), 10)
        self.assertEqual(max_integer([-100, -50, -10]), -10)

    def test_empty(self):
        # Tests an empty list
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_same(self):
        # Tests lists containing only the same values
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -1, -1]), -1)

    def test_bad_input(self):
        # Tests lists containing invalid types
        with self.assertRaises(TypeError):
            max_integer([0, "school", 1])
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_string(self):
        # Finds the highest value in a string
        self.assertEqual(max_integer("Best School"), 't')

    def test_floats(self):
        # Inputs floats
        self.assertEqual(max_integer([1, 2, 2.5, 3]), 3)
        self.assertEqual(max_integer([1, 2, 2, 3.5]), 3.5)
        self.assertEqual(max_integer([1.1, 1.2, 1.5, 1.3]), 1.5)
