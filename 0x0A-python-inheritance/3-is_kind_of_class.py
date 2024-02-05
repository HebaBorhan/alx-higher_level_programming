#!/usr/bin/python3
"""
module checking if object instance of a spesified class
"""


def is_kind_of_class(obj, a_class):
    """function returns True if object an instance of specified class
    or if the object is instance of class that inherited the specified class 
    otherwise False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
