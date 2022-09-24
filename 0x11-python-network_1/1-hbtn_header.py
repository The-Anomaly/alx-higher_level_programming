#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.
"""


from urllib.request import urlopen, Request
from sys import argv

if len(argv) >= 2:
    req = Request(argv[1])
    with urlopen(req) as response:
        header = response.info()
        print(f"{header['X-Request-Id']}")
