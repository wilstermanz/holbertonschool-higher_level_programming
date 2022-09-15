#!/usr/bin/python3
"""Module for task 4"""


def inherits_from(obj, a_class):
    """
    Write a function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ; otherwise False.
    """

    return issubclass(obj, a_class)
