#!/usr/bin/python3
"""Square class"""


class Square:
    """Square Class
    This square has a size an area
    """

    def __eq__(self, other):
        return self.__size == other.__size

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __ne__(self, other):
        return self.size != other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __init__(self, size=0):
        """
        Initializing square
        """
        self.__size = size

    def area(self):
        """
        Returns area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
