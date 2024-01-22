#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end='')
    
    except TypeError:
        for i in range(x):
            print("{:d}".format(my_list[i]), end='')
    print("\nnb_print: {:d}".format(x))
