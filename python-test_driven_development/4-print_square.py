#!/usr/bin/python3
"""Print_square module"""


def print_square(size):
    """Printing a square"""
    if type(size) != int or size != size:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for row in range(size):
            for column in range(size):
                print("#", end="")
            print()
