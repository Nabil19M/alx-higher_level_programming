#!/usr/bin/python3
""" check for instantiation of object from specific class
    """


def is_same_class(obj, a_class):
    """check through isinstance function.

        Args:
        obj ( any type):
            a_class (any class):

        Returns:
            True : if object has instatiated from specific class
        """
    if type(obj) == a_class:
        return True
    return False
