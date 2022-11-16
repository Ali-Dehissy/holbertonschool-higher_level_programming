#!/usr/bin/python3
"""Creating a class named rectangle"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def height(self):
        """Getting the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Getting the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returning the area of the class instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Returning the permimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returning the string representation of the class instance"""
        stringrep = ""
        if self.__width == 0 or self.__height == 0:
            return stringrep
        for row in range(self.__height):
            for column in range(self.__width):
                stringrep += str(self.print_symbol)
            if row < self.__height - 1:
                stringrep += "\n"
        return stringrep

    def __repr__(self):
        """Returns the string representation of the class isntance"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Finalizing when the instance has been deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
