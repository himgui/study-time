#!/usr/bin/env python

""" Prints a simple multiplication table from 1 to 10"""
__version__ = "0.1.1"
__author__ = "Guilherme"

numbers = list(range(1,11))
# Iterable List
for n1 in numbers:
    print("{:-^18}".format(f"Multiplication Table of {n1}"))
    print()
    for n2 in numbers:
        result =  n1 * n2
        print  ("{:^18}".format(f"{n1} x {n2} = {result}"))
    print("#" * 18)
print("\U0001F389")