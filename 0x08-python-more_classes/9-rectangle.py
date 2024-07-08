#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        del self

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        result = []
        for i in range(self.height):
            result.append(str(self.print_symbol) * self.width)
        return "\n".join(result)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def area(self):
        """ function to calculate area of rectangle

        Returns:
            int : area of rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """ function to calculate perimeter of rectangle

        Returns:
            int : perimeter of rectangle
        """
        if self.width and self.height:
            return 2 * (self.height + self.width)
        return 0

    def print(self):
        """print the object by #

        Returns:
            0: if width or height equal zero
        """
        if self.width and self.height:
            for i in range(self.height):
                print(self.print_symbol * self.width)
        else:
            return 0
