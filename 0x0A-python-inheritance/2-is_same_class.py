#!/usr/bin/python3
"""
module to if instance of a spesified class
"""


def is_same_class(obj, a_class):
    """function returns True if object exactly an instance of specified class
    otherwise False"""
    if type(obj) is a_class:
        return True
    else:
        return False
