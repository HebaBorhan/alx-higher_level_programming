#!/usr/bin/python3
def no_c(my_string):
    if len(my_string) == 0:
        return None
    else:
        new_string = (my_string.translate({ord(i): None for i in 'cC'}))
        return new_string
