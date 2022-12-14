#!/usr/bin/python3
"""
    This module contains a function that prints a square
"""


def print_square(size):
    """
    This function prints a square of given size

    Args:
        size (int): length of the side of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
