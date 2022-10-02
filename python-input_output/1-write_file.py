#!/usr/bin/python3
"""Number_of_lines function"""


def write_file(filename="", text=""):
    """Returns the number of lines of a txt file"""

    with open(filename, mode="w",  encoding="utf-8") as myfile:
        myfile.write(text)
        return len(text)
