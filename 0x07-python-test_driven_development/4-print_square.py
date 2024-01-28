#!/usr/bin/python3
"""
printing square by Size module.
it contains a function that prints square.
It also includes a docstring that explains what this function does.
"""


def print_square(size):
    """prints # according to square size.
    prints empty line if size is 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")

    if size == 0:
        print("")
    else:
        for i in range(int(size)):
            for j in range(int(size)):
                print("#", end="")
            print("")
