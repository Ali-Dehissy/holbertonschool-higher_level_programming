#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    pascal = []
    row = []
    for j in range(n):
        row = [1]
        if j > 0:
            for k in range(i):
                row.append(sum(pascal[-1][k:k+2]))
        pascal.append(row)
    return pascal
