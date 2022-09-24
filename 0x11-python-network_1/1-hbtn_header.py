#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- displays the value of the X-Request-Id variable
- found in the header of the response.
"""


from urllib.request import urlopen, Request
from sys import argv

if __name__ == '__main__':
    req = Request(argv[1])
    with urlopen(req) as response:
        header = dict(response.headers)
        print(header['X-Request-Id'])
