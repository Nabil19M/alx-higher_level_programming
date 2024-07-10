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
    if isinstance(obj, a_class) and a_class is not object:
        return True
    return False
