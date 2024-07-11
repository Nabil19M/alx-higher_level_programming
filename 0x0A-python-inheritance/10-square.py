#!/usr/bin/python3
""" Rectangle module imported"""
Rectangle = __import__('9-rectangle').Rectangle
"""Defines a Sqaure class inherited from geometry"""


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return super().area()