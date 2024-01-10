#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None

    else:
        new_matrix = []

        for row in matrix:
            new_row = list(map(lambda x: x**2, row))
            new_matrix.append(new_row)

        return new_matrix
