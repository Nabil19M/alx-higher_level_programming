#!/usr/bin/python3
""" Defines Square class with private attributes"""


class Square:
    """ Represent a square."""
    def __init__(self, size=0) -> None:
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
