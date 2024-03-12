#!/usr/bin/python3
for i in range(10):
    for ii in range(10):
        if ii > i:
            if i == 8 and ii == 9:
                print("{0}{1}".format(i, ii))
            else:
                print("{0}{1}, ".format(i, ii), end='')
