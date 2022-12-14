#!/usr/bin/python3
"""
    Task 0
    Write a function that adds 2 integers.
    Prototype: def add_integer(a, b=98):
"""


def add_integer(a, b=98):
    """
        Adds two integers and returns the sum
    """
    if a is None:
        a = 0
    if b is None:
        b = 0
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
