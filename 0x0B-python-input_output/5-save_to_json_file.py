#!/usr/bin/python3
"""A function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file"""
    with open('filename', 'w') as op:
        json.dump(my_obj, op)
