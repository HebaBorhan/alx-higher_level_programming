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


class Square(BaseGeometry):
    """subclass Square."""
    def __init__(self, size):
        """Initialize subclass Square."""
        super().__init__()
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        return self.__size ** 2
