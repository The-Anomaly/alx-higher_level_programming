#!/usr/bin/python3
"""A script that
- takes in a URL,
- sends a request to the passed URL
- displays the body of the response.
"""


import requests
from sys from argv

if __name__ == "__main__":

    r = requests.get(argv[1])
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
