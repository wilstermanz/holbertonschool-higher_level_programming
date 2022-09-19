#!/usr/bin/python3
"""This module contains class: Student for task 10"""


class Student:
    """This class defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiates new students"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of Student instance"""
        if attrs is None:
            return vars(self)
        json_dict = {}
        for key, value in vars(self).items():
            if key in attrs:
                json_dict[key] = value
        return json_dict
