#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """A class named Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """Height instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Width instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Gets the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the permimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns the string representation"""
        stringrep = ""
        if self.__width == 0 or self.__height == 0:
            return stringrep
        for row in range(self.__height):
            for column in range(self.__width):
                stringrep += "#"
            if row < self.__height - 1:
                stringrep += "\n"
        return stringrep

    def __repr__(self):
        """Returns the string representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Finalizer when instance is deleted"""
        print("Bye rectangle...")
