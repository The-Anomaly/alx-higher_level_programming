#!/usr/bin/python3
"""
    Module to add two integers

    Functions:
        add_integers(object, object) -> int
"""


def add_integer(a, b=98):
    """ Definition of function that adds two integers or floats
    Args:
        param1 (int or float): the first number
        param2 (int or float): the second number. Defaults to 98

    Returns:
        int: the sum of the numbers

    Examples:
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
