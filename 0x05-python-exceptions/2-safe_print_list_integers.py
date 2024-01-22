#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0

    while i < x:
        try:
            print("{}".format(my_list[i]), end='')
            i += 1

        except (IndexError):
            print("{:d}".format(my_list[i]), end='')

    print("")
    return i
