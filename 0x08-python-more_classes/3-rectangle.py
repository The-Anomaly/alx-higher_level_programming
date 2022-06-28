#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize attributes

        Args:
            width: value to initialize to `width`
            height: value to initialize to `height`

        Raises:
            TypeError: when `width` isn't an integer
            ValueError: `width` is less than 0
            TypeError: when `height` isn't an integer
            ValueError: `height` is less than 0

        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the value of `width`

        Returns:
           width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width to `value`

        Args:
            value (int): value to set set

        Raise:
            TypeError: if `value` isn't an integer
            ValueError: if `value` is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieves the value of `height`

        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height to `value`

        Args:
            value (int): value to set set

        Raise:
            TypeError: if `value` isn't an integer
            ValueError: if `value` is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculates the area of the rectangle

        Returns:
            area
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle

        Returns:
            perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * (self.__width + self.__height))

    def __str__(self):
        """print the rectangle with the character #

        Returns:
            0 if width or height is 0
            {string}: rectangle containing `#`
        """
        rect = ""

        if self.__width == 0 or self.__height == 0:
            return 0

        for i in range(self.__height):
            rect = rect + ("#"*self.__width)
            if i < (self.__height - 1):
                rect = rect + "\n"
        return rect
