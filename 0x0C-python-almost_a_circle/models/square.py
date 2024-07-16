#!/usr/bin/python3
""" importing the Rectangle class for inhertiance """

from models.rectangle import Rectangle
""" Define a rectangle class inhertied from base class
    """


class Square(Rectangle):
    """defineing Square calss

    Args:
        Rectangle (_cls_): the parent class
    """

    def __init__(self, size, x=0, y=0, id=None):
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
        return self.__dict__
