#!/usr/bin/python3
"""
    This module contains a function that formats a string
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text(string): The string to format

    Raises:
        TypeError: if text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    for i in range(len(text)):
        if text[i] is not " ":
            flag = 0
        if flag == 0:
            print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print("\n")
            flag = 1
