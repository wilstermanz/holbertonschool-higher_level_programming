#!/usr/bin/python3
"""This module contains the functions for task 1"""


def write_file(filename="", text=""):
    """
        This functions writes a string to a text file and returns
        the number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
    return len(text)
