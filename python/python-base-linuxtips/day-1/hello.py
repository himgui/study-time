#!/usr/bin/env python3

"""
Best hello world app.
"""
__version__= "0.1.2"
__author__= "Guilherme"
__license__= "Unlicensed"

import os
import sys

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        # TODO: Logging
        print(f"[ERROR] {str(e)}")
        print("This is not a valid caracther. Use '='")
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
    
    arguments[key] = value

# Debugging:
current_language = arguments["lang"]
print(f"{current_language=}")
if current_language is None:
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg= {
    "pt_BR": "Olá, Mundo",
    "en_US": "Hello, World",
    "es_SP": "Holá, mundo"
}

try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, find the available here {list(msg.keys())}")
    sys.exit(1)
print(message * int(arguments["count"]))