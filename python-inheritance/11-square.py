#!/usr/bin/python3
'''a module'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''This is a class'''

    def __init__(self, size):
        '''a function'''
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        '''a function'''
        return self.__size ** 2

    def __str__(self):
        '''a function'''
        return f"[Square] {self.__size}/{self.__size}"
