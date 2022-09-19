#!/usr/bin/python3
"""This module contains the required functions for task 5"""
import json


def save_to_json_file(my_obj, filename):
    """This functions writes the JSON representation of an object to a file"""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
