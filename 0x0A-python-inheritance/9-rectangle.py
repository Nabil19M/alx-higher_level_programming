#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Defines a Rectangle class inherited from geometry"""


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def print(self):
        print(f"[Rectangle] {self.__width}/{self.__height}")

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
