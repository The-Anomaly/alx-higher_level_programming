#!/usr/bin/python3
"""
    Module to print a name

    Functions:
        say_my_name(string, string) -> string
"""


def say_my_name(first_name, last_name=""):
    """ Definition of a function to print a name

    Args:
        first_name (string): first name
        last_name (string): last name. defaults to an empty string

    Returns:
        full name: a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    return print("My name is {} {}".format(first_name, last_name))
