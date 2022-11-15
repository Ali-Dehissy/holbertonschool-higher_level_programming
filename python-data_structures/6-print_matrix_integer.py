#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        var = 0
        for j in row:
            var += 1
            print('{:d}'.format(j), end=(" " if var < len(row) else ""))
        print()
