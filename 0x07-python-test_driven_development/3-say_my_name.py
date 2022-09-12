#!/usr/bin/python3
"""
    This module contains a function that takes a name as an argument
"""


def say_my_name(first_name, last_name=""):
    """
        This function takes a name as an argument, and prints it formatted

        Args:
            first_name (str): The first name
            last_name (str, optional): The last name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
