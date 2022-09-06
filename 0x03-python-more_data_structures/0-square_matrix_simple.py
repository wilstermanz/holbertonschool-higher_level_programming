#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    out = []
    for i in matrix:
        out.append(list(map(lambda n: n**2, i)))
    return out
