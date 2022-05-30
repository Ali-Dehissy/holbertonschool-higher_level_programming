#!/usr/bin/python3
"""A class named inherits_from"""


def inherits_from(obj, a_class):
    """Returns True or False based on inheritance"""
    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True
    else:
        return False
