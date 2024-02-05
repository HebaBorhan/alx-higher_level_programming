#!/usr/bin/python3
"""
module of List Class and MyList subclass
"""


class list():
    """list class"""
    def __init__(self, iterable=None):
        self.data = [] if iterable is None else list(iterable)
    

class MyList(list):
    """derived class MyList"""
    def print_sorted(self):
        """print elements in sorted order"""
        print(" ".join([str(i) for i in sorted(set(self.data
                                                   ))]))
        