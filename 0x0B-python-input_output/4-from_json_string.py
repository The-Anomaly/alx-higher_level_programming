#!/usr/bin/python3
"""Module to create JSO string from object"""


import json


def from_json_string(my_str):
    """Defines how to create a JSON string from an object
    Args:
        my_str {string}
    """
    return json.loads(my_str)
