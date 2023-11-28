#!/usr/bin/env python

""" Prints a simple multiplication table from 1 to 10"""
__version__ = "0.1.0"
__author__ = "Guilherme"

numbers = list(range(1,11))
# Iterable List
for number in numbers:
    print("Multiplication table from:", number)
    for other_number in numbers:
        print(number * other_number)
    print("------------") 