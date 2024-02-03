#!/usr/bin/python3
"""Module matrix division
it contains a function that devide matrix.
It also includes a docstring that explains what this function does.
"""


def matrix_divided(matrix, div):
    """Divide each element of a matrix by the value in the second parameter.
    int or floats.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
