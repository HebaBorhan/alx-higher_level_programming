#!/usr/bin/python3
"""class Student module"""


class Student():
    """Student class defines a student."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the attributes of an instance as a JSON string."""
        if attrs is None:
            return self.__dict__
        
        filter_attrs = {}
        for attr in attrs:
            if hasattr(self, attr):
                filter_attrs[attr] = getattr(self, attr)
        return filter_attrs
