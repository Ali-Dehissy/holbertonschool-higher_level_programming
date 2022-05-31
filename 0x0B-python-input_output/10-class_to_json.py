#!/usr/bin/python3
"""Creating a function class_to_json that return a JSON from a class"""


def class_to_json(obj):
    """Returns the dictionary description of object"""
    
    return obj.__dict__
