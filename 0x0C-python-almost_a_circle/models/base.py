#!/usr/bin/python3
"""This module contains the base class, task 1"""


class Base:
    """The base class for objects in the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes new objects"""
        if id is not None:
            self.id = id
        if id is None:
            self.__nb_objects += 1
