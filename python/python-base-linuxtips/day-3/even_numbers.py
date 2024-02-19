#!/usr/bin/env python3

"""
Create a program that print even numbers from 1 to 200.

Ex.
2
4
...
"""

for num in range(1,201):
    if num % 2 != 0:
        continue
    print(num)