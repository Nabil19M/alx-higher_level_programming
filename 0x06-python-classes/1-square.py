#!/usr/bin/python3
""" Defines Square class with private attributes"""


class Square:
    """ Represent a square."""
    def __init__(self, size) -> None:
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size