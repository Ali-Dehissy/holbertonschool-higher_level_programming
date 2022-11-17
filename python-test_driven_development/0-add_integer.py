#!/usr/bin/python3
"""Adds integer module"""


def add_integer(a, b=98):
    """ Function that adds two strings"""
    if (type(a) != int and type(a) != float) or a != a:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float or b != b:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
