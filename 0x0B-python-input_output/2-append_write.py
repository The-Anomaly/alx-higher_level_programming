#!/usr/bin/python3
"""Module to append text to a file"""


def append_write(filename="", text=""):
    """Defines how to append text to a file
    Args:
        filename {string}
        text {string}
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
