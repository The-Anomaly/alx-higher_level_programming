#!/usr/bin/python3
"""
    Module for text indentation

    Functions:
        text_indentation(string)
"""


def text_indentation(text):
    """ Function that prints a text with 2 new lines
        after each of these characters: ., ? and :

    Args:
        text (str): text to be printed

    Returns:
        prints indented string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i, ch in enumerate(text):
        if not (i > 0 and ch == " " and text[i-1] in ['.', '?', ':']):
            print(ch, end="")
        if ch in ['.', '?', ':']:
            print("\n")
