#!/usr/bin/python3
""" Defines Student calss
    """


class Student:
    """ Defines a Student calss
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self,  attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) is list and
                all(type(item) is str for item in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        try:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
        except KeyError:
            pass
