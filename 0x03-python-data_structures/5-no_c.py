#!/usr/bin/python3
def no_c(my_string):
    if len(my_string) == 0:
        return None
    else:
        my_string = (my_string.translate({ord(i): None for i in 'cC'}))
        return my_string
