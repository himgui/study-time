#!/usr/bin/env python3

"""
Vowel repetition
"""

vowels = ["a","e","i","o","u"]

word_one = input("Type a random word")
#word_two = input("Type a second random word")
#word_three = input("Type a third random word")

for vowels in word_one:
    print(word_one,vowels[vowels])