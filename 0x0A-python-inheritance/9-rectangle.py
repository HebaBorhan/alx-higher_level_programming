#!/usr/bin/python3
"""defining BaseGeometry module."""


class BaseGeometry:
    """class BaseGeometry."""

    def __init__(self):
        """Initialize BaseGeometry class."""
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """subclass Rectangle."""
    def __init__(self, width, height):
        """Initialize subclass Rectangle."""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
