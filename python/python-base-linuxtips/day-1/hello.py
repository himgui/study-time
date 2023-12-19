#!/usr/bin/env python3

"""
Best hello world app.
"""
__version__= "0.1.2"
__author__= "Guilherme"
__license__= "Unlicensed"

import os

current_language = os.getenv("LANG")[:5]
#current_language = "es_SP"

msg= {
    "pt_BR": "Olá, Mundo",
    "en_US": "Hello, World",
    "es_SP": "Holá, mundo"
}

print(msg[current_language])