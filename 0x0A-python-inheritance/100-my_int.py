#!/usr/bin/python3

"""This module contains the MyInt class"""


class MyInt(int):
    """MyInt class"""

    def __init__(self, value):
        """Returns an instance of a Rectangle"""
        if isinstance(value, int):
            self.__int = value

    def __ne__(self, value):
        """Returns True"""
        return (True)

    def __eq__(self, value):
        """Returns False"""
        return (False)
