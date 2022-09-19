#!/usr/bin/python3
"""This module contains required functions for task 4"""
import json


def from_json_string(my_obj):
    """This module returns an object from its JSON representation"""
    return json.loads(my_obj)
