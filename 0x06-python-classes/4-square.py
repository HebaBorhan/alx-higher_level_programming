#!/usr/bin/python3
"""defining Square by Size module."""


class Square:
    """class Square that defines a square by Size."""

    def __init__(self, size=0):
        """Initialize the Square class with a given 'size' argument."""
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self._size = value

    def area(self):
        """Returns the area of the square."""
        return self._size ** 2
