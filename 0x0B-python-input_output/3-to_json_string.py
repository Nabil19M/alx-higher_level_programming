#!/usr/bin/python3
""" importing json"""
import json
""" Defines function that returns json representation of object
    """


def to_json_string(my_obj):
    """function that returns json representation of object

    Args:
        my_obj (_dict_): dictionary

    Returns:
       _dict_: json representation of object
    """
    return json.dumps(my_obj)
