#!/usr/bin/env python3

"""
Sending emails!
"""

import smtplib

SERVER = "localhost"
PORT = 8025


FROM = "myemail@gmail.com"
TO = ["destination1@server.com", "destination2@server.com"]
SUBJECT = "My second python email"
TEXT = """\
This is my email sent using Python.
<b> Hello World <\b>
"""

message = f"""From: {FROM}
To: {TO}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM,TO,message)