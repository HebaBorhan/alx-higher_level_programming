#!/usr/bin/python3
def uppercase(str):
    for c in str:
        value = ord(c)
        if 97 <= value <= 122:
            print("{}".format(chr(value - 32)), end='')
        else:
            print("{}".format(c), end='')
