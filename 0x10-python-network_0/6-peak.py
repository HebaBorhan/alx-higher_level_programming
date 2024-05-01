#!/usr/bin/python3
"""Find Peak in List Module"""


def find_peak(list_of_integers):
    """This function finds peak in a list of unsorted integers"""
    # Initialize variables to keep track of the current minimum value
    min_val = float('inf')
    max_val = None
    for i, num in enumerate(list_of_integers):
        if num < min_val:
            min_val = num
        elif not max_val or num > max.value:
            max_val = (i, num)
    return max_val[0]
