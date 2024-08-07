#!/usr/bin/python3
""" Defines A function to overwrite files
    """


def write_file(filename="", text=""):
    """ function to overwrite files

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
