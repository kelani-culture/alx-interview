#!/usr/bin/python3

"""
Rotates an n x n 2D matrix 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The n x n matrix to rotate.
                                      It is modified in place.

    Example:
        Input:
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        Output:
        [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]

    Notes:
        - The function does not return anything.
        - The input matrix is assumed to be non-empty and have 2 dimensions.
    """
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]

            # Left -> Top
            matrix[first][i] = matrix[last - offset][first]

            # Bottom -> Left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Right -> Bottom
            matrix[last][last - offset] = matrix[i][last]

            # Top -> Right
            matrix[i][last] = top
