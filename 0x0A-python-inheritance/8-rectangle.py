#!/usr/bin/python3
"""Rectangle class
that inherits from BaseGeometry
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class
    A simple empty Rectangle class
    """

    def __init__(self, width, height):
        """Returns an instance of a Rectangle
            width : The width of the Rectangle
            height : The height of the Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
