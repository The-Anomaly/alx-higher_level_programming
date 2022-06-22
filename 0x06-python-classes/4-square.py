#!/usr/bin/python3
"""A square class"""


class Square:
    """Derives a square"""
    def __init__(self, size=0):
        """Initialize attributes

        Args:
            self (int): value to initialize to `size`

        Note:
            Do not include the `self` paramtere in the ``Args`` section.

        Raises:
            TypeError: when `size` isn't an integer
            ValueError: `size` is less than 0

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate area of the square

        Returns:
            The area of the square

        """

        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the value of `size`

        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size to `value`

        Args:
            value (int): value to set set

        Raise:
            TypeError: if `value` isn't an integer
            ValueError: if `value` is less than 0

        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
