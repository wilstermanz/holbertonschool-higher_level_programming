#!/usr/bin/python3
"""
    Module for task 0
"""


def add_integer(a, b=98):
    """Adds two integers and returns the sum

    Args:
        a (int, float): First int to be added
        b (int, float, optional): Second int to be added. Defaults to 98.

    Raises:
        TypeError: if a or b is not type int or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
