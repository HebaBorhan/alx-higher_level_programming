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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation of object in a file"""
        if list_objs is None:
            list_objs = []

        list_objs = [obj.to_dictionary() for obj in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """return a list of objects from a JSON string"""
        if json_string is None or json_string == []:
            return "[]"

        return json.loads(json_string)
