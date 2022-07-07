#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """Read a file
    Args:
        filename {string}
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
