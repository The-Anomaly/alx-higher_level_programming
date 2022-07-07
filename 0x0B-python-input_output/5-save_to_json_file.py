#!/usr/bin/python3
"""Module to write an object to a text file in JSON"""


import json


def save_to_json_file(my_obj, filename):
    """Defines how to write JSOn to a file
    Args:
        my_obj
        filename
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
