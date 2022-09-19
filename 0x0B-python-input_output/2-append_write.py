#!/usr/bin/python3
"""This module contains required functions for task 2"""


def append_write(filename="", text=""):
    """This function appends a string to the end of a file"""
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
    return len(text)
