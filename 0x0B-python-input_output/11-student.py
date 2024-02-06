#!/usr/bin/python3
"""class Student module"""


class Student():
    """Student class defines a student."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        return self.__dict__

    def reload_from_json(self, json):
        for key in list(self.__dict__.keys()):
            if key not in json:
                delattr(self, key)
                for key, value in json.items():
                    setattr(self, key, value)
                    