#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    maxkey = None
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            if a_dictionary[key] >= max:
                maxkey = key
                max = value
    return maxkey
