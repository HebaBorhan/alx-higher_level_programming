#!/usr/bin/python3
def uppercase(str):
    for c in str:
        value = ord(c)
        if 97 <= value <= 122:
            value = value - 32

        print("{}".format(chr(value)), end='')

    print("{}".format("\n"), end='')
