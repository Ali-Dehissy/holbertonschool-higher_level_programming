#!/usr/bin/python3
"""Text_identification module"""


def text_indentation(text):
    """Printing identified text"""
    if type(text) != str:
        raise TypeError("text must be a string")
    flag = 0
    newstring = ""
    for i in text:
        if flag == 1:
            newstring = ""
            flag = 0
        if i not in "?:.":
            newstring += i
        else:
            newstring += i
            print(newstring.strip())
            print()
            flag = 1
    if flag == 0 and '\n' not in newstring:
        print(newstring.strip(), end="")
    elif flag == 0:
        print(newstring.strip())
