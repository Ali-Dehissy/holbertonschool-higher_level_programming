#!/usr/bin/python3
for j in range(0, 9):
    for k in range(j + 1, 10):
        if j == 8:
            print("{}{}".format(j, k))
        else:
            print("{}{}".format(j, k), end=", ")
