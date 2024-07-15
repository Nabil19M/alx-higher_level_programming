#!/usr/bin/python3
"""import json function to make an add_item function
    """
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""a script that adds all arguments to a Python list,
    and then save them to a file
    """
filename = "add_item.json"
my_obj = []
try:
    my_obj = load_from_json_file(filename)
except:
    my_obj = []

for arg in sys.argv[1:]:
    my_obj.append(arg)
save_to_json_file(my_obj, filename)
