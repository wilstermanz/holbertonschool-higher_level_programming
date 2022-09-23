#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base
import os


class TestRectangle(unittest.TestCase):
    """Unit test suite for Rectangle"""

    def test_docstrings(self):
        """Checks module and function docstrings"""
        modDocstring = __import__('models').rectangle.__doc__
        self.assertIsNotNone(modDocstring)
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

    def test_objects(self):
        """Tests for created objects"""
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)
        Rectangle(2, 4)
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_simple_testcases(self):
        """Checks for simple, correct test cases"""
        r1 = Rectangle(10, 2, 0, 0, 1)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10, 0, 0, 2)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_bad_input(self):
        """Checks for improper number of inputs"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

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

    def test_display(self):
        """Tests display method"""
        r1 = Rectangle(2, 2)
        r2 = Rectangle(2, 3, 1, 1)
        with patch('sys.stdout', new=StringIO()) as outstream:
            r1.display()
            self.assertEqual('##\n##\n', outstream.getvalue())
        with patch('sys.stdout', new=StringIO()) as outstream:
            r2.display()
            self.assertEqual('\n ##\n ##\n ##\n', outstream.getvalue())

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

    def test_to_json_string_bad(self):
        """Tests bad input in json_str method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')
        self.assertIsInstance(json_dictionary, str)
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')
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
        self.assertTrue(os.path.isfile('Rectangle.json'))

    def test_save_to_file_bad(self):
        """Tests bad input to save_to_file method"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            list_dicts = file.read()
        self.assertEqual(list_dicts, '[]')
        self.assertTrue(os.path.isfile('Rectangle.json'))

    def test_from_json_str(self):
        """Test from_json_str method"""
        list_input = [
                        {'id': 89, 'width': 10, 'height': 4},
                        {'id': 7, 'width': 1, 'height': 7}
                    ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)
        self.assertEqual(list_output, list_input)

    def test_from_json_str_bad(self):
        output = Rectangle.from_json_string(None)
        self.assertIsInstance(output, list)
        self.assertEqual(output, [])

    def test_create(self):
        """Test for create method"""
        r1 = Rectangle(3, 5, 1, 0, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 1, 0, 0, 1)
        r2 = Rectangle.create()
        self.assertEqual(str(r1), str(r2))

    def test_create_bad(self):
        r1 = Rectangle(3, 5, 1, 0, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(TypeError):
            Rectangle.create(r1_dictionary)
        r1_dictionary = {'bad', 'dict'}
        with self.assertRaises(TypeError):
            Rectangle.create(r1_dictionary)
        with self.assertRaises(TypeError):
            Rectangle.create(**r1_dictionary)
        with self.assertRaises(TypeError):
            Rectangle.create(None)

    def test_load_from_file(self):
        """Test load_from_file method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        n1 = list_rectangles_output[0]
        n2 = list_rectangles_output[1]
        self.assertEqual(str(r1), str(n1))
        self.assertNotEqual(r1, n1)
        self.assertEqual(str(r2), str(n2))
        self.assertNotEqual(r2, n2)

    def test_load_from_file_bad(self):
        """Tests when load_from_file cannot find a file"""
        os.remove("Rectangle.json")
        self.assertFalse(os.path.isfile('Rectangle.json'))
        output = Rectangle.load_from_file()
        self.assertIsInstance(output, list)
        self.assertEqual(output, [])


if __name__ == '__main__':
    unittest.main()
