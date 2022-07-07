#!/usr/bin/python3
import json


"""Module that creates an object from a json file"""


def load_from_json_file(filename):
    """Defines how to create an object from a json file
    Args:
        filename
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
