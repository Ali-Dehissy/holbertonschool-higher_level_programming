#!/usr/bin/python3
"""From_json_string function"""


import json


def from_json_string(my_str):
    """Returns the JSON representation of an obj string"""
    return json.loads(my_str)
