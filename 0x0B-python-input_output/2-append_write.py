#!/usr/bin/python3
"""append to a file module"""


def append_write(filename="", text=""):
    """appends string at end of text file & returns numb of char. written"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
