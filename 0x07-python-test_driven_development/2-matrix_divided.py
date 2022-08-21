#!/usr/bin/python3
""" Module to divide elements of a matrix

    Functions:
        matrix_divided(list, int) -> list

"""


def matrix_divided(matrix, div):
    """ Definition of function that divides a matrix

    Args:
        matrix (list of lists of int or float): the matrix
        div (int or float): the divisor

    Returns:
        list: a new matrix
    """
    for i, m in enumerate(matrix):
        prev = i-1
        if prev >= 0 and prev < len(matrix) and len(m) != len(matrix[prev]):
            raise TypeError("Each row of the matrix must have the same size")
        for n in m:
            if type(n) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(int(j)/div, 2) for j in i] for i in matrix]
