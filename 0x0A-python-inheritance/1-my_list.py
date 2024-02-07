#!/usr/bin/python3
"""
module of List Class and MyList subclass
"""


class MyList(list):
    """derived class MyList"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))

if __name__ == "__main__":
    my_list = MyList()
    print(type(my_list) == MyList)
