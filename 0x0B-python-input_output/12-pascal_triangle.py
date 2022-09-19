#!/usr/bin/python3
"""This module contains the required function for task 12"""


def pascal_triangle(n):
    """
        This function creates a list of lists representing
        pascal's triangle for a given number of rows
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(n - 1):
        row = triangle[i]
        temp1 = row + [0]
        temp2 = [0] + row
        new_row = []
        for j in range(len(temp1)):
            new_row.append(temp1[j] + temp2[j])
        triangle.append(new_row)

    return triangle
