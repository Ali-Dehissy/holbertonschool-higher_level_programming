#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = []
    for j in my_list:
        newlist.append(j)
    if idx < 0:
        return newlist
    elif idx > len(my_list) - 1:
        return newlist
    else:
        newlist[idc] = element
        return newlist
