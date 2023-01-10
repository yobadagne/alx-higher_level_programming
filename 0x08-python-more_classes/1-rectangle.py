#!/usr/bin/pyhton3
""" A rectangle module """


class Rectangle:
    """A rectangle class"""

    def __init__(self, width=0, height=0):
        """Instantiate rectangle.

        Args:
            width(int): The width of the rectangle
            Height(int): The height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """get/set width"""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer ")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """get/set height"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer ")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
