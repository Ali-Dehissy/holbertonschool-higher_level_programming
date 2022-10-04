#!/usr/bin/python3
"""Returns JSON dictionary"""


def class_to_json(obj):
    """Returns the dictionary description of obj"""
    return obj.__dict__
