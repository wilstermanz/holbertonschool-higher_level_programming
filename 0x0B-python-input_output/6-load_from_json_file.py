#!/usr/bin/python3
"""This module contains the required functions for task 6"""
import json


def load_from_json_file(filename):
    """This functions creates an object from a JSON file"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.loads(file.read())
