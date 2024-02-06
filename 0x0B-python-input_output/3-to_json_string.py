#!/usr/bin/python3
"""JSON representation module"""
import json


def to_json_string(my_obj):
    """Converts a Python object into a JSON string."""
    serialized_data = json.dumps(my_obj)
    return serialized_data
