#!/usr/bin/python3
""" Defines function to json representation of an object
    """


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: The object instance to be serialized.

    Returns:
        dict: A dictionary containing the object's serializable attributes.
    """
    return obj.__dict__
