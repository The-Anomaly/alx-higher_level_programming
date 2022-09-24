#!/usr/bin/python3
"""A script that
- takes a URL
- sends a request to the URL
- displays the value of the variable X-Request-ID in the response header
"""

import requests
from sys import argv

r = requests.get(argv[1])
print(r.headers.get('X-Request-ID'))
