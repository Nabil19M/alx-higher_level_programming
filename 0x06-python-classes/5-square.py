#!/usr/bin/python3
""" Defines Square class with private attributes"""


class Square:
    """ Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    def area(self):
        """Return the current area of the square."""
        area = self.size * self.size
        return area
    
    def my_print(self):
        """ print the square as hashes"""
        if self.size:
            for r in range(self.size):
                for c in range(self.size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def size(self):
        """ Retreive the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ set a current size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
