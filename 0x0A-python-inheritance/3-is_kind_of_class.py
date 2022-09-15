#!/usr/bin/python3
"""Module for task 3"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    """

    if type(obj) is a_class:
        return True
    return issubclass(obj, a_class)
