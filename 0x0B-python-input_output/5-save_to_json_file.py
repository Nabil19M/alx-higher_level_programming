#!/usr/bin/python3
""" importing json"""
import json
""" Defines function that writes an Object to a text file
    , using a JSON representation
    """


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj (_dict_): _description_
        filename (_str_): _description_
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
