#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize class rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        """Width proprety"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting width proprety"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height proprety"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height proprety"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """Returns area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Instance of the rectangle"""
        for y_coor in range(0, self.y):
            print()
        for row in range(self.height):
            for x_coor in range(self.x):
                print(' ', end='')
            for col in range(self.width):
                print('#', end='')
            print()
    def __str__(self):
        """Printing rectangle propreties"""
        return ("[{}] ({}) {}/{:d} - {:d}/{:d}".format(self.__class__.__name__,
                                                       self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height))
    def update(self, *args, **kwargs):
        """Updateing instance using setter method"""
        place = 0
        if (args is not None) and (len(args) > 0):
            for arg in args:
                if place == 0:
                    self.id = arg
                elif place == 1:
                    self.width = arg
                elif place == 2:
                    self.height = arg
                elif place == 3:
                    self.x = arg
                elif place == 4:
                    self.y = arg
                else:
                    break
                place += 1

        elif kwargs is not None:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns dictionnary of class rectangle"""
        return ({'id': self.id, 'width': self.width, 'height': self.height,
                 'x': self.x, 'y': self.y})
