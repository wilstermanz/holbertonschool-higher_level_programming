#!/usr/bin/python3
"""Module for task 9"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle"""

    def __init__(self, width, height):
        """Sets width and height of new objects"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Defines the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Returns rectangle parameters"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def print(self):
        """Prints rectangle parameters"""

        print("[Rectangle] {}/{}".format(self.__width, self.__height))
