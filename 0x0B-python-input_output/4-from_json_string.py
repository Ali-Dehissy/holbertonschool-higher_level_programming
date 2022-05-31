#!/usr/bin/python3
"""Defining the append_write function"""


def append_write(filename="", text=""):
    """Appends a string at end of a text file, returns # of characters written"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
