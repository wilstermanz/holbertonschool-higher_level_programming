#!/usr/bin/python3
"""Unittest for models module"""
import unittest
import models


class TestModuleDocstring(unittest.TestCase):
    """Unit test suite for module docstring"""

    def test_docstrings(self):
        """Checks module docstrings"""
        modDocstring = __import__('models').__doc__
        self.assertIsNotNone(modDocstring)
