#!/usr/bin/python3
"""
printing text module.
it contains a function that prints text.
It also includes a docstring that explains what this function does.
"""


def text_indentation(text):
    """prints 2 new lines after characters: ., ? and :.
    text must be string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for delimiters in ".?:":
        text = (delimiters + "\n\n").join([line.strip(" ") for line
                                           in text.split(delimiters)])

    print(text, end="")
