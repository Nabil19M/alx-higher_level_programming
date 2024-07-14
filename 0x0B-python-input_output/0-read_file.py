#!/usr/bin/python3
""" Defines A function to read files
    """


def read_file(filename=""):
    """
        function to read file passing its name as arg
    Args:
        filename (str):file name to be read. Defaults to "".
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file.readline():
            print(line)
