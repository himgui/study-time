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


while True:
    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("What's the tag?").strip().lower()

        for line in open(filepath):
            title, tag, text = line.split("\t")
            if tag.lower() == arg_tag:
                print(f"Title: {title}")
                print(f"Text: {text}")
                print("-" * 30)
                print()

    if arguments[0] == "new":
        try:
            title = arguments[1]
        except IndexError:
            title = input("What's the title?").strip().title()
        text = [
            f"{title}",
            input("Tag: ").strip(),        
            input("Text: ").strip(),       
        ]
        with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")
    
    cont = input(f"Do you want to continue {arguments[0]} with the notes? [N/Y]").strip().lower()
    if cont != "y":
        break