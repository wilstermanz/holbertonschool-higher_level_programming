#!/usr/bin/python3
"""This module contains a class that defines a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square. Inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size (int): size of the side of a square
            x (int, optional): x coord position of square. Defaults to 0.
            y (int, optional): y coord position of square. Defaults to 0.
            id (_type_, optional): Desired ID for square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
