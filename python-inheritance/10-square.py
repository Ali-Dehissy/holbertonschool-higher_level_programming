#!/usr/bin/python3
"""Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square"""
    def __init__(self, size):
        """Initializing an instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
