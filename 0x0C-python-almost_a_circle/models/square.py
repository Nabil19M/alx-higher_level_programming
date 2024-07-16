#!/usr/bin/python3
""" importing the Rectangle class for inhertiance """

from rectangle import Rectangle
""" Define a rectangle class inhertied from base class
    """


class Square(Rectangle):
    """defineing Square calss

    Args:
        Rectangle (_cls_): the parent class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square

        Args:
            size (int): The size of the new square
            x (int): The x coordinate of the new square
            y (int): The y coordinate of the new square
            id (int): The id of the new square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the instance attributes

        Args:
            *args: Variable length argument list for updating attributes
            **kwargs: Arbitrary keyword arguments for updating attributes
        """
        if args:
            att_list = ["id", "size", "x", "y"]
            for k, v in enumerate(args):
                if k < len(att_list):
                    setattr(self, att_list[k], v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ generate dict representation for square

        Returns:
            _dict_: string representation of sqaure attributes
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))
