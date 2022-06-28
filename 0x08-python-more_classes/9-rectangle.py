#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        """create the rectangle with the character #

        Returns:
            {string}: rectangle containing `print_symbol`
        """
        rect = ""

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            rect = rect + (str(self.print_symbol)*self.__width)
            if i < (self.__height - 1):
                rect = rect + "\n"
        return rect

    def __repr__(self):
        """string representation for new instance of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """delete instance of the rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Check for bigger rectangle based on area

        Args:
            rect_1 (Rectangle)
            rect_2 (Rectangle)

        Raise:
            TypeError: if `rect_1` isn't a Rectangle
            TypeError: if `rect_2` isn't a Rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Create a square of width and height `size`

        Args:
            size
        """
        return cls(size, size)
