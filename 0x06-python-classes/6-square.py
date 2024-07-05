#!/usr/bin/python3
""" Defines Square class with private attributes"""


class Square:
    """ Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

    def area(self):
        """Return the current area of the square."""
        area = self.size * self.size
        return area

    def my_print(self):
        """ print the square as hashes"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.position[1]):
            print()
        if self.size:
            for r in range(self.size):
                for i in range(self.position[0]):
                    print(" ", end="")
                for c in range(self.size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def size(self):
        """ Retreive the current size of the square"""
        return (self.__size)

    @property
    def position(self):
        """ Retreive the current position of the square"""
        return (self.__position)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
