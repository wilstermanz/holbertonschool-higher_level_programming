#!/usr/bin/python3
"""Module for task 8"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Defines a rectangle"""

    def __init__(self, width, height):
        """Sets width and height of new objects"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
