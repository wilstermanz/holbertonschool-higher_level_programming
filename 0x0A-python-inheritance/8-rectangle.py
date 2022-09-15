#!/usr/bin/python3
"""Module for task 8"""


class BaseGeometry:
    """Defines geometry"""

    def area(self):
        """This doesn't do anything"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks for valid integers"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Defines a rectangle"""

    def __init__(self, width, height):
        """Sets width and height of new objects"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
