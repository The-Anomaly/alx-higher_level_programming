#!/usr/bin/python3
"""A script that
- takes in a URL,
- sends a request to the passed URL
- displays the body of the response.
"""


import requests
from sys from argv

if __name__ == "__main__":
    data = {'email': argv[2]}

    r = requests.post(argv[1], data=data)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
