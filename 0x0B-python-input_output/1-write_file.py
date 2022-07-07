#!/usr/bin/python3
"""Module to write to a file"""


def write_file(filename="", text=""):
    """Defines how to write to a file

    Args:
        filename {string}
        text {string}
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
