#!/usr/bin/python3
"""Creating a student module"""


class Student:
    """A studentclass"""
    def __init__(self, first_name, last_name, age):
        """Initializing an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieving dictionary representation"""
        if type(attrs) is list and all(type(x) is str for x in attrs):
            dictionary = {}
            for j in attrs:
                if j in self.__dict__:
                    dictionary[j] = self.__dict__[j]
            return dictionary
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replacing all attributes"""
        for key, value in json.items():
            self.__dict__[key] = value
