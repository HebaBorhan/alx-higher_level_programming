#!/usr/bin/python3
"""base module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert list of dictionaries into json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)
