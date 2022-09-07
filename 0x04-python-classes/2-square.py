#!/usr/bin/python3
"""Contains info relating to square classes"""


class Square:
    """Creates a square and defines the length of a side"""

    def __init__(self, size=0):
        """Initializes square, sets size, and checks for size errors"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
