#!/usr/bin/python3
"""Creating a student class"""


class Student(object):
    """ A student class"""

    def __init__(self, first_name, last_name, age):
        """Return a student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the JSON format of a student"""
        return (self.__dict__)
