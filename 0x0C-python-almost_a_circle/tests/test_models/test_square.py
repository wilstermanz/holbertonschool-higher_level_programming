#!/usr/bin/python3
"""Unittest for class Base"""
from json import JSONDecodeError
import unittest
import os
from unittest.mock import patch
from io import StringIO
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Unit test suite for Square"""

    def test_docstrings(self):
        """Checks module and function docstrings"""
        modDocstring = __import__('models').square.__doc__
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertIsNotNone(Square.area.__doc__)
        self.assertIsNotNone(Square.display.__doc__)
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_simple_testcases(self):
        """Checks for simple, correct test cases"""
        r1 = Square(10, 0, 0, 1)
        self.assertEqual(r1.id, 1)
        r2 = Square(2, 0, 0, 2)
        self.assertEqual(r2.id, 2)
        r3 = Square(10, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_bad_input(self):
        """Tests with improper number of inputs"""
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

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
        s = Square(1)
        self.assertEqual(s.area(), 1)
        s = Square(2)
        self.assertEqual(s.area(), 4)
        s = Square(8, 0, 0, 12)
        self.assertEqual(s.area(), 64)

    def test_display(self):
        """Tests display method"""
        s1 = Square(2)
        s2 = Square(3, 1, 1)
        with patch('sys.stdout', new=StringIO()) as outstream:
            s1.display()
            self.assertEqual('##\n##\n', outstream.getvalue())
        with patch('sys.stdout', new=StringIO()) as outstream:
            s2.display()
            self.assertEqual('\n ###\n ###\n ###\n', outstream.getvalue())

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

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 1)
        s1_dictionary = s1.to_dictionary()
        test_d = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(s1_dictionary, test_d)

    def test_to_json_string(self):
        """Tests to_json_str static method"""
        s1 = Square(10, 7, 2, 1)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        json_test = '[{"id": 1, "x": 7, "y": 2, "size": 10}]'
        self.assertEqual(json_dictionary, json_test)
        self.assertIsInstance(json_dictionary, str)

    def test_to_json_string_bad(self):
        """Tests bad input in json_str method"""
        r1 = Square(10, 2, 8, 1)
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')
        self.assertIsInstance(json_dictionary, str)
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')
        self.assertIsInstance(json_dictionary, str)

    def test_save_to_file(self):
        """Test save_to_file method"""
        s1 = Square(10, 2, 8, 1)
        s2 = Square(4, 0, 0, 2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            list_dicts = file.read()
        test_list = str('[{"id": 1, "x": 2, "y": 8, "size": 10}, '
                        '{"id": 2, "x": 0, "y": 0, "size": 4}]')
        self.assertEqual(list_dicts, test_list)
        self.assertIsInstance(list_dicts, str)
        self.assertTrue(os.path.isfile('Square.json'))

    def test_save_to_file_bad(self):
        """Tests bad input to save_to_file method"""
        Square.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            list_dicts = file.read()
        self.assertEqual(list_dicts, '[]')
        self.assertTrue(os.path.isfile('Square.json'))

    def test_from_json_str(self):
        """Test from_json_str method"""
        list_input = [
                        {'id': 89, 'size': 10},
                        {'id': 7, 'size': 200}
                    ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)
        self.assertEqual(list_output, list_input)

    def test_from_json_str_bad(self):
        output = Square.from_json_string(None)
        self.assertIsInstance(output, list)
        self.assertEqual(output, [])

    def test_create(self):
        """Test for create method"""
        s1 = Square(3, 1, 0, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)

    def test_create_bad(self):
        s1 = Square(5, 1, 0, 1)
        s1_dictionary = s1.to_dictionary()
        with self.assertRaises(TypeError):
            Square.create(s1_dictionary)
        s1_dictionary = {'bad', 'dict'}
        with self.assertRaises(TypeError):
            Square.create(s1_dictionary)
        with self.assertRaises(TypeError):
            Square.create(**s1_dictionary)
        with self.assertRaises(TypeError):
            Square.create(None)

    def test_load_from_file(self):
        """Test load_from_file method"""
        s1 = Square(10, 2, 8, 1)
        s2 = Square(2, 0, 0, 2)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        n1 = list_squares_output[0]
        n2 = list_squares_output[1]
        self.assertEqual(str(s1), str(n1))
        self.assertNotEqual(s1, n1)
        self.assertEqual(str(s2), str(n2))
        self.assertNotEqual(s2, n2)

    def test_load_from_file_bad(self):
        """Tests when load_from_file cannot find a file"""
        os.remove("Square.json")
        self.assertFalse(os.path.isfile('Square.json'))
        output = Square.load_from_file()
        self.assertIsInstance(output, list)
        self.assertEqual(output, [])
        with open("Square.json", 'w', encoding="utf-8") as file:
            file.write("")
        self.assertTrue(os.path.isfile('Rectangle.json'))
        output = Square.load_from_file()
        self.assertIsInstance(output, list)
        self.assertEqual(output, [])
        with open('Square.json', 'w', encoding="utf-8") as file:
            file.write("Bad format")
        with self.assertRaises(JSONDecodeError):
            output = Square.load_from_file()


if __name__ == '__main__':
    unittest.main()
