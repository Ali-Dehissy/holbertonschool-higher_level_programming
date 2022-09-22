#!/usr/bin/python3
"""square"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """square constructor"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """tuple size of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        err = "position must be a tuple of 2 positive integers"
        if isinstance(value, tuple):
            if len(value) == 2 and value[0] >= 0 \
               and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError(err)
        else:
            raise TypeError(err)

    def area(self):
        """Ararea of the square"""
        return (self.size * self.size)

    def my_print(self):
        """printing based on the size"""
        if self.size == 0:
            print()
        else:
            for p0 in range(self.position[1]):
                print("\n", end="")
            for i in range(self.size):
                for p1 in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
