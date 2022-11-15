#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    fin = []
    for j in my_list:
        fin.append(True if not j % 2 else False)
    return fin
