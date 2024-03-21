#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    mylist = sorted(list(a_dictionary))
    for elem in mylist:
        print("{} : {}".format(elem, a_dictionary.get(elem)))
