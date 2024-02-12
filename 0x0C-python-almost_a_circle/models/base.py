#!/usr/bin/python3
"""base module"""


class Base:
    """creating Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """initialise function"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
