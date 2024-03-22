#!/usr/bin/python3
def weight_average(my_list=[]):
    avg = 0
    num = denum = 0
    if my_list == [] or is None:
        return 0
    for s, w in my_list:
        num += s * w
        denum += w
    avg = num / denum
    return avg
