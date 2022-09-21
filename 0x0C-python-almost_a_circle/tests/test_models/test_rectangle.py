#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


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
        """Tests area method"""
        r = Rectangle(1, 1)
        self.assertEqual(r.area(), 1)
        r = Rectangle(2, 10)
        self.assertEqual(r.area(), 20)
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_str(self):
        "Tests __str__ method"
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r = Rectangle(5, 5, 1)
        self.assertEqual(r.__str__(), f"[Rectangle] ({r.id}) 1/0 - 5/5")
        r = Rectangle(1, 1)
        self.assertEqual(r.__str__(), f"[Rectangle] ({r.id}) 0/0 - 1/1")

    def test_update_args(self):
        """Tests update method with args"""
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

    def test_update_kwargs(self):
        """Tests update method with kwargs"""
        r1 = Rectangle(10, 10, 10, 10, 10)
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

    def test_to_dictionary(self):
        """Tests to_dictionary method"""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dictionary = r1.to_dictionary()
        test_d = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, test_d)
        self.assertIsInstance(r1_dictionary, dict)

    def test_to_json_string(self):
        """Tests to_json_str static method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        json_test = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_dictionary, json_test)
        self.assertIsInstance(json_dictionary, str)

    def test_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            list_dicts = file.read()
        test_list = str('[{"id": 1, "width": 10, '
                        '"height": 7, "x": 2, "y": 8}, '
                        '{"id": 2, "width": 2, '
                        '"height": 4, "x": 0, "y": 0}]')
        self.assertEqual(list_dicts, test_list)
        self.assertIsInstance(list_dicts, str)

    def test_from_json_str(self):
        list_input = [
                        {'id': 89, 'width': 10, 'height': 4},
                        {'id': 7, 'width': 1, 'height': 7}
                    ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)
        self.assertEqual(list_output, list_input)
