#!/usr/bin/python3
class MyList(list):
    """ Defines class Mylist

    Args:
        list (int): parent class of Mylist
    """

    def print_sorted(self):
        """print sorted list of integers
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)
