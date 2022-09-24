#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""


from urllib.request import urlopen, Request


req = Request('https://alx-intranet.hbtn.io/status')
with urlopen(req) as response:
    body = response.read()
    type = type(body)
    utf_body = body.decode("utf-8")
    print(f"""Body response:\n\t- type: {type}
\t- content: {body}
\t- utf8 content: {utf_body}""")
