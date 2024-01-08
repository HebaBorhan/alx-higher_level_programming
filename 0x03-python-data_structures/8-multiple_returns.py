#!/usr/bin/python3

def multiple_returns(sentence):
    str_tuple = tuple(sentence)

    length = len(str_tuple)

    first = str_tuple[0]

    if length == 0:
        first = None

    return length, first
