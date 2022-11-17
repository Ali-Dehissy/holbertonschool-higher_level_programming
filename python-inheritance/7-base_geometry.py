#!/usr/bin/python3
"""A class named BaseGeometry"""


class BaseGeometry:
    """A class"""
    def area(self):
        """Raising an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Input"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
