#!/usr/bin/python3
"""A script that
- takes in a letter
- sends a POST request to http://0.0.0.0:5000/search_user
- with the letter as a parameter.
"""


import requests
from sys import argv

if __name__ == "__main__":
    data = {'q': ""}
    data['q'] = argv[1]
    url = 'http://0.0.0.0:5000/search_user'

    r = requests.post(url, data=data)
    try:
        res =  r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
