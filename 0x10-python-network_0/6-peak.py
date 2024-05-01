#!/usr/bin/python3
"""Find Peak in List Module"""


def find_peak(list_of_integers):
    """This function finds peak in a list of unsorted int."""
    if not list_of_integers:
        return None
    min, max = 0, len(list_of_integers) - 1
    while min < max:
        mid = (min + max) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            min = mid + 1
        else:
            max = mid
    return list_of_integers[min]
