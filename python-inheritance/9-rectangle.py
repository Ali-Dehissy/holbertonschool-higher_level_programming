#!/usr/bin/python3
"""Creating rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Basegeometry class"""
    def __init__(self, width, height):
        """initializes an instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returning area of instance"""
        return self.__width * self.__height

    def __str__(self):
        """Returning string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
