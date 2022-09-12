#!/usr/bin/python3
"""
    This module contains a function that formats a string
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text(string): The string to format
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        print(i, end="")
        if i in [".", "?", ":"]:
            print("")
            print("")
