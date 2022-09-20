#!/usr/bin/python3
"""This module contains the base class, task 1"""
import json


class Base:
    """The base class for objects in the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes new objects"""
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes a JSON representation of list_objs to a file"""
        my_dict = []
        if list_objs is not None:
            for obj in list_objs:
                my_dict.append(obj.to_dictionary())
        with open(cls.__name__+".json", 'w', encoding='utf-8') as file:
            file.write(json.dumps(my_dict))
