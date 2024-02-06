#!/usr/bin/python3
"""class to json module"""


def class_to_json(obj):
    """returns dictionary description for JSON serialization of object"""
    return obj.__dict__
