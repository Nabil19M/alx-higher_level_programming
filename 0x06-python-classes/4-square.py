#!/usr/bin/python3
""" Defines Square class with private attributes"""


class Square:
    """ Represent a square."""
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        area = self.__size * self.__size
        return area
    
    def size(self):
        """ Retreive the current size of the square"""
        return self.__size
    
    def size(self, value):
        """ set a current size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
