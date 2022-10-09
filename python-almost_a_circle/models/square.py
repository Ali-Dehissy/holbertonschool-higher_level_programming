#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square that inertis from rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initiliasing square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Printing  propreties of the square"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                          self.x,
                                                          self.y,
                                                          self.width))
