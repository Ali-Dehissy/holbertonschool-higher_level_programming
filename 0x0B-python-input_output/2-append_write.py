#!/usr/bin/python3
"""Defining the read_lines function"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding='utf-8') as file:
        if nb_lines <= 0:
            for line in file:
                print(line, end="")
        else:
            for line in range(nb_lines):
                print(file.readline(), end="")
