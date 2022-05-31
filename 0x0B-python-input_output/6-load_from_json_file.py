#!/usr/bin/python3
"""a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """function that writes an Object to a text file"""
    with open(filename, encoding='utf-8') as op:
        return(json.loads(op.read()))
