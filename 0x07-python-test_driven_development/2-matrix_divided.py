#!/usr/bin/python3
"""
    This contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
        This function divides all elements of a matrix

        Args:
            matrix (matrix of ints or floats): _description_
            div (int or float): _description_
    """

    err1 = "div must be a number"
    err2 = "division by zero"
    err3 = "Each row of the matrix must have the same size"
    err4 = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in [int, float]:
        raise TypeError(err1)
    if div == 0:
        raise ZeroDivisionError(err2)
    out = []
    rowLen = len(matrix[0])
    for row in matrix:
        if len(row) != rowLen:
            raise TypeError(err3)
        for item in row:
            if type(item) not in [float, int]:
                raise TypeError(err4)
        out.append(list(map(lambda n: round(n/div, 2), row)))
    return out
