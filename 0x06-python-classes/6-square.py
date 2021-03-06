#!/usr/bin/python3
"""Square class"""


class Square:
    """Square Class
        """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size

        if type(position) is not tuple or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    def area(self):
        """
        Returns area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """
    Returns print of square
        """
        if self.__size == 0:
            print("")
            return

        for x in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for t in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
