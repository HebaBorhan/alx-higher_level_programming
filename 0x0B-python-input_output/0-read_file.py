#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """Read a text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
