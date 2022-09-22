#!/usr/bin/python3
"""square"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """square constructor"""
        self.size = size

    @property
    def size(self):
        """int size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise ValueError("size must be an integer")

    def area(self):
        """area of the square"""
        return (self.size * self.size)

    def my_print(self):
        """printing based of the size
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
