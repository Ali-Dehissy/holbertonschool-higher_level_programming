#!/usr/bin/python3
"""Creating a student module"""


class Student:
    """A student class"""
    def __init__(self, first_name, last_name, age):
        """Initializing an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieving the dictionary representation"""
        if type(attrs) is list and all(type(x) is str for x in attrs):
            dictionary = {}
            for i in attrs:
                if i in self.__dict__:
                    dictionary[i] = self.__dict__[i]
            return dictionary
        else:
            return self.__dict__
