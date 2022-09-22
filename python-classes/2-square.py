#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""square"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """Square constructor"""
        
        self.set_size = size

    @property
    def get_size(self):
        """int size of the square"""
        return (self.__size)

    @get_size.setter
    def set_size(self, size):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise ValueError("size must be an integer")
