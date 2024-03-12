#!/usr/bin/python3
j = 1
for i in range(26):
    ii = 97 + 26 - j
    j += 1
    if ii % 2 == 0:
        char = chr(ii)
    else:
        char = chr(ii - 32)
    print("{}".format(char), end='')
