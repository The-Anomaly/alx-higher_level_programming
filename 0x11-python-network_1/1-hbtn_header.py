#!/usr/bin/python3
"""A script that
- takes in a URL, and an email
- sends a POST request to the URL with the email as a parameter
- displays the body of the response in utf-8
"""


from urllib.request import urlopen, Request
from sys import argv

if __name__ == '__main__':
    req = Request(argv[1])
    with urlopen(req) as response:
        header = dict(response.headers)
        print(header.get('X-Request-Id'))
