#!/usr/bin/python3
"""append to a file module"""


def append_write(filename="", text=""):
    """appends string at the end of a text file & returns numb of characters written"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.append(text))
