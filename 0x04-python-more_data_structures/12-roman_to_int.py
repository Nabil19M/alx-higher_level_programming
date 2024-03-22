#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    rom = roman_string
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in list(rom):
        if i not in dict:
            return 0
    res = dict[rom[len(roman_string) - 1]]
    for i in reversed(range(len(roman_string) - 1)):
        if dict[rom[i]] < dict[rom[i + 1]]:
            res -= (dict[rom[i]])
        else:
            res += dict[rom[i]]
    return res
