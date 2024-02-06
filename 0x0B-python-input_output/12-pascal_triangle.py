#!/usr/bin/python3
"""pascal triangle module"""


def pascal_triangle(n):
    """Returns list of lists of integers representing Pascal triangle of n."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return []
    else:
        row = [1] * (n + 1)
        result = [row]
        return result
