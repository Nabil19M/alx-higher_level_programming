#!/usr/bin/python3
"""
    Defining function for matrix dividing
"""


def matrix_divided(matrix, div):
    """ using iterators to divide matrix numbers

    Args:
        matrix (int / float): Matrix should be divided
        div (int / float): the divisior

    Raises:
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        ZeroDivisionError: _description_

    Returns:
        new matrix after division
    """
    new_matrix = []
    length = len(matrix[0])
    for i in matrix:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of"
                                "integers/floats")
        if len(i) != length:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for col in matrix:
        result = list(map(lambda x: round(x / div, 2), col))
        new_matrix.append(result)
    return new_matrix
