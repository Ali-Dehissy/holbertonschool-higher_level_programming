#!/usr/bin/python3
"""A module class Mylist"""


class MyList(list):
    """Mylist class"""
    def print_sorted(self):
        """Printing instance"""
        print(sorted(self))
