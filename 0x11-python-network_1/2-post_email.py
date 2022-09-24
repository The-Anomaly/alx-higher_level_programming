#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- displays the value of the X-Request-Id variable
- found in the header of the response.
"""


from urllib.request import urlopen, Request
from sys import argv
from urllib.parse import urlencode

if __name__ == '__main__':
    values = {'email': argv[2]}

    data = urlencode(values)
    data = data.encode('ascii')
    req = Request(argv[1], data)

    with urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
