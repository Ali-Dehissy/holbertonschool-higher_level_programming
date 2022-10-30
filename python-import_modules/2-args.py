#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    j = 1
    if length - 1 == 0:
        print("{} arguments.".format(length - 1))
    elif length - 1 == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(length - 1))
    while j < length:
        print("{}: {}".format(j, argv[j]))
        j += 1
