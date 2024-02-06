#!/usr/bin/python3
"""JSON representation module"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string."""
    deserialized_data = json.loads(my_str)
    return deserialized_data
