#!/usr/bin/python3
"""This module contains class: Student for task 9"""


class Student:
    """This class defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiates new students"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation of Student instance"""
        return vars(self)
