#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_string = (my_string.translate({ord(i): None for i in 'cC'}))
        return new_string

    else:
        return my_string
