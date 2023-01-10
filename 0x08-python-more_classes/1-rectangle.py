#!/usr/bin/pyhton3
""" A rectangle module """


class Rectangle:
    def __init__(self, width=0, height=0):
        if type(height) is not int:
            raise TypeError("height must be an integer ")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = height
        if type(width) is not int:
            raise TypeError("height must be an integer ")
        elif width < 0:
            raise ValueError("height must be >= 0")
        else:
            self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer ")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer ")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
