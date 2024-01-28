#!/usr/bin/python3
"""
say_my_name module.
it contains a function that prints first and last name.
It also includes a docstring that explains what this function does.
"""


def say_my_name(first_name, last_name=""):
    """prints first and last name.
    default value for last name is "".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
