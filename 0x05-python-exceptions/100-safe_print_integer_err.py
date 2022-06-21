#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True

    except TypeError as te:
        sys.stderr.write("Exception : {}\n".format(te))
        return False

    except ValueError as ve:
        sys.stderr.write("Exception : {}\n".format(ve))
        return False
