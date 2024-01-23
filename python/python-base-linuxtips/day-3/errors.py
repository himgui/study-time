#!/usr/bin/env python3

"""
Working with errors cases with Python.
"""
import os
import sys

if os.path.exists("names.txt"):
    print("The file exists.")
    input("...") #Race Condition
    names = open("names.txt").readlines()
else:
    print("[Error]: File not found.")
    sys.exit(1)
# LBYL - Look Before You Leap
if len(names) >=3:
    print(names[2])
else:
    print("[Error]: Missing name in the list.")
    sys.exit(1)