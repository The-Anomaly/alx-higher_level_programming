#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import requests


r = requests.get('https://alx-intranet.hbtn.io/status')
print(f"""Body response:
\t- type: {type(r.text)}
\t- content: {r.text}""")
