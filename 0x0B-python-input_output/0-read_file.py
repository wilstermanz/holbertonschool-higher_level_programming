#!/usr/bin/python3
"""This module contains the required functions for task 0"""


def read_file(filename=""):
    """This function opens and prints a file to stdout"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end='')
