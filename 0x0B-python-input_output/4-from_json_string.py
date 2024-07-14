#!/usr/bin/python3
""" importing json"""
import json
""" Defines function that returns python representation of object
    """


def from_json_string(my_str):
    return json.loads(my_str)
