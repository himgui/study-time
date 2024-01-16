"""
Send email to users.
"""

__version__ = "0.1.1"

import sys
import os

arguments = sys.argv[1:]

if not arguments:
    print("Type the the file name of emails.")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

for line in open(filepath):
    name, email = line.split(",")


    print(f"Sending the email to: {email}")
    print()
    print(
        open(templatepath).read()
        % {
            "name": name,
            "team": "Palmeiras",
            "text": "a lot of titles",
            "link": "palmeiras.com.br",
            "spots": 5,
            "price": 100.5,
        }
    )