#!/usr/bin/python3
"""JSON representation module"""
import json


def load_from_json_file(filename):
    """creates an Object from a "JSON file"."""
    with open(filename, "r", encoding="utf-8") as f:
        deserialized_data = json.load(f)
        return (deserialized_data)
