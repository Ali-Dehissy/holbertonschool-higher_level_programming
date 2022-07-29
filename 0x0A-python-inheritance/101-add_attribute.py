#!/usr/bin/python3
"""
Adds an attribute
"""


def add_attribute(object, attribute, value):
    """
        Adds a new attribute to an object
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, value)
