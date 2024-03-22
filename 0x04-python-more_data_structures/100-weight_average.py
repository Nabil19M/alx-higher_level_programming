#!/usr/bin/python3
def weight_average(my_list=[]):
    avg = 0
    num = denum = 0
    if my_list == []:
        return 0
    for s in my_list:
        num += s[0] * s[1]
        denum += s[1]
    avg = num / denum
    return avg
