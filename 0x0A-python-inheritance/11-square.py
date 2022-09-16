#!/usr/bin/python3
"""Module for task 9"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size):
        """Initializes new Square objects"""
        self.integer_validator("size", size)
        self.__size = size
        self._Rectangle__width = size
        self._Rectangle__height = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
