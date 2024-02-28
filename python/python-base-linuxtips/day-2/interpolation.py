"""
Send email to users.
"""

__version__ = "0.1.1"

import sys
import os
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]

if not arguments:
    print("Type the the file name of emails.")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

with smtplib.SMTP(host="localhost", port=8025) as server:

    for line in open(filepath):
        name, email = line.split(",")

        text =  (
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
        from_ = "gui@mail.com"
        to = ",".join([email])
        message = MIMEText(text)
        message["Subject"] = "Buy more!"
        message["From"] = from_
        message["To"] = to

        server.sendmail(from_, to, message.as_string())