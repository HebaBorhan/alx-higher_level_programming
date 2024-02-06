#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """writes a string to a text file & returns number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        print(f.write(text))

    f.close()
