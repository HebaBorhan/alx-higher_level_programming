#!/usr/bin/python3
"""JSON representation module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        serialized_data = json.dump(my_obj, filename)
        return serialized_data
