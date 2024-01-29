#!/usr/bin/python3
"""
defining Rectangle module
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle by width and height
    """
    def __init__(self, width=0, height=0):
        """Initialize Rectangle with width and height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = ("#" * self.__width + '\n') * self.__height
            # Remove the extra newline character at the end
            return rect[:-1]
