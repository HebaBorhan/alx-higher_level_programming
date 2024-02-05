#!/usr/bin/python3
"""
module checking if object instance of a class inherited specifid cls
"""


def inherits_from(obj, a_class):
    """function returns True if object is an instance of a class
    that inherited the specified class
    otherwise False"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
