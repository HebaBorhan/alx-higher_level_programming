#!/usr/bin/python3
"""
defining Rectangle module
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle by width and height
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize Rectangle with width and height
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol

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
            rect = (str(self.print_symbol) * self.__width
                    + '\n') * self.__height
            # Remove the extra newline character at the end
            return rect[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(str(self.__width),
                                          str(self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
        return Rectangle.number_of_instances

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
