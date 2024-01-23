#!/usr/bin/env python3

"""
Working with errors cases with Python.
"""
import os
import sys

# EAFP - Easy to Ask Forgiveness than permission > LBYL

# Testing a error using raise.
try:
    raise RuntimeError("There is an error")
except Exception as e:
    print(str(e))

try:
    names = open("names.txt").readlines() # FileNotFoundError
except (FileNotFoundError, ZeroDivisionError) as e:
    print(f"[Error]: {str(e)}.")
    sys.exit(1)
    # TODO: Use retry
else: 
    print("Sucess!")
finally:
    print("Always execute this.")

try:
    print(names[2])
except:
    print("[Error]: Missing name in the list.")
    sys.exit(1)