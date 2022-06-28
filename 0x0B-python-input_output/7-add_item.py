#!/usr/bin/python3
"""Creating a script that adds args to Python list and saves them"""

import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    loadfile = load_from_json_file("add_item.json")

except FileNotFoundError:
    loadfile = []
argc = len(sys.argv)
for idx in range(1, argc):
    loadfile.append(sys.argv[idx])
save_to_json_file(loadfile, "add_item.json")
