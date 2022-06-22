#!/usr/bin/python3
"""A square class"""


class Square:
    """Derives a square"""
    def __init__(self, size):
        """Initialize attributes
        Args:
            self (int): value to initialize to `size`
        Note:
            Do not include the `self` paramtere in the ``Args`` section.
        """
        self.__size = size
