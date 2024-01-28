#!/usr/bin/python3
"""
defining add module.
it has 1 function that returns the sum of two integer or floats.
It also includes a docstring that explains what this function does.
"""


def add_integer(a, b=98):
    """If only one argument is provided, it will be used as the first value,
    and The default value for `b` is 98.
    """
    if isinstance(a, float):
        a = int(a)
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if isinstance(b, float):
        b = int(b)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return a + b
