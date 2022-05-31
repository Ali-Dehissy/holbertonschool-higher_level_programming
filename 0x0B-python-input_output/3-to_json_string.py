#!/usr/bin/python3
"""Defining the write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns number of characters written"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
