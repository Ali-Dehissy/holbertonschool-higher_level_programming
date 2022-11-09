#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) <= ord('z') and ord(char) >= ord('a'):
            upp = chr(ord(char) - 32)
        else:
            upp = char
        print('{}'.format(upp), end='')

    print()
