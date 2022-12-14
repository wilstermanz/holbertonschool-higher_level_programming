#!/usr/bin/python3
"""Contains Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle, inherits from class Base"""
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
        """Sets str value of the rectangle"""
        return (f"[Rectangle] ({self.id}) "
                f"{self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Updates the rectangle's attributes"""
        if args is not None and len(args) != 0:
            attr_list = ['id', 'width', 'height', 'x', 'y']
            for arg_no in range(len(args)):
                setattr(self, attr_list[arg_no], args[arg_no])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of a Rectangle"""
        my_dict = {}
        for key, value in vars(self).items():
            key = key.replace("_Rectangle__", "")
            my_dict[key] = value
        return my_dict
