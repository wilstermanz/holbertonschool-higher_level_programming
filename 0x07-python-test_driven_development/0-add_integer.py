#!/usr/bin/python3
"""Returns the sum of two integers, or floats typecasted as int
"""


def add_integer(a, b=98):
    """Math takes place here"""
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if a is None:
        raise TypeError("'NoneType' object is not subscriptable")
    if b is None:
        raise TypeError("'NoneType' object is not subscriptable")
    """
    if type(a) is complex:
        raise TypeError("a must be an integer")
    if type(b) is complex:
        raise TypeError("b must be an integer")
    """
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")

    return(a + b)
