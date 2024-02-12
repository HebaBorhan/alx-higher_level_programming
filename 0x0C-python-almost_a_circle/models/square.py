#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes function"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def display(self):
        """Display the Square by #."""
        print('\n' * self.y, end="")
        print(((" " * self.x) + "#" * self.width + '\n') * self.width, end="")

    def __str__(self):
        """printing Square string"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the position and size of the Square."""
        if args:
            attr_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Convert a Square object into a dictionary."""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
