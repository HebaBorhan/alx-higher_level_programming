#!/usr/bin/python3
"""defining Square by Size module."""


class Square:
    """class Square that defines a square by Size."""

    def __init__(self, size=0):
        """Initialize the Square class with a given 'size' argument."""

        if not isinstance(size, int):
            raise TypeError("Size must be an integer")

        if size < 0:
            raise ValueError("Size must be >= 0")

        self.__size = size
        
