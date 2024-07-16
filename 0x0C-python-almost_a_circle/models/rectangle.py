#!/usr/bin/python3
""" importing the base class for inhertiance """
from models.base import Base
""" Define a rectangle class inhertied from base class
    """


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): The id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Return a string representation of the rectangle."""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ calculate area of rectangle

        Returns:
            _int_: area of rectangle
        """
        return self.height * self.width

    def display(self):
        """ display rectangle with #
        """
        for y in range(self.y):
            print()
        for r in range(self.height):
            for x in range(self.x):
                print(" ", end='')
            for c in range(self.width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """ update instance using args
            and kwargs that assigns a key/value argument to attributes
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for k, value in kwargs.items():
                setattr(self, k, value)
