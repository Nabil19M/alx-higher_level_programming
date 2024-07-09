#!/usr/bin/python3
""" defenition of function return objects dict.
    """


def lookup(obj):
    """ returns the list of available attributes and methods of an object

    Args:
        obj (): any object type

    Returns:
        list: list of available attributes
    """
    return obj.__dict__
