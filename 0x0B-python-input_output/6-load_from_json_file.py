#!/usr/bin/python3
""" importing json"""
import json
""" Defines function that creates an Object from a “JSON file”
    """


def load_from_json_file(filename):
    """ def load_from_json_file(filename):

    Args:
        filename (_str_): name of file
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
