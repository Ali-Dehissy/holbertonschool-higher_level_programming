#!/usr/bin/python3
"""Creates a class named Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class named Square
    size : size of square
    area : finds the area
    """
    def __init__(self, size):
        """Initializes an instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
