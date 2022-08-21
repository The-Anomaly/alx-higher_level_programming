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

    flag = 0

    for ch in text:
        if flag == 0:
            if ch == " ":
                continue
            else:
                flag = 1
        if flag == 1:
            if ch in ['.', '?', ':']:
                print(ch)
                print()
                flag = 0
            else:
                print(ch, end="")
