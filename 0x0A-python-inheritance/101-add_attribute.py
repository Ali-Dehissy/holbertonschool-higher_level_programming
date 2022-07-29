#!/usr/bin/python3

"""This module contains the add_atribute function"""


def add_attribute(obj, name, value):
    """Returns Nothing"""

    if str(type(obj)).find("__main__") != -1:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
