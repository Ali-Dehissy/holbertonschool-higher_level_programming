#!/usr/bin/python3

"""This module contains 
the add_atribute function"""


def add_attribute(object, attribute, value):
    """Adds anew attribute"""
    
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, value)
