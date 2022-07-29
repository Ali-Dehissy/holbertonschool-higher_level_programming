#!/usr/bin/python3

"""This module contains the Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    
    """A simple Square class"""
    
    def __init__(self, size):
        
        """Returns an instance"""
        
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
    
        """Returns informal string representation"""
        
        return "[Square] {}/{}".format(self.__size, self.__size)
