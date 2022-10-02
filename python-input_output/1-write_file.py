#!/usr/bin/python3
"""Number_of_lines function"""


def number_of_lines(filename=""):
    """Returns the number of lines of a txt file"""
    count = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            count += 1
        return count
