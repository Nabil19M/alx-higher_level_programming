#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Defines a Sqaure class inherited from geometry"""


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def print(self):
        print(f"[Sqaure] {self.__size}/{self.__size}")

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
