#!/usr/bin/python3
"""Inherits from function"""


def inherits_from(obj, a_class):
    """returns true or fasle based on the inheritance"""
    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True
    else:
        return False
