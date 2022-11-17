#!/usr/bin/python3
"""Matrix module"""


def matrix_divided(matrix, div):
    """Dividing all elements of a matrix"""
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/fl\
oats")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for row in matrix:
        for k in row:
            if (type(k) != int and type(k) != float) or k != k:
                raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div != div or div == float('inf'):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    nonemptyflag = 0
    for row in matrix:
        if len(row) != 0:
            nonemptyflag = 1
    if nonemptyflag == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    return [[round(i/div, 2) for i in row] for row in (matrix)]
