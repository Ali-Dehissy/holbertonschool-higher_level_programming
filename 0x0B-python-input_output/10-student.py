#!/usr/bin/python3
"""Creating a student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Json method that retrieves
        a dictionary representation of a Student instance"""
        dict = {}
        if type(attrs) is not list:
            return self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__:
                    dict[i] = self.__dict__[i]
            return(dict)
