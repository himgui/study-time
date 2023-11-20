#!/usr/bin/env python3

"""
Best hello world app.
"""
__version__= "0.0.1"
__author__= "Guilherme"
__license__= "Unlicensed"

import os

current_language = os.getenv("LANG")[:5]
msg="Palmeiras"

if current_language == "pt_BR":
    msg = "Olá mundo!"
elif current_language == "en_US":
    msg = "This is America"
print(msg)