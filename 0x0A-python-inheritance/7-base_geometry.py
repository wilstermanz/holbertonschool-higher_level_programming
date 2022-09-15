#!/usr/bin/python3
"""Module for task 7"""


class BaseGeometry:
    """Defines something"""

    def area(self):
        """This doesn't do anything"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks for valid integers"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
