#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    my_list = list(set(my_list))
    for i in my_list:
        add += i
    return add
