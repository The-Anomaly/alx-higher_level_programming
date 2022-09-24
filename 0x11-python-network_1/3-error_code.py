#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- displays the body of the response in utf-8
"""


from urllib.request import urlopen, Request
from sys import argv
from urllib.error import HTTPError

if __name__ == '__main__':
    req = Request(argv[1])

    try:
        with urlopen(req) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except HTTPError as e:
        print(f"Error code: {e.code}")
