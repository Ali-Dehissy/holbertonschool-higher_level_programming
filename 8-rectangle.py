#!/usr/bin/python3
"""Creating rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class basegeometry"""
    def __init__(self, width, height):
        """Initializing instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
