#!/usr/bin/python3
"""Module for task 2"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class
    otherwise False
    """

    if type(obj) is a_class:
        return True
    return False
