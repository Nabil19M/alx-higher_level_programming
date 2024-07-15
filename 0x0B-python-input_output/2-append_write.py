#!/usr/bin/python3
""" Defines A function to write into files
    """


def write_file(filename="", text=""):
    """ function to write into files

    Args:
        filename (str, empty): file name. Defaults to "".
        text (str, empty): text to be written. Defaults to "".
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
