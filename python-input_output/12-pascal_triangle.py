#!/usr/bin/python3
"""Pascal"""

def pascal_triangle(n):
    """Returning a list of integers representing the triangle"""
    var = []
    if n <= 0:
        return var
    if n == 1:
        return [[1]]

    var = [[1]]
    for i in range(n-1):
        var.append([a+b for a, b in zip([0] + var[-1], var[-1] + [0])])
    return var
