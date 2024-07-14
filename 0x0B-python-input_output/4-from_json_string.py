#!/usr/bin/python3
""" importing json"""
import json
""" Defines function treturns an object (Python DS) 
    represented by a JSON string
    """


def from_json_string(my_str):
    """function that returns json representation of object

    Args:
        my_str (_dict_): dictionary

    Returns:
       _dict_: json representation of object
    """
    return json.loads(my_str)
