#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for j in my_string:
        if j != 'c' and j != 'C':
            newstring = newstring + j
    return newstring
