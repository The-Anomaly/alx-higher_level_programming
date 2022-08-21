#!/usr/bin/python3
"""
    Module that prints a square with the character #.

    Functions:
        print_square(int)
"""


def print_square(size):
    """ Definition for a function that prints a square with the character #.

    Args:
        size (int): size length of the square

    Returns:
        Prints a square with the character #
    """

    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        print("#"*size)
