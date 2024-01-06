#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    else:
        temp = my_list
        new_element = 9
        temp[idx] = new_element
        new_list = temp
        return new_list
