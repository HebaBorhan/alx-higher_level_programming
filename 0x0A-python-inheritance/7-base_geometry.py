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
