#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count = count + 1
        except IndexError:
            None
    print()
    return (count)

my_list = [1, 2, 3, 4]
x = len(my_list) + 1

nb_print = safe_print_list(my_list, x)
print("{:d}".format(nb_print))