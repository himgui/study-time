#!/usr/bin/env python3

"""
Notepad

$ notes.py add "Title"
Tag: Football
Text: 
Palmeiras, meu Palmeiras!

$ notes.py read --tag=tech
...
...
"""

__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specify a subcommad: {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print("Invalid command: {arguments[0]}")

if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"Title: {title}")
            print(f"Text: {text}")
            print("-" * 30)
            print()

if arguments[0] == "new":
    title = arguments[1] # TODO: Do exception
    text = [
        f"{title}",
        input("Tag: ").strip(),        
        input("Text: ").strip(),       
    ]
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")