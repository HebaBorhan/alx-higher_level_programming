#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if my_list:
        new_list = list(map(lambda x : x*number, my_list))
        return new_list
