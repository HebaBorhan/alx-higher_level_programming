#!/usr/bin/python3
"""square module"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes function"""
        super().__init__(id, x, y, size, size)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.y = value

    def area(self):
        """Return the area of this rectangle."""
        return self.size ** 2
    
    def display(self):
        print('\n' * self.y, end="")
        print(((" " * self.x ) + "#" * self.width + '\n') * self.width, end="")

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        if args:
            attr_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
