#!/usr/bin/env python3

"""
Prefix Calculator

Operations available:
sum -> +
sub -> -
mul -> *
div -> /

"""
__version__= "0.1.0"
__author__= "Guilherme"
__license__= "Unlicensed"

welcome_msg = "Welcome to the Prefix Calculator! Your daily math helper :)"
print(welcome_msg)
print("\n -------------------------------------- ")

username = input("Start by writing your name: ")
aftername_msg = f"Hey {username}, you can use the Prefix Calculator using sum, sub, mul or div."

print(aftername_msg)

operation_type = input("Enter the operation type yo want to do: ")
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if '+' in operation_type:
    print(n1 + n2)
elif '-' in operation_type:
    print(n1 - n2)
else:
    print("No specified symbols found in the input.")