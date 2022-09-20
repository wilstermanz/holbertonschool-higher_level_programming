#!/usr/bin/python3
"""Contains Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes new rectangles

        Args:
            width (int): width of rectangle
            height (int): height of the rectangle
            x (int, optional): position x of rectangle. Defaults to 0.
            y (int, optional): position y of rectangle. Defaults to 0.
            id (int, optional): Inherits from super.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Prints the rectangle to stdout"""
        print('\n' * self.__y, end='')
        for rows in range(self.__height):
            print((' ' * self.__x)+('#' * self.__width))

    def __str__(self):
        return (f"[Rectangle] ({self.id}) "
                f"{self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def update(self, *args):
        """Updates the rectangle's attributes"""
        numArgs = len(args)
        if numArgs > 0:
            self.id = args[0]
        if numArgs > 1:
            self.__width = args[1]
        if numArgs > 2:
            self.__height = args[2]
        if numArgs > 3:
            self.__x = args[3]
        if numArgs > 4:
            self.__y = args[4]
