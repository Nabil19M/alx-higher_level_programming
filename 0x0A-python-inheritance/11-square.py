#!/usr/bin/python3
""" Rectangle module imported"""
Rectangle = __import__('9-rectangle').Rectangle
"""Defines a Sqaure class inherited from geometry"""


class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
