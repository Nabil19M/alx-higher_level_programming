#!/usr/bin/python3
"""Defines a Base class
    """


class Base:
    """Defines A base class for all other incoming classes
    """    
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
