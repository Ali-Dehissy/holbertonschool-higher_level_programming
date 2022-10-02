#!/usr/bin/python3
"""Read_file function"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end="")
