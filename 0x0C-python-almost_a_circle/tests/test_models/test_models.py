#!/usr/bin/python3
"""Unittest for models module"""
import unittest


class TestModuleDocstring(unittest.TestCase):
    """Unit test suite for module docstring"""

    def test_docstrings(self):
        """Checks module docstrings"""
        modDocstring = __import__('models').__doc__
        self.assertIsNotNone(modDocstring)


if __name__ == '__main__':
    unittest.main()
